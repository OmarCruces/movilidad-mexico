from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="Movilidad México",
    version="0.3.0"
)

class Reporte(BaseModel):
    estacion_id: int
    direccion: str
    mensaje: str
    usuario: str

estaciones = [
    {"id": 1, "nombre": "Buenavista", "linea_id": 1},
    {"id": 2, "nombre": "Fortuna", "linea_id": 1},
    {"id": 3, "nombre": "Tlalnepantla", "linea_id": 1},
    {"id": 4, "nombre": "San Rafael", "linea_id": 1},
    {"id": 5, "nombre": "Lechería", "linea_id": 1},
    {"id": 6, "nombre": "Tultitlán", "linea_id": 1},
    {"id": 7, "nombre": "Cuautitlán", "linea_id": 1},
    {"id": 8, "nombre": "Cueyamil", "linea_id": 2},
    {"id": 9, "nombre": "La Loma", "linea_id": 2},
    {"id": 10, "nombre": "Teyahualco", "linea_id": 2},
    {"id": 11, "nombre": "Prados Sur", "linea_id": 2},
    {"id": 12, "nombre": "Cajiga", "linea_id": 2},
    {"id": 13, "nombre": "Xaltocan", "linea_id": 2},
    {"id": 14, "nombre": "AIFA", "linea_id": 2}
]

reportes = []

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
    return estaciones

@app.get("/estaciones/{linea_id}")
def obtener_estaciones_por_linea(linea_id: int):
    resultado = []

    for estacion in estaciones:
        if estacion["linea_id"] == linea_id:
            resultado.append(estacion)

    return resultado

@app.post("/reportes")
def crear_reporte(reporte: Reporte):

    estacion_existe = False

    for estacion in estaciones:
        if estacion["id"] == reporte.estacion_id:
            estacion_existe = True
            break

    if not estacion_existe:
        return {
            "error": "La estación no existe"
        }

    nuevo_reporte = reporte.dict()

    nuevo_reporte["fecha"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    reportes.append(nuevo_reporte)

    return {
        "mensaje": "Reporte recibido",
        "reporte": nuevo_reporte
    }

@app.get("/reportes")
def obtener_reportes():
    return reportes