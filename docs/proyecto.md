# 📋 Movilidad México — Documentación del Proyecto

> Plataforma comunitaria para monitorear el Tren Suburbano en tiempo real.  
> Proyecto en desarrollo activo. Última actualización: Junio 2026.

---

## 🔖 Versión Actual

**v0.1.0** — API base funcional con endpoints de líneas y estaciones.

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
| Git | - | Control de versiones |
| GitHub | - | Repositorio remoto |
| VS Code | - | Editor de código |

### Base de datos (planeada)
| Tecnología | Uso |
|-----------|-----|
| PostgreSQL | Almacenamiento principal en producción |
| SQLite | Desarrollo local (temporal) |

### Frontend (fase futura)
| Tecnología | Uso |
|-----------|-----|
| Kotlin | Aplicación Android nativa |

---

## 🏛️ Arquitectura

```
Cliente Android (futuro)
         │
         ▼
    [ FastAPI ]
         │
         ▼
  [ PostgreSQL ]
```

**Descripción:**
- El cliente Android consumirá la API REST de FastAPI via HTTP.
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
Lista las estaciones registradas.
> ⚠️ Pendiente: agregar estaciones reales con coordenadas GPS.

---

## 🗺️ Roadmap

### ✅ Fase 0 — Fundamentos (Completado)
- [x] Repositorio Git local creado
- [x] Primer commit realizado
- [x] FastAPI corriendo con Uvicorn
- [x] Endpoint `GET /` funcionando
- [x] Endpoint `GET /lineas` funcionando
- [x] Endpoint `GET /estaciones` funcionando

### 🔄 Fase 1 — Estabilización (En progreso)
- [ ] Crear `.gitignore`
- [ ] Crear repositorio en GitHub
- [ ] Subir código al repositorio remoto
- [ ] Agregar estaciones reales con coordenadas GPS
- [ ] Crear `docs/proyecto.md` en el repositorio ← *este archivo*

### 🔜 Fase 2 — Reportes
- [ ] Diseñar modelo de datos para reportes
- [ ] Integrar SQLite para desarrollo local
- [ ] Crear endpoint `POST /reportes`
- [ ] Crear endpoint `GET /reportes`
- [ ] Validación básica de datos (estación válida, timestamp, dirección)

### 🔜 Fase 3 — Base de Datos Real
- [ ] Migrar de SQLite a PostgreSQL
- [ ] Definir esquema de tablas (líneas, estaciones, reportes)
- [ ] Integrar con SQLAlchemy o Tortoise ORM

### 🔜 Fase 4 — Validación Comunitaria
- [ ] Sistema de confirmación/rechazo de reportes
- [ ] Lógica de validación por GPS
- [ ] TTL (tiempo de vida) de reportes activos

### 🔜 Fase 5 — Frontend Android
- [ ] App Android nativa en Kotlin
- [ ] Mapa interactivo de estaciones
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
| Kotlin para Android | React Native / Flutter | App nativa, mejor rendimiento y acceso a GPS |

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

---

*Documentación mantenida por el equipo de desarrollo de Movilidad México.*
