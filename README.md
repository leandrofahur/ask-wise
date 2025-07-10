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
make help               # Show all available commands
make install            # Install dependencies
make test               # Run all tests
make lint               # Run linting checks
make format             # Format code with Black
make coverage           # Run tests with coverage
make ci                 # Run complete CI pipeline
make clean              # Clean generated files

# Server commands
make server-install     # Install server dependencies
make server             # Start backend API server

# Clien commands
# Frontend (Next.js)
make client-install     # Install frontend dependencies (pnpm)
make client             # Start frontend dev server (Next.js)
```

---

## **1. Backend: FastAPI on Railway**

### **A. Prepare Your Backend for Railway**
1. **Ensure you have a `requirements.txt`** in `backend/`:
   ```sh
   cd backend
   pip freeze > requirements.txt
   ```
2. **Add a `Procfile`** in `backend/`:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
3. **(Optional) Add a `pyproject.toml`** if not present (for uvicorn, fastapi, etc.)

### **B. Deploy to Railway**
1. Go to [Railway](https://railway.app/) and sign in.
2. Click **New Project** → **Deploy from GitHub repo**.
3. Select your repo and set the root directory to `backend/`.
4. Railway will auto-detect Python and install from `requirements.txt`.
5. Set the **Start Command** to:
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
6. Deploy!  
   - Note your backend URL (e.g., `https://your-backend.up.railway.app`).

---

## **2. Frontend: Next.js on Vercel**

### **A. Prepare Your Frontend**
1. In `frontend/`, create a `.env` file:
   ```
   NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app/api/v1
   ```
2. In your frontend code, use `process.env.NEXT_PUBLIC_API_URL` for all API calls.

### **B. Deploy to Vercel**
1. Go to [Vercel](https://vercel.com/) and sign in.
2. Click **New Project** → **Import GitHub Repo**.
3. Set the project root to `frontend/`.
4. In Vercel dashboard, add the environment variable:
   - `NEXT_PUBLIC_API_URL=https://your-backend.up.railway.app/api/v1`
5. Deploy!

---

## **3. Update Your Frontend API Calls**

In your frontend API utility (e.g., `frontend/lib/api.ts`):

```ts
const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000/api/v1";

export async function getFSM() {
  const res = await fetch(`${API_URL}/fsm`);
  if (!res.ok) throw new Error("Failed to fetch FSM");
  return res.json();
}

export async function postFSM(fsm: any) {
  const res = await fetch(`${API_URL}/fsm`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(fsm),
  });
  if (!res.ok) throw new Error("Failed to post FSM");
  return res.json();
}
```

---

## **4. CORS on Backend**

Your backend CORS should allow your Vercel domain:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://your-vercel-app.vercel.app",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## **5. Test the Full Flow**

- Deploy backend to Railway, get the public URL.
- Deploy frontend to Vercel, set the backend URL as an env var.
- Open your Vercel app and create/view FSMs!

---

## **Would you like:**
- Example `requirements.txt` and `Procfile`?
- Example `.env` and API utility for frontend?
- Help with custom domain or HTTPS?

Let me know if you want the exact files or have any issues during deployment!