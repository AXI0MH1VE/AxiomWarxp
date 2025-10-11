from typing import List, Optional

class AxiomaticLogicEngine:
    def __init__(self):
        self.axioms: List[str] = []

    def add_axiom(self, axiom: str):
        self.axioms.append(axiom)

    def derive(self, premise: str) -> Optional[str]:
        # Simple derivation logic
        for axiom in self.axioms:
            if premise in axiom:
                return axiom
        return None

# Example usage
if __name__ == "__main__":
    engine = AxiomaticLogicEngine()
    engine.add_axiom("All men are mortal")
    result = engine.derive("Socrates is a man")
    print(result)
