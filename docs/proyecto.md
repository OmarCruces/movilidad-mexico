# 📋 Movilidad México — Documentación del Proyecto

> Plataforma comunitaria para monitorear el Tren Suburbano en tiempo real.  
> Proyecto en desarrollo activo. Última actualización: Junio 2026.

---

## 🔖 Versión Actual

**v0.3.x** — API funcional con catálogo completo de estaciones, filtrado por línea y sistema de reportes con validación.

---

## 🧭 Visión General

**Movilidad México** es una API backend que permite a los usuarios reportar y consultar el estado del Tren Suburbano de la ZMVM en tiempo real, mediante reportes validados por la comunidad.

---

## 👥 Equipo

| Rol | Nombre |
|-----|--------|
| Founder & Desarrollador | Omar Cruces |
| Arquitectura, Backend & Mentor técnico | ChatGPT |
| Documentación & Revisión técnica | Claude |

**Repositorio:** https://github.com/OmarCruces

---

## 🎯 Objetivos

- Crear una plataforma comunitaria para monitorear el Tren Suburbano en tiempo real.
- Permitir que los usuarios reporten el paso de trenes desde su ubicación.
- Ofrecer información útil y accesible para los miles de usuarios diarios del Suburbano.

---

## 🚆 Alcance Inicial

**Líneas cubiertas:**
- Línea 1: Buenavista ↔ Cuautitlán
- Línea 2: Buenavista ↔ AIFA

**Fuera de alcance (por ahora):**
- Otros sistemas de transporte (Metro, Metrobús, Mexibús, etc.)
- Notificaciones push
- Autenticación de usuarios

---

## 🛠️ Stack Tecnológico

### Backend (fase actual)
| Tecnología | Versión | Uso |
|-----------|---------|-----|
| Python | 3.14 | Lenguaje principal |
| FastAPI | Latest | Framework API REST |
| Uvicorn | Latest | Servidor ASGI |
| Pydantic | Latest | Validación de datos y modelos |
| Git | - | Control de versiones |
| GitHub | - | Repositorio remoto |
| VS Code | - | Editor de código |

### Planeadas para futuras versiones
| Tecnología | Uso |
|-----------|-----|
| SQLAlchemy | ORM para PostgreSQL |
| Docker | Contenerización |

### Base de datos (planeada)
| Tecnología | Uso |
|-----------|-----|
| PostgreSQL | Almacenamiento principal en producción |
| SQLite | Desarrollo local (temporal) |

### Frontend (fase futura)
| Tecnología | Uso |
|-----------|-----|
| Por definir (HTML/CSS/JS o framework web) | Página web interactiva con mapa, similar a amigosuburbano.com |

---

## 🏛️ Arquitectura

```
Cliente Web (futuro)
         │
         ▼
    [ FastAPI ]
         │
         ▼
  [ PostgreSQL ]
```

**Descripción:**
- El cliente web (página interactiva con mapa) consumirá la API REST de FastAPI vía HTTP.
- FastAPI gestiona la lógica de negocio y validación de reportes.
- PostgreSQL almacena líneas, estaciones y reportes de usuarios.
- En desarrollo local se usa SQLite en lugar de PostgreSQL.

---

## 📡 Endpoints Actuales

### `GET /`
Verificación de salud del servicio.
```json
{
  "status": "ok",
  "service": "Movilidad México"
}
```

### `GET /lineas`
Lista las líneas del Tren Suburbano disponibles.
```json
[
  { "id": 1, "nombre": "Buenavista - Cuautitlán" },
  { "id": 2, "nombre": "Buenavista - AIFA" }
]
```

### `GET /estaciones`
Lista todas las estaciones registradas.

**Línea 1:** Buenavista · Fortuna · Tlalnepantla · San Rafael · Lechería · Tultitlán · Cuautitlán
**Línea 2 (AIFA):** Cueyamil · La Loma · Teyahualco · Prados Sur · Cajiga · Xaltocan · AIFA

> ⚠️ Pendiente: agregar coordenadas GPS reales a cada estación.

### `GET /estaciones/{linea_id}`
Filtra estaciones por línea específica.
```
GET /estaciones/1   → Estaciones de Buenavista-Cuautitlán
GET /estaciones/2   → Estaciones de Cueyamil-AIFA
```

### `POST /reportes`
Crea un nuevo reporte de paso de tren. Valida que `estacion_id` exista en el catálogo antes de aceptarlo.

**Modelo (Pydantic):**
```python
class Reporte(BaseModel):
    estacion_id: int
    direccion: str
    mensaje: str
    usuario: str
```

**Ejemplo de petición:**
```json
{
  "estacion_id": 10,
  "direccion": "AIFA",
  "mensaje": "Tren saliendo de Teyahualco",
  "usuario": "Omar"
}
```

### `GET /reportes`
Consulta todos los reportes almacenados (actualmente en memoria, sin persistencia en BD todavía).

---

## 🧪 Pruebas

Todos los endpoints se prueban vía Swagger/OpenAPI en `http://127.0.0.1:8000/docs`.

| Prueba | Estado |
|--------|--------|
| Consulta de líneas | ✅ |
| Consulta de estaciones | ✅ |
| Filtrado por línea | ✅ |
| Creación de reportes | ✅ |
| Consulta de reportes | ✅ |
| Validación de estación inexistente | ✅ |

---

## 🗺️ Roadmap

