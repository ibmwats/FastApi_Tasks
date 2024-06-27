from fastapi import FastAPI
from app.api.endpoints import general, equipment
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Подключение роутеров
app.include_router(general.router, prefix="/general", tags=["General"])
app.include_router(equipment.router, prefix="/equipment", tags=["Equipment"])

# Статические файлы и шаблоны
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI project!"}
