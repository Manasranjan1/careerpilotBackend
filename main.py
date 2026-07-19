from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import analyze, cover_letter

app = FastAPI(title="CareerPilot AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "https://careerpilot-project.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(analyze.router, prefix="/api")
app.include_router(cover_letter.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "CareerPilot AI API is running"}

@app.get("/health")
async def health():
    return {"status": "ok"}
