# 📊 Análisis del Sistema — Movilidad México

> Documento de análisis previo al desarrollo de la plataforma.  
> Versión: 1.0 | Fecha: Junio 2026

---

## 1. 📋 Descripción General

**Movilidad México** es una plataforma comunitaria que permite a los pasajeros del Tren Suburbano de la ZMVM reportar y consultar el paso de trenes en tiempo real, mediante interacción directa con un mapa de estaciones.

---

## 2. 🎯 Objetivos del Sistema

| # | Objetivo |
|---|----------|
| 1 | Permitir a los pasajeros conocer el estado actual del Tren Suburbano |
| 2 | Registrar reportes de paso de trenes por estación |
| 3 | Validar reportes mediante confirmación comunitaria |
| 4 | Mostrar información en tiempo real mediante un mapa interactivo |

---

## 3. 👥 Usuarios del Sistema

### Usuario Principal: Pasajero del Suburbano

Persona que utiliza el Tren Suburbano en su rutina diaria y necesita saber si hay trenes circulando en tiempo real.

**Características:**
- Accede al servicio desde cualquier cliente web o móvil
- Está parado en una estación o en camino a ella
- Necesita información rápida y confiable
- Puede reportar el paso de un tren tocando su estación en el mapa

> ⚠️ **Pendiente de definir:** Si el sistema requerirá registro/login o permitirá reportes anónimos. Esta decisión impacta directamente en la arquitectura de autenticación.

---

## 4. 📌 Requerimientos Funcionales

| ID | Requerimiento | Prioridad |
|----|--------------|-----------|
| RF-01 | El sistema debe mostrar un mapa con todas las estaciones del Suburbano | Alta |
| RF-02 | El usuario puede tocar una estación para reportar el paso de un tren | Alta |
| RF-03 | El sistema debe mostrar reportes activos por estación | Alta |
| RF-04 | Los reportes deben tener un tiempo de vida (TTL) limitado | Alta |
| RF-05 | El usuario puede confirmar o rechazar un reporte existente | Media |
| RF-06 | El sistema debe mostrar la línea y dirección del tren reportado | Media |
| RF-07 | El sistema debe registrar timestamp y coordenadas del reporte | Alta |
| RF-08 | El sistema debe diferenciar entre Línea 1 y Línea 2 | Alta |

---

## 5. 📌 Requerimientos No Funcionales

| ID | Requerimiento | Descripción |
|----|--------------|-------------|
| RNF-01 | Disponibilidad | El sistema debe estar disponible 24/7 |
| RNF-02 | Rendimiento | La API debe responder en menos de 500ms |
| RNF-03 | Escalabilidad | Debe soportar múltiples usuarios simultáneos |
| RNF-04 | Seguridad | No exponer datos sensibles en endpoints públicos |
| RNF-05 | Usabilidad | La app debe ser intuitiva y de uso rápido |
| RNF-06 | Portabilidad | Android nativo como plataforma objetivo |

---

## 6. 🧑‍💻 Casos de Uso

### CU-01: Consultar estado de una estación
- **Actor:** Pasajero
- **Precondición:** La app está abierta y el mapa cargado
- **Flujo:** El pasajero toca una estación → El sistema muestra reportes activos
- **Postcondición:** El pasajero ve si hay trenes recientes reportados

### CU-02: Reportar paso de un tren
- **Actor:** Pasajero
- **Precondición:** El pasajero está en o cerca de una estación
- **Flujo:** Toca su estación en el mapa → Selecciona dirección del tren → Confirma el reporte
- **Postcondición:** El reporte queda registrado y visible para otros usuarios

### CU-03: Confirmar o rechazar un reporte
- **Actor:** Pasajero
- **Precondición:** Existe al menos un reporte activo en la estación
- **Flujo:** El pasajero ve el reporte → Toca "Confirmar" o "Rechazar"
- **Postcondición:** El reporte sube o baja en confiabilidad

---

## 7. 📖 Historias de Usuario

