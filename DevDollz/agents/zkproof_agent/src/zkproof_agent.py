class ZKProofAgent:
    def generate_proof(self, data: str) -> str:
        return f"ZK proof for: {data}"

if __name__ == "__main__":
    agent = ZKProofAgent()
    print(agent.generate_proof("transaction"))
