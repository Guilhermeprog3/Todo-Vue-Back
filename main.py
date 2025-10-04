from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import models
from database import engine
from routers import auth, tasks

models.Base.metadata.create_all(bind=engine)

description = """
API para gerenciar uma lista de tarefas (To-Do List). 🚀

Desenvolvido por **Guilherme Silva Rios**.
[Visite meu portfólio](https://guilhermeriosdev.vercel.app)
"""

app = FastAPI(
    title="To-Do List API",
    description=description,
    version="1.0.0",
    contact={
        "name": "Guilherme Silva Rios",
        "url": "https://guilhermeriosdev.vercel.app",
    },
)


origins = [
    "http://localhost:5173",
    "http://localhost:8080",
    "https://todo-vue-front-end.vercel.app"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API da To-Do List!"}