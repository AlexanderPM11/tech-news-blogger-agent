# Plantilla Minimalista de Agentes CrewAI con FastAPI

Esta plantilla proporciona una estructura de carpetas limpia, desacoplada y lista para clonar y desarrollar proyectos inteligentes con **CrewAI** y **FastAPI**.

## Características Principales

- **Estructura Modular Limpia**: Componentes separados lógicamente para agentes, tareas y herramientas.
- **Configuración Dinámica de LLMs**: Soporte integrado para OpenAI, Google Gemini, NVIDIA NIM y Ollama (local).
- **Entrada Doble**:
  - Interfaz de consola interactiva (CLI) para pruebas y depuración local rápida.
  - API FastAPI lista para producción, compatible con webhooks y herramientas de automatización como **n8n**.
- **Fácilmente Extensible**: Reemplaza o añade tus agentes, tareas y herramientas en sus respectivas carpetas sin romper el flujo principal.

---

## Estructura del Proyecto

```text
template - api - crewai/
├── app/
│   ├── agents/
│   │   └── agents.py           # Definición de tus Agentes (ej. Asistente)
│   ├── core/
│   │   ├── config.py           # Configuración tipada de variables de entorno (Pydantic Settings)
│   │   └── llm_setup.py        # Inicialización del LLM activo (Ollama, OpenAI, Gemini, Nvidia)
│   ├── crews/
│   │   └── crew.py             # Clase orquestadora SimpleCrew (conecta agentes y tareas)
│   ├── tasks/
│   │   └── tasks.py            # Definición de tus Tareas
│   └── tools/
│       └── custom_tools.py     # Herramientas personalizadas con decorador @tool de CrewAI
├── .dockerignore
├── .env.example
├── .gitignore
├── api.py                      # Servidor FastAPI
├── Dockerfile                  # Configuración de contenedor Docker
├── docker-compose.yml          # Orquestación local por Docker Compose
├── main.py                     # Cliente interactivo de consola (CLI)
└── requirements.txt            # Dependencias de Python
```

---

## Configuración e Instalación Local

### 1. Crear y Activar el Entorno Virtual

**En Windows:**
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En macOS y Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar las Variables de Entorno
Copia el archivo `.env.example` como `.env`:
```bash
cp .env.example .env
```
Completa tu proveedor preferido en `MODEL_PROVIDER` (`openai`, `gemini`, `nvidia`, `ollama`) y su correspondiente API Key.

---

## Cómo Ejecutar el Proyecto

### Modo Consola Interactivo (CLI)
Ideal para verificar el comportamiento de tus agentes rápidamente:
```bash
python main.py
```

### Modo API (FastAPI)
Ejecuta el servidor web local:
```bash
python api.py
```
El endpoint de salud estará disponible en [http://localhost:8000/health](http://localhost:8000/health).

---

## Integración con la API conversacional

Para enviar mensajes a tu Crew a través de la API, envía una petición POST segura a:
```text
POST /chat
```

### Headers Requeridos:
```http
Content-Type: application/json
x-api-key: <Tu valor de API_SECRET_KEY configurado en .env>
```

### Payload de la Petición:
```json
{
  "mensaje": "Hola, por favor ejecuta la acción de ejemplo con el parámetro 'mi_valor'",
  "session_id": "sesion-123"
}
```

---

## Cómo Personalizar la Plantilla

1. **Añadir Herramientas**: Agrega tus funciones personalizadas decoradas con `@tool` en `app/tools/custom_tools.py`.
2. **Añadir Agentes**: Crea nuevos agentes y asígnales herramientas en `app/agents/agents.py`.
3. **Añadir Tareas**: Describe las misiones y objetivos de tus agentes en `app/tasks/tasks.py`.
4. **Conectar en la Crew**: Importa y conecta tus nuevos agentes y tareas en `app/crews/crew.py`.
