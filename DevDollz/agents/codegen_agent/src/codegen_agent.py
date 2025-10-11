class CodegenAgent:
    def generate_code(self, spec: str) -> str:
        return f"Generated code for: {spec}"

if __name__ == "__main__":
    agent = CodegenAgent()
    print(agent.generate_code("API endpoint"))
