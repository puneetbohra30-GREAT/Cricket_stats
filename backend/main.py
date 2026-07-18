from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import time

# IMPORTS
from api import auth, chat, cricket, external, insights, knowledge, user
from database.db import Base, engine
from config import settings


# ================================
# STARTUP / SHUTDOWN
# ================================
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting Cricket AI Backend...")

    # Create DB tables
    Base.metadata.create_all(bind=engine)

    yield

    print("🛑 Server Stopped")


# ================================
# APP INIT
# ================================
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    debug=settings.DEBUG,
    lifespan=lifespan
)


# ================================
# REQUEST LOGGER
# ================================
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    duration = round(time.time() - start_time, 3)
    print(f"{request.method} {request.url.path} - {response.status_code} - {duration}s")

    return response


# ================================
# CORS
# ================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # ⚠️ production में specific domain डालना
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ================================
# BASIC ROUTES
# ================================
@app.get("/")
def home():
    return {"message": "🏏 Cricket AI Backend Running"}


@app.get("/health")
def health():
    return {"status": "ok"}


# ================================
# ROUTES
# ================================

# ✅ AUTH → /auth/*
app.include_router(auth.router, prefix="/auth", tags=["Auth"])

# ✅ CRICKET → /cricket/*
# ⚠️ cricket.py में prefix नहीं होना चाहिए
app.include_router(cricket.router, prefix="/cricket", tags=["Cricket"])

# ✅ USER → /user/*
app.include_router(user.router, prefix="/user", tags=["User"])

# ✅ CHAT → /chat/*
app.include_router(chat.router, prefix="/chat", tags=["Chat"])

# OPTIONAL MODULES
if settings.ENABLE_INSIGHTS:
    app.include_router(insights.router, prefix="/insights", tags=["Insights"])

if settings.ENABLE_KNOWLEDGE:
    app.include_router(knowledge.router, prefix="/knowledge", tags=["Knowledge"])

if settings.ENABLE_EXTERNAL:
    app.include_router(external.router, prefix="/external", tags=["External"])


# ================================
# DEBUG ROUTE
# ================================
@app.get("/routes")
def list_routes():
    return [{"path": r.path, "name": r.name} for r in app.routes]
