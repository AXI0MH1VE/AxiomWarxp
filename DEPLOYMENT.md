# DEPLOYMENT.md

## Operational Playbook for AxiomHive Genesis Refractor vΩ.2 (Escalation Cascade — Sovereign Audit Runtime)

### Prerequisites
- Python 3.8+
- Rust 1.70+
- Git
- GitHub SSH or HTTPS credentials configured
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
1. **Genesis Boot**: Run `python ARTIFACTS/genesis_refractor.py` to verify BOOT_STATE and GITHUB_AUTH.
2. **GitHub Repository Setup**: Ensure AxiomHive/<artifact> repository exists or auto-create.
3. **Ledger Initialization**: Load `ARTIFACTS/adag_config.json` and initialize A-DAG.
4. **Artifact Deployment**: Deploy generated artifacts to sovereign infrastructure.
5. **GitHub Synchronization**: Auto-commit and push artifacts to repository.
6. **Audit Verification**: Run validation against `ARTIFACTS/ledger_schema.json` and GitHub state.

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