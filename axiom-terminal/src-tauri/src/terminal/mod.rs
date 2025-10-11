use portable_pty::{native_pty_system, CommandBuilder, PtySize};
use std::collections::HashMap;
use std::io::{Read, Write};
use std::sync::{Arc, Mutex};
use uuid::Uuid;

pub struct TerminalSession {
    id: String,
    pty: Box<dyn portable_pty::MasterPty + Send>,
    writer: Box<dyn Write + Send>,
    reader: Box<dyn Read + Send>,
}

pub struct TerminalManager {
    sessions: HashMap<String, Arc<Mutex<TerminalSession>>>,
}

impl TerminalManager {
    pub fn new() -> Self {
        Self {
            sessions: HashMap::new(),
        }
    }

    pub fn create_session(&mut self) -> Result<String, Box<dyn std::error::Error>> {
        let pty_system = native_pty_system();

        let pair = pty_system.openpty(PtySize {
            rows: 24,
            cols: 80,
            pixel_width: 0,
            pixel_height: 0,
        })?;

        let cmd = if cfg!(target_os = "windows") {
            CommandBuilder::new("powershell.exe")
        } else {
            CommandBuilder::new("bash")
        };

        let _child = pair.slave.spawn_command(cmd)?;

        let writer = pair.master.take_writer()?;
        let reader = pair.master.try_clone_reader()?;

        let session_id = Uuid::new_v4().to_string();

        let session = TerminalSession {
            id: session_id.clone(),
            pty: pair.master,
            writer,
            reader,
        };

        self.sessions.insert(
            session_id.clone(),
            Arc::new(Mutex::new(session)),
        );

        Ok(session_id)
    }

    pub fn write(&self, session_id: &str, data: &[u8]) -> Result<(), Box<dyn std::error::Error>> {
        if let Some(session) = self.sessions.get(session_id) {
            let mut session_lock = session.lock().unwrap();
            session_lock.writer.write_all(data)?;
            session_lock.writer.flush()?;
            Ok(())
        } else {
            Err("Session not found".into())
        }
    }

    pub fn read(&self, session_id: &str) -> Result<String, Box<dyn std::error::Error>> {
        if let Some(session) = self.sessions.get(session_id) {
            let mut session_lock = session.lock().unwrap();
            let mut buffer = [0; 1024];
            let n = session_lock.reader.read(&mut buffer)?;
            Ok(String::from_utf8_lossy(&buffer[..n]).to_string())
        } else {
            Err("Session not found".into())
        }
    }

    pub fn resize(&self, session_id: &str, cols: u16, rows: u16) -> Result<(), Box<dyn std::error::Error>> {
        if let Some(session) = self.sessions.get(session_id) {
            let session_lock = session.lock().unwrap();
            session_lock.pty.resize(PtySize {
                rows,
                cols,
                pixel_width: 0,
                pixel_height: 0,
            })?;
            Ok(())
        } else {
            Err("Session not found".into())
        }
    }

    pub fn close_session(&mut self, session_id: &str) -> Result<(), Box<dyn std::error::Error>> {
        if let Some(session) = self.sessions.remove(session_id) {
            // The Arc will be dropped, and if no other references, the session will be closed
            Ok(())
        } else {
            Err("Session not found".into())
        }
    }
}
