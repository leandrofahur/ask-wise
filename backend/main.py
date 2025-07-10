from fastapi import APIRouter, FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

app = FastAPI(title="ASK WISE API", version="0.1.0")

fsm_data = None

router = APIRouter(prefix="/api/v1")


@router.post("/fsm")
async def set_fsm(request: Request):
    global fsm_data
    fsm_data = await request.json()
    return {"status": "ok"}


@router.get("/fsm")
async def get_fsm():
    if fsm_data is not None:
        return fsm_data
    return JSONResponse({"error": "No FSM defined yet"}, status_code=404)


@router.get("/")
async def root():
    return {"message": "ASK WISE API is running!"}


@router.get("/health")
async def health_check():
    return {"status": "healthy"}


app.include_router(router)

# Allow CORS for local frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