```
HU-01
Como pasajero del Suburbano,
quiero ver si hay trenes circulando en mi estación,
para decidir si vale la pena esperar o buscar otra opción de transporte.

HU-02
Como pasajero del Suburbano,
quiero reportar el paso de un tren tocando mi estación en el mapa,
para ayudar a otros usuarios a saber que el servicio está activo.

HU-03
Como pasajero del Suburbano,
quiero confirmar el reporte de otro usuario,
para que la información sea más confiable.

HU-04
Como pasajero del Suburbano,
quiero ver la dirección del tren reportado (hacia Buenavista o hacia Cuautitlán/AIFA),
para saber si el tren va en la dirección que necesito.
```

---

## 8. 🏗️ Arquitectura del Sistema

```
[Cualquier cliente: Web, Android, iOS — fase futura]
         │
         │ HTTP / REST
         ▼
[API REST - FastAPI / Python]  ← Fase actual
         │
         │ ORM / SQL
         ▼
[Base de Datos - PostgreSQL]
```

**Descripción de capas:**

| Capa | Tecnología | Responsabilidad | Fase |
|------|-----------|----------------|------|
| Backend | FastAPI (Python) | Lógica de negocio, validación, API REST | ✅ Actual |
| Base de datos | PostgreSQL | Persistencia de datos | 🔜 Próxima |
| Base de datos local | SQLite | BD ligera sin configuración | 🔜 Próxima |
| Frontend web | Por definir | Interfaz de usuario, mapa interactivo | 🔜 Futura |
| App Android | Kotlin | App nativa móvil | 🔜 Futura |

---

## 9. 🗄️ Modelo de Datos (Preliminar)

### Tabla: `lineas`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER | Identificador único |
| nombre | VARCHAR | Nombre de la línea |

### Tabla: `estaciones`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER | Identificador único |
| nombre | VARCHAR | Nombre de la estación |
| linea_id | INTEGER | FK → lineas |
| latitud | FLOAT | Coordenada GPS |
| longitud | FLOAT | Coordenada GPS |
| orden | INTEGER | Posición en la línea |

### Tabla: `reportes`
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER | Identificador único |
| estacion_id | INTEGER | FK → estaciones |
| direccion | VARCHAR | "buenavista" o "terminal" |
| timestamp | DATETIME | Fecha y hora del reporte |
| latitud | FLOAT | Coordenada GPS del usuario |
| longitud | FLOAT | Coordenada GPS del usuario |
| confirmaciones | INTEGER | Número de confirmaciones |
| rechazos | INTEGER | Número de rechazos |
| activo | BOOLEAN | Si el reporte sigue vigente |

---

## 10. 🔌 Endpoints Planeados

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/lineas` | Lista de líneas |
| GET | `/estaciones` | Lista de estaciones |
| GET | `/estaciones/{id}` | Detalle de una estación |
| POST | `/reportes` | Crear nuevo reporte |
| GET | `/reportes` | Consultar reportes activos |
| POST | `/reportes/{id}/confirmar` | Confirmar un reporte |
| POST | `/reportes/{id}/rechazar` | Rechazar un reporte |

---

## 11. ⚠️ Decisiones Pendientes

| # | Decisión | Impacto |
|---|----------|---------|
| 1 | ¿Login o reportes anónimos? | Arquitectura de autenticación |
| 2 | ¿TTL de reportes? (ej. 15 min) | Lógica de expiración |
| 3 | ¿Validación por GPS? | Seguridad de reportes |
| 4 | ¿Número mínimo de confirmaciones para mostrar reporte? | Confiabilidad |

---

## 12. 🚫 Fuera de Alcance (v1.0)

- Otros sistemas de transporte (Metro, Metrobús, Mexibús)
- Notificaciones push
- Historial de reportes
- Estadísticas de uso
- Frontend web *(fase futura)*
- App Android nativa en Kotlin *(fase futura)*

---

*Documento elaborado por el equipo de Movilidad México — Junio 2026*
