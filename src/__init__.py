from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routers.documents_views import api_router


app = FastAPI(title='Squirro API', version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


app.include_router(api_router, prefix="/documents", tags=["documents"])
