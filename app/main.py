from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.PessoaController import router as pessoa_router
from app.controllers.BlocoController import router as bloco_router
from app.database.database import engine, Base
import app.models

app = FastAPI(
    title="LensFlow ERP - Ótica",
    version="1.0.0",
    description="API backend do ERP LensFlow"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # depois restringe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(pessoa_router)
app.include_router(bloco_router)

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)