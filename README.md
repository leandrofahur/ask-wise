# AskWise - FSM Assistant with LangChain & FastAPI

[![codecov](https://codecov.io/gh/leandrofahur/ask-wise/branch/main/graph/badge.svg?token=YR9K32XX5X)](https://codecov.io/gh/leandrofahur/ask-wise?branch=main)
[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/downloads/)
[![Project Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/leandrofahur/ask-wise/releases)


> A modular, extensible, and class-based Deterministic Finite State Machine (DFSM) platform, now integrated with LangChain to support intelligent retrieval from your custom PDFs for theory explanation and control examples.


## Motivation
AskWise combines finite state machine simulation with retrieval-augmented AI using LangChain. It serves as an educational and development tool for anyone working with control systems, robotics, AI agents, and system modeling.

### Key Use Cases:

- Visualize and simulate FSMs via a fullstack interface.
- Chat with an FSM-Aware AI Assistant trained on your own PDFs.
- Extend the backend to include FSM transitions based on user interaction or AI state classification.


## Architecture
```bash
ask-wise/
├── backend/                   # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   ├── api/               # REST endpoints
│   │   ├── fsm/               # FSM engine logic
│   │   ├── rag/               # LangChain PDF ingestion + chat
│   │   └── core/              # Configs, logging
│   ├── tests/                 # Pytest-based test suite
│   ├── Makefile               # Dev CLI commands
│   └── pyproject.toml
├── frontend/ (coming soon)    # Next.js FSM visualizer
└── README.md
```


## Features
|Fature                        | Description                                                   |
|------------------------------|---------------------------------------------------------------|
| FSM Engine                   | Python-based, test-covered deterministic state machine engine |
| FSM Visualizer               | Frontend (Next.js) renders Mermaid graphs from API            |
| LanChain RAG                 | Upload a control theory PDF and ask context-aware questions   |
| Test Coverage                | Fully tested with pytest, httpx, and CI workflows             |
| Developer tools              | Uses uv, Makefile automation, black, ruff, and coverage       |
| Docker ready                 | Runs via Docker Compose for full local simulation stack       |



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

|Branch   | Purpose                                |
|---------|----------------------------------------|
| `main`  | Stable production-ready code           |
| `dev`   | Ongoing development, always deployable |

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