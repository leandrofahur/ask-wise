# AskWise - FSM Tutor Mode

[![codecov](https://codecov.io/gh/leandrofahur/ask-wise/branch/main/graph/badge.svg?token=YR9K32XX5X)](https://codecov.io/gh/leandrofahur/ask-wise?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Project Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/leandrofahur/ask-wise/releases)


> A modular, extensible, and class-based Deterministic Finite State Machine library for Python.

## Motivation
Create a Deterministic Finite State Machines (DFSMs) easy to extesion and will serve as the API for our FE.

## Architecture
🚧

## Features
🚧

## Getting started
### Installing Python Venvs
The Python packages are managed using the [uv](https://github.com/astral-sh/uv) package manager, In order to install it, you can follow the [installation guide](https://docs.astral.sh/uv/#getting-started). For Mac users, as of 22 Oct 2024 enter the following in your terminal:

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

Once `uv` is installed and available in your terminal you can navigate to the course root directory and execute:

```bash
$ uv python install 3.12.7
$ uv venv --python 3.12.7
$ uv sync
```

> If the `uv` command is not recognized, try restarting your terminal.

With that we have our chapter venv installed. When working through the code for a specific chapter, always create a new venv to avoid dependency hell.



### Git Branching Strategy
Please, follow these branch naming and usage conventions in order to keep the repository maintainable and collaborative:

|Branch|	Purpose|
|------|-----------|
|main  |	Stable production-ready code|
|dev   | Ongoing development, always deployable|

All work should be merged into `dev`, and only thoroughly tested code gets merged into `main`.

| Prefix     | Used For               | Branches Off | Example                             |
|------------|------------------------|--------------|-------------------------------------|
| feature/   | New functionality      | `dev`        | `feature/fsm-diff-visualization`    |
| bugfix/    | Bug resolution         | `dev`        | `bugfix/fix-missing-transition`     |
| hotfix/    | Urgent production fix  | `main`       | `hotfix/fix-runtime-error`          |
| release/   | Production releases    | `dev`        | `release/v0.2.0`                    |
| test/      | Experimental testing   | `dev`        | `test/mutation-graph-export`        |
| doc/       | Documentation updates  | `dev`        | `doc/add-readme-branch-strategy`    |

In order to create a branch out of `dev`, for example, you should do the following:

```bash
$ git checkout dev
$ git checkout -b <branch_prefix>/<functionality>
```



### Git Flow Process

1. **Start New Work**
```bash
$ git checkout dev
$ git checkout -b feat/my-new-feature
```

2. **Push & Open PR**
- Push your branch:

```bash
$ git push origin feat/my-new-feature
```

- Open a Pull Request into `dev`.
- Get at least 1 approval before merging.

3. **Merging**
- Only maintainers merge into main (via `dev`).
- Use squash merge unless otherwise needed.

4. **Release to Production**

```bash
$ git checkout main
$ git merge dev
$ git tag vX.X.X
$ git push origin main --tags
```

### Example Workflow
```bash
# Start working on a feature
git checkout dev
git checkout -b feature/ai-tutor-endpoint

# Make changes
git add .
git commit -m "feature(api): add initial AI tutor endpoint"
git push origin feature/ai-tutor-endpoint

# Open PR → review → merge into dev
```



### Run Linting and Formatting
```bash
# From repository root (recommended)
make help          # Show all available commands
make install       # Install dependencies
make test          # Run all tests
make lint          # Run linting checks
make format        # Format code with Black
make coverage      # Run tests with coverage
make ci            # Run complete CI pipeline
make clean         # Clean generated files

# Or from backend directory
cd backend
make test
make lint
make format
make coverage
make ci
```