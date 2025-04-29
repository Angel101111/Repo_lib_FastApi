# main.py

# Importar la clase FastAPI
from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()
app.title = "Mi primera aplicación con FastAPI"
app.version = "1.0.0"

# Lista de películas (simulación de base de datos en memoria)
movies = [
    {
        "id": 1,
        "titulo": "Avatar",
        "descripcion": "Un soldado con el tren inferior paralizado toma la decisión de...",
        "Año": "2009"  
    },
    {
        "id": 2,
        "titulo": "Cars",
        "descripcion": "Un carro parlante sueña con ganar la copa piston",
        "Año": "2000"  
    }
]

# Ruta GET básica para probar la API
@app.get("/Hola", tags=["Home"])
def home():
    return {"message": "¡Hola desde FastAPI en Docker! 🚀"}

# Ruta GET que retorna un json
@app.get("/Movie", tags=["Home"])
def home():
    return movies

# Ruta GET para observar como funcionan los parametros de ruta
@app.get("/Movie/{id}", tags=["Home"])
def home(id:int):
    for movie in movies:
        if movie["id"]==id:
            return movie

