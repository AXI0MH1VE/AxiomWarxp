class DevDollzAgent:
    def __init__(self, name: str):
        self.name = name

    def perform_task(self, task: str) -> str:
        print(f"Agent {self.name} performing task: {task}")
        return f"Task {task} completed"

# Example
if __name__ == "__main__":
    agent = DevDollzAgent("Monitor")
    result = agent.perform_task("Check system health")
    print(result)
