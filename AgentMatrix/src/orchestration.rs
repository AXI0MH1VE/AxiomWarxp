use crate::agents::Agent;

pub struct Orchestrator {
    agents: Vec<Agent>,
}

impl Orchestrator {
    pub fn new() -> Self {
        Orchestrator { agents: vec![] }
    }

    pub fn add_agent(&mut self, agent: Agent) {
        self.agents.push(agent);
    }

    pub fn orchestrate(&self) -> Vec<String> {
        self.agents.iter().map(|a| a.perform()).collect()
    }
}
