import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import health, glue, athena, dashboard, copilot

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("medical_ops_backend")

app = FastAPI(
    title="Medical Operations Intelligence & Automation Command System API",
    version="4.2.0",
    description="Production-grade Backend REST API connecting React Frontend to AWS Glue, Athena, S3 & Bedrock"
)

# Enable CORS for React Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routers
app.include_router(health.router)
app.include_router(dashboard.router)
app.include_router(glue.router)
app.include_router(athena.router)
app.include_router(copilot.router)

@app.get("/")
def root():
    return {
        "title": "Medical Operations Intelligence Command System API",
        "status": "online",
        "docs": "/docs",
        "health": "/api/health"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
