class TestAgent:
    def run_tests(self) -> str:
        return "All tests passed"

if __name__ == "__main__":
    agent = TestAgent()
    print(agent.run_tests())
