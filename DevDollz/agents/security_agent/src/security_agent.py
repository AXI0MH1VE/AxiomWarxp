class SecurityAgent:
    def check_security(self) -> str:
        return "Security check passed"

if __name__ == "__main__":
    agent = SecurityAgent()
    print(agent.check_security())
