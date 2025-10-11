// Prevents additional console window on Windows in release
#![cfg_attr(not(debug_assertions), windows_subsystem = "windows")]

use tauri::{CustomMenuItem, Manager, Menu, MenuItem, Submenu, SystemTray, SystemTrayMenu};
use std::sync::{Arc, Mutex};

mod terminal;
mod ai;
mod plugins;
mod config;

use terminal::TerminalManager;
use ai::AIEngine;

#[derive(Clone, serde::Serialize)]
struct TerminalOutput {
    data: String,
}

// Global state
struct AppState {
    terminal_manager: Arc<Mutex<TerminalManager>>,
    ai_engine: Arc<Mutex<AIEngine>>,
}

#[tauri::command]
async fn create_terminal(state: tauri::State<'_, AppState>) -> Result<String, String> {
    let mut manager = state.terminal_manager.lock().unwrap();
    manager.create_session()
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn write_to_terminal(
    state: tauri::State<'_, AppState>,
    session_id: String,
    data: String,
) -> Result<(), String> {
    let manager = state.terminal_manager.lock().unwrap();
    manager.write(&session_id, data.as_bytes())
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn read_from_terminal(
    state: tauri::State<'_, AppState>,
    session_id: String,
) -> Result<String, String> {
    let manager = state.terminal_manager.lock().unwrap();
    manager.read(&session_id)
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn ai_complete_command(
    state: tauri::State<'_, AppState>,
    partial_command: String,
) -> Result<Vec<String>, String> {
    let ai = state.ai_engine.lock().unwrap();
    ai.complete_command(&partial_command)
        .await
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn ai_explain_command(
    state: tauri::State<'_, AppState>,
    command: String,
) -> Result<String, String> {
    let ai = state.ai_engine.lock().unwrap();
    ai.explain_command(&command)
        .await
        .map_err(|e| e.to_string())
}

#[tauri::command]
async fn natural_to_shell(
    state: tauri::State<'_, AppState>,
    natural_language: String,
) -> Result<String, String> {
    let ai = state.ai_engine.lock().unwrap();
    ai.natural_to_shell(&natural_language)
        .await
        .map_err(|e| e.to_string())
}

fn main() {
    // Create application menu
    let menu = Menu::new()
        .add_submenu(Submenu::new(
            "File",
            Menu::new()
                .add_item(CustomMenuItem::new("new_tab", "New Tab").accelerator("Ctrl+T"))
                .add_item(CustomMenuItem::new("new_window", "New Window").accelerator("Ctrl+N"))
                .add_native_item(MenuItem::Separator)
                .add_item(CustomMenuItem::new("settings", "Settings").accelerator("Ctrl+,"))
                .add_native_item(MenuItem::Separator)
                .add_item(CustomMenuItem::new("quit", "Quit").accelerator("Ctrl+Q")),
        ))
        .add_submenu(Submenu::new(
            "Edit",
            Menu::new()
                .add_native_item(MenuItem::Copy)
                .add_native_item(MenuItem::Paste)
                .add_native_item(MenuItem::SelectAll),
        ))
        .add_submenu(Submenu::new(
            "View",
            Menu::new()
                .add_item(CustomMenuItem::new("zoom_in", "Zoom In").accelerator("Ctrl+="))
                .add_item(CustomMenuItem::new("zoom_out", "Zoom Out").accelerator("Ctrl+-"))
                .add_item(CustomMenuItem::new("zoom_reset", "Reset Zoom").accelerator("Ctrl+0"))
                .add_native_item(MenuItem::Separator)
                .add_item(CustomMenuItem::new("toggle_fullscreen", "Toggle Fullscreen").accelerator("F11")),
        ));

    // Create system tray
    let tray_menu = SystemTrayMenu::new()
        .add_item(CustomMenuItem::new("show", "Show"))
        .add_item(CustomMenuItem::new("hide", "Hide"))
        .add_native_item(tauri::SystemTrayMenuItem::Separator)
        .add_item(CustomMenuItem::new("quit", "Quit"));
    
    let system_tray = SystemTray::new().with_menu(tray_menu);

    // Initialize application state
    let terminal_manager = Arc::new(Mutex::new(TerminalManager::new()));
    let ai_engine = Arc::new(Mutex::new(AIEngine::new()));

    tauri::Builder::default()
        .menu(menu)
        .system_tray(system_tray)
        .manage(AppState {
            terminal_manager,
            ai_engine,
        })
        .invoke_handler(tauri::generate_handler![
            create_terminal,
            write_to_terminal,
            read_from_terminal,
            ai_complete_command,
            ai_explain_command,
            natural_to_shell,
        ])
        .on_menu_event(|event| {
            match event.menu_item_id() {
                "new_tab" => {
                    event.window().emit("menu:new-tab", ()).unwrap();
                }
                "new_window" => {
                    // Create new window
                }
                "settings" => {
                    event.window().emit("menu:settings", ()).unwrap();
                }
                "quit" => {
                    std::process::exit(0);
                }
                _ => {}
            }
        })
        .on_system_tray_event(|app, event| {
            if let tauri::SystemTrayEvent::MenuItemClick { id, .. } = event {
                match id.as_str() {
                    "show" => {
                        let window = app.get_window("main").unwrap();
                        window.show().unwrap();
                        window.set_focus().unwrap();
                    }
                    "hide" => {
                        app.get_window("main").unwrap().hide().unwrap();
                    }
                    "quit" => {
                        std::process::exit(0);
                    }
                    _ => {}
                }
            }
        })
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
