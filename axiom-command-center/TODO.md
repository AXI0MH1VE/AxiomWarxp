# AxiomHive Command Center Development Plan

## Information Gathered
- Existing package.json with Tauri 2.0, React, react-markdown, TypeScript setup
- Sidebar.tsx updated with 6 sections: mission, engine, doctrine, ops, audit, settings
- MissionControl.tsx has hardcoded content, needs to load STRATEGY.md dynamically
- Need to create src-tauri/ with tauri.conf.json, Cargo.toml, src/main.rs for Rust backend commands
- Commands: start_kernel, run_constellation_test, run_abmv, validate_schema, read_file for md
- Components to create: DoctrineLedger, EngineRoom, OperationsCenter, IntegrityAudit, SystemSettings
- App.tsx needs routing for sections
- Files to load: AxiomHive/STRATEGY.md, AxiomHive/PRINCIPLES.md
- Schema: VALIDATION/schemas/strategy_schema.json for validation

## Plan
1. Create src-tauri/tauri.conf.json with allowlist for shell.execute and fs
2. Create src-tauri/Cargo.toml with Tauri 2.0 dependencies
3. Create src-tauri/src/main.rs with invoke handlers for commands
4. Update MissionControl.tsx to use invoke to read STRATEGY.md
5. Create src/components/doctrine/DoctrineLedger.tsx to read PRINCIPLES.md
6. Create src/components/engine/EngineRoom.tsx with buttons for start_kernel, run_constellation_test, run_abmv
7. Create src/components/ops/OperationsCenter.tsx with deploy and rollback
8. Create src/components/audit/IntegrityAudit.tsx with validate_schema and hardcoded attestation
9. Create src/components/settings/SystemSettings.tsx (placeholder)
10. Update App.tsx to handle section switching

## Dependent Files
- All components depend on App.tsx for state
- Rust commands depend on main.rs
- File reading depends on fs allowlist in tauri.conf.json

## Followup Steps
- Run npm run tauri dev to test the app
- Verify UI rendering, navigation, md loading, button invokes, command outputs
- Test all sections and interactions
