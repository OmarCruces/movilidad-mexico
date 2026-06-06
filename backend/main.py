from fastapi import FastAPI

app = FastAPI(
    title="Movilidad México",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "Movilidad México"
    }

@app.get("/lineas")
def obtener_lineas():
    return [
        {   
            "id": 1,
            "nombre": "Buenavista - Cuautitlán"
        },
        {
            "id": 2,
            "nombre": "Buenavista - AIFA"
        }
    ]

@app.get("/estaciones")
def obtener_estaciones():
    return [
        {
            "id": 1,
            "nombre": "Buenavista",
            "linea_id": 1
        },
        {
            "id": 2,
            "nombre": "Fortuna",
            "linea_id": 1
        },
        {
            "id": 3,
            "nombre": "Lechería",
            "linea_id": 1
        }
    ]