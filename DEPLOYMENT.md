# DEPLOYMENT.md

## Operational Playbook for AxiomHive Genesis Refractor vΩ.1

### Prerequisites
- Python 3.8+
- Rust 1.70+
- Git
- Docker (optional for containerized deployment)

### Build Commands
```bash
# Build all components
python build.py

# Build Rust components only
cd AgentMatrix && cargo build --release

# Build Python components
python -m compileall . -q
```

### Deployment Steps
1. **Genesis Boot**: Run `python ARTIFACTS/genesis_refractor.py` to verify BOOT_STATE.
2. **Ledger Initialization**: Load `ARTIFACTS/adag_config.json` and initialize A-DAG.
3. **Artifact Deployment**: Deploy generated artifacts to sovereign infrastructure.
4. **Audit Verification**: Run validation against `ARTIFACTS/ledger_schema.json`.

### Environment Setup
- Set `AXIOMHIVE_SOVEREIGN=true` to enable full sovereignty mode.
- Mount ledger at `/var/axiomhive/ledger` for persistence.
- Configure entropy monitoring with threshold `1e-11 nats`.

### Rollback Procedures
- On entropy spike >1e-11: `python genesis_refractor.py --rollback`
- Kernel panic: Automatic reset to genesis state.
- Manual rollback: `git reset --hard GENESIS_COMMIT`

### Cost Considerations
- Minimal dependencies reduce deployment costs.
- Stateless design enables serverless deployment.
- Sovereign operation eliminates platform fees.

### Latency Considerations
- A-DAG validation: <1ms per node.
- Artifact generation: <100ms for typical outputs.
- Equilibrium check: O(n) where n = ledger size.