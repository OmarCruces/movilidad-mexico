# 📐 Diagramas UML — Movilidad México

> Diagramas de diseño del sistema usando notación Mermaid.  
> Versión: 1.0 | Fecha: Junio 2026

---

## 1. 🧑‍💻 Diagrama de Casos de Uso

```mermaid
graph TD
    Pasajero((Pasajero))

    Pasajero --> CU01[Consultar estado de estación]
    Pasajero --> CU02[Reportar paso de tren]
    Pasajero --> CU03[Confirmar reporte]
    Pasajero --> CU04[Rechazar reporte]
    Pasajero --> CU05[Ver líneas disponibles]
    Pasajero --> CU06[Ver estaciones por línea]

    CU02 --> CU07[Seleccionar dirección del tren]
    CU03 --> CU08[Validación comunitaria]
    CU04 --> CU08
```

**Descripción:**
- El único actor en esta fase es el **Pasajero**.
- El sistema no tiene administradores en v1.0.
- La validación comunitaria se activa con confirmaciones y rechazos.

---

## 2. 🏛️ Diagrama de Clases

```mermaid
classDiagram
    class Linea {
        +int id
        +string nombre
        +list~Estacion~ estaciones
        +get_estaciones()
    }

    class Estacion {
        +int id
        +string nombre
        +int linea_id
        +float latitud
        +float longitud
        +int orden
        +list~Reporte~ reportes
        +get_reportes_activos()
    }

    class Reporte {
        +int id
        +int estacion_id
        +string direccion
        +datetime timestamp
        +float latitud
        +float longitud
        +int confirmaciones
        +int rechazos
        +bool activo
        +confirmar()
        +rechazar()
        +expirar()
    }

    Linea "1" --> "1..*" Estacion : contiene
    Estacion "1" --> "0..*" Reporte : tiene
```

---

## 3. 🔄 Diagrama de Secuencia — Reportar paso de tren

```mermaid
sequenceDiagram
    actor Pasajero
    participant App as Cliente Web/App
    participant API as FastAPI
    participant DB as Base de Datos

    Pasajero->>App: Abre la aplicación
    App->>API: GET /estaciones
    API->>DB: SELECT estaciones
    DB-->>API: Lista de estaciones
    API-->>App: JSON estaciones
    App-->>Pasajero: Muestra mapa con estaciones

    Pasajero->>App: Toca su estación en el mapa
    App-->>Pasajero: Muestra opciones de dirección

    Pasajero->>App: Selecciona dirección del tren
    App->>API: POST /reportes
    Note right of API: {estacion_id, direccion, latitud, longitud}
    API->>DB: INSERT reporte
    DB-->>API: Reporte guardado
    API-->>App: 201 Created
    App-->>Pasajero: Reporte registrado ✅
```

---

## 4. 🔄 Diagrama de Secuencia — Confirmar reporte

```mermaid
sequenceDiagram
    actor Pasajero
    participant App as Cliente Web/App
    participant API as FastAPI
    participant DB as Base de Datos

    Pasajero->>App: Consulta estación
    App->>API: GET /reportes?estacion_id=X
    API->>DB: SELECT reportes activos
    DB-->>API: Lista de reportes
    API-->>App: JSON reportes
    App-->>Pasajero: Muestra reportes activos

    Pasajero->>App: Toca "Confirmar" en un reporte
    App->>API: POST /reportes/{id}/confirmar
    API->>DB: UPDATE confirmaciones + 1
    DB-->>API: OK
    API-->>App: 200 OK
    App-->>Pasajero: Confirmación registrada ✅
```

---

## 5. 🗄️ Diagrama Entidad-Relación

```mermaid
erDiagram
    LINEA {
        int id PK
        string nombre
    }

    ESTACION {
        int id PK
        string nombre
        int linea_id FK
        float latitud
        float longitud
        int orden
    }

    REPORTE {
        int id PK
        int estacion_id FK
        string direccion
        datetime timestamp
        float latitud
        float longitud
        int confirmaciones
        int rechazos
        bool activo
    }

    LINEA ||--o{ ESTACION : "tiene"
    ESTACION ||--o{ REPORTE : "recibe"
```

---

## 6. 🧩 Diagrama de Componentes

```mermaid
graph TB
    subgraph Cliente
        WEB[Cliente Web / App]
    end

    subgraph Backend
        API[FastAPI]
        subgraph Routers
            R1[/lineas]
            R2[/estaciones]
            R3[/reportes]
        end
    end

    subgraph Base de Datos
        DEV[(SQLite\nDesarrollo)]
        PROD[(PostgreSQL\nProducción)]
    end

    WEB -->|HTTP REST| API
    API --> R1
    API --> R2
    API --> R3
    R1 --> DEV
    R2 --> DEV
    R3 --> DEV
    DEV -.->|migración futura| PROD
```

---

## 7. 🔁 Diagrama de Actividad — Ciclo de vida de un reporte

```mermaid
stateDiagram-v2
    [*] --> Creado : Pasajero reporta tren

    Creado --> Activo : Reporte registrado
    Activo --> Confirmado : confirmaciones >= umbral
    Activo --> Rechazado : rechazos > confirmaciones
    Activo --> Expirado : TTL vencido (ej. 15 min)

    Confirmado --> Expirado : TTL vencido
    Rechazado --> [*]
    Expirado --> [*]
```

---

> 📋 Ver análisis completo del sistema en [docs/analisis.md](./analisis.md)

---

*Diagramas elaborados por el equipo de Movilidad México — Junio 2026*
