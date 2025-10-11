pub struct Agent {
    pub name: String,
}

impl Agent {
    pub fn new(name: &str) -> Self {
        Agent { name: name.to_string() }
    }

    pub fn perform(&self) -> String {
        format!("Agent {} performing task", self.name)
    }
}
