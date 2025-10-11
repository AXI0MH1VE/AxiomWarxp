class MonitoringAgent:
    def monitor(self) -> str:
        return "System healthy"

if __name__ == "__main__":
    agent = MonitoringAgent()
    print(agent.monitor())