### ✅ Fase 0 — Fundamentos (Completado)
- [x] Repositorio Git local creado
- [x] Primer commit realizado
- [x] FastAPI corriendo con Uvicorn
- [x] Endpoint `GET /` funcionando
- [x] Endpoint `GET /lineas` funcionando
- [x] Endpoint `GET /estaciones` funcionando

### ✅ Fase 1 — Estabilización (Completado)
- [x] Crear `.gitignore`
- [x] Crear repositorio en GitHub
- [x] Subir código al repositorio remoto
- [x] Crear `docs/proyecto.md`, `docs/analisis.md`, `docs/uml.md`
- [ ] Agregar coordenadas GPS reales a las estaciones

### 🔄 Fase 2 — Reportes (En progreso)
- [x] Diseñar modelo de datos para reportes (Pydantic)
- [x] Crear endpoint `POST /reportes`
- [x] Crear endpoint `GET /reportes`
- [x] Endpoint `GET /estaciones/{linea_id}` (filtrado por línea)
- [x] Validación: rechazar reportes de estaciones inexistentes
- [ ] Agregar fecha y hora automática a cada reporte
- [ ] Crear endpoint `GET /reportes/{estacion_id}`
- [ ] Validar dirección del tren
- [ ] Agregar identificador único (UUID) a reportes
- [ ] Integrar SQLite para desarrollo local (persistencia actual: en memoria)

### 🔜 Fase 3 — Base de Datos Real
- [ ] Migrar de almacenamiento en memoria a PostgreSQL
- [ ] Definir esquema de tablas (líneas, estaciones, reportes)
- [ ] Integrar con SQLAlchemy

### 🔜 Fase 4 — Validación Comunitaria
- [ ] Sistema de confirmación/rechazo de reportes
- [ ] Lógica de validación por GPS
- [ ] TTL (tiempo de vida) de reportes activos
- [ ] Geolocalización de estaciones
- [ ] Estadísticas de tráfico ferroviario

### 🔜 Fase 5 — Frontend Web
- [ ] Página web interactiva con mapa de estaciones (estilo amigosuburbano.com)
- [ ] Reportar paso de tren tocando la estación en el mapa
- [ ] Consumo de la API REST

---

## 🏗️ Estructura del Proyecto

```
movilidad-mexico/
├── main.py               # Punto de entrada FastAPI
├── routers/              # Endpoints organizados por módulo
│   ├── lineas.py
│   ├── estaciones.py
│   └── reportes.py       # (próximamente)
├── models/               # Modelos de datos
├── database/             # Configuración de BD
├── docs/
│   └── proyecto.md       # Este archivo
├── .gitignore
├── requirements.txt
└── README.md
```

> ⚠️ Esta estructura es una propuesta. Actualizar conforme evolucione el proyecto.

---

## 📐 Decisiones Técnicas

| Decisión | Alternativa considerada | Razón |
|---------|------------------------|-------|
| FastAPI sobre Flask | Flask | FastAPI es más moderno, async nativo y genera docs automáticas |
| PostgreSQL en producción | MySQL | Mejor soporte para datos geoespaciales (coordenadas GPS) |
| SQLite en desarrollo | PostgreSQL local | Sin configuración, ideal para avanzar rápido |
| Frontend web (no app móvil) | App Android nativa | Mayor alcance sin instalación, más rápido de iterar, referencia directa: amigosuburbano.com |

---

## 📝 Notas del Equipo

- Este proyecto es **no oficial** y no tiene relación con el operador del Tren Suburbano.
- La confiabilidad del sistema depende de la participación activa de la comunidad.
- Priorizar simplicidad en las primeras fases antes de optimizar.

---

## 📅 Historial de Cambios

### v0.1.0 — 2026-06-08
- Proyecto iniciado.
- FastAPI instalado y configurado con Uvicorn.
- Repositorio Git local creado, primer commit realizado.
- Endpoint `GET /` implementado.
- Endpoint `GET /lineas` implementado.
- Endpoint `GET /estaciones` implementado.
- Documentación inicial `docs/proyecto.md` creada.

### v0.2.0 — 2026-06-08/09
- `.gitignore` corregido (renombrado correctamente con el punto).
- Repositorio conectado a GitHub (`git remote add origin`).
- Rama renombrada de `master` a `main`.
- Primer push exitoso a GitHub.
- `README.md` profesional agregado (Claude).
- `docs/analisis.md` creado: requerimientos, casos de uso, historias de usuario, modelo de datos.
- `docs/uml.md` creado: 7 diagramas Mermaid (casos de uso, clases, secuencia, ER, componentes, actividad).

### v0.3.x — 2026-06-19
- Catálogo de estaciones corregido y completado para Línea 1 y Línea AIFA.
- Estaciones movidas a variable global reutilizable (`estaciones = []`).
- Endpoint `GET /estaciones/{linea_id}` implementado (filtrado por línea).
- Modelo `Reporte` creado con Pydantic.
- Endpoint `POST /reportes` implementado.
- Endpoint `GET /reportes` implementado (almacenamiento en memoria por ahora).
- Validación agregada: rechaza reportes con `estacion_id` inexistente.
- Pruebas funcionales completas vía Swagger/OpenAPI.
- Errores resueltos: comando `uvicorn` no reconocido (solución: activar entorno virtual y usar `python -m uvicorn`), error 422 por JSON mal formado en pruebas.
- Commit `cd1deb7`: "feat: validar existencia de estaciones en reportes" — subido a GitHub.

---

*Documentación mantenida por el equipo de desarrollo de Movilidad México.*
