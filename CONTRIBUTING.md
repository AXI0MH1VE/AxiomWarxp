# Contributing to AxiomWarxp

Thank you for your interest in contributing to AxiomWarxp! This document outlines the guidelines and processes for contributing to this sovereign AI platform.

## Code of Conduct

All contributors must adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you agree to maintain a respectful and professional environment.

## Sovereignty Principles

All contributions must align with AxiomWarxp's core sovereignty principles:

### 1. Determinism
- All code must produce deterministic outputs
- No random number generation without explicit seeding
- Functions must be pure where possible

### 2. Traceability
- Every change must be linked to an explicit intent
- A-DAG ledger entries must be maintained
- GitHub synchronization must be preserved

### 3. Minimal Dependencies
- No external API dependencies without explicit approval
- Prefer self-contained implementations
- External libraries must be thoroughly vetted

### 4. Metamorphic Architecture
- Contributions should enable or enhance self-evolution
- Architecture improvements are highly valued
- Entropy reduction is a key metric

## Development Workflow

### 1. Issue Creation
- Create an issue before starting work (except for trivial fixes)
- Use appropriate issue templates
- Clearly describe the problem and proposed solution

### 2. Branching Strategy
```bash
# Create feature branch
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b bugfix/issue-number-description
```

### 3. Development Standards
- Follow existing code style and conventions
- Add comprehensive tests for new functionality
- Update documentation as needed
- Ensure sovereignty compliance

### 4. Commit Guidelines
- Use conventional commit format: `type(scope): description`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- Keep commits atomic and focused

### 5. Testing
- Run full test suite: `python build.py`
- Ensure genesis refractor validation passes
- Test in isolated environment if possible

### 6. Pull Request
- Use the PR template
- Provide clear description of changes
- Reference related issues
- Request review from maintainers

## Component-Specific Guidelines

### AxiomHive Genesis Refractor
- Changes must maintain A-DAG integrity
- Entropy calculations must be preserved
- GitHub sync must remain functional

### DevDollz Agents
- Agents must implement self-correction loops
- Kernel panic recovery must be maintained
- Inter-agent communication must be secure

### TranscendentAI Modules
- Ethical boundaries must be respected
- Safety guardians must be updated for new capabilities
- Performance benchmarks must be maintained

### Agent Matrix (Rust)
- Memory safety must be guaranteed
- Performance must not degrade
- FFI boundaries must be secure

### User Interfaces
- Accessibility standards must be maintained
- Security best practices must be followed
- Performance must be optimized

## Review Process

### Automated Checks
- CI/CD pipeline must pass
- Security scanning must clear
- Code coverage must be maintained

### Manual Review
- At least one maintainer must approve
- Sovereignty compliance must be verified
- Architecture impact must be assessed

### Merge Requirements
- All automated checks pass
- Manual review completed
- No sovereignty violations
- Documentation updated

## Getting Help

- **Documentation**: Check component-specific READMEs
- **Issues**: Search existing issues before creating new ones
- **Discussions**: Use GitHub Discussions for questions
- **Contact**: Reach out to maintainers for guidance

## Recognition

Contributors will be recognized in:
- Release notes
- Contributors file
- A-DAG ledger entries
- Sovereign merit system

Thank you for contributing to the future of sovereign AI!