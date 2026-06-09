# 🚆 Movilidad México

> Plataforma comunitaria para monitorear el Tren Suburbano de la ZMVM en tiempo real.

![Estado](https://img.shields.io/badge/estado-en%20desarrollo-yellow)
![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![Licencia](https://img.shields.io/badge/licencia-MIT-lightgrey)

---

## 📖 ¿Qué es Movilidad México?

**Movilidad México** es una API REST que permite a los usuarios reportar y consultar el estado del Tren Suburbano en tiempo real, mediante reportes validados por la comunidad — similar a Waze, pero para el tren.

---

## 🚆 Líneas cubiertas

| Línea | Ruta |
|-------|------|
| Línea 1 | Buenavista ↔ Cuautitlán |
| Línea 2 | Buenavista ↔ AIFA |

---

## 🛠️ Tecnologías

- **Python 3.14**
- **FastAPI** — Framework API REST
- **Uvicorn** — Servidor ASGI
- **PostgreSQL** — Base de datos *(próximamente)*
- **Kotlin** — App Android nativa *(fase futura)*

---

## 🚀 Instalación y uso

### 1. Clona el repositorio

```bash
git clone https://github.com/OmarCruces/movilidad-mexico.git
cd movilidad-mexico
```

### 2. Crea un entorno virtual

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta el servidor

```bash
uvicorn backend.main:app --reload
```

### 5. Abre la documentación interactiva

```
http://127.0.0.1:8000/docs
```

---

## 📡 Endpoints disponibles

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Estado del servicio |
| `GET` | `/lineas` | Lista de líneas del Suburbano |
| `GET` | `/estaciones` | Lista de estaciones |
| `POST` | `/reportes` | Crear reporte *(próximamente)* |
| `GET` | `/reportes` | Consultar reportes *(próximamente)* |

---

## 🗺️ Roadmap

- [x] API base con FastAPI
- [x] Endpoints de líneas y estaciones
- [x] Repositorio en GitHub
- [x] Documentación inicial
- [ ] Estaciones reales con coordenadas GPS
- [ ] Endpoint de reportes
- [ ] Integración con PostgreSQL
- [ ] Validación comunitaria de reportes
- [ ] App Android nativa en Kotlin

---

## 👥 Equipo

| Rol | Nombre |
|-----|--------|
| Founder & Desarrollador | Omar Cruces |
| Arquitectura & Backend | ChatGPT |
| Documentación & Revisión técnica | Claude |

---

## ⚠️ Aviso

Este proyecto es **no oficial** y no tiene relación con el operador del Tren Suburbano ni con ninguna entidad gubernamental. Es un proyecto comunitario de código abierto.

---

## 📄 Licencia

MIT © 2026 Omar Cruces
