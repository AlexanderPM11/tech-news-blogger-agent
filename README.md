# Plantilla de Agentes CrewAI con FastAPI para Creación de Contenido

Esta plantilla proporciona una estructura de carpetas limpia, desacoplada y lista para clonar y desarrollar proyectos inteligentes con **CrewAI** y **FastAPI**. Está configurada específicamente para funcionar como un generador automatizado de artículos de noticias y tendencias tecnológicas con salida JSON de estructura garantizada.

## Características Principales

- **Flujo Especializado de Doble Agente**:
  - **Periodista Investigador (`agente_periodista`)**: Investiga las tendencias y noticias tecnológicas más recientes de este año (2026), selecciona categorías y crea borradores en formato HTML.
  - **Editor Jefe y Humanizador (`agente_editor`)**: Pule el borrador, elimina modismos y clichés de IA ("En conclusión", "Es crucial", etc.), optimiza el SEO y reescribe el texto para que tenga un tono cercano, natural y de autoría humana propia.
- **Salida JSON Estructurada Garantizada**: Utiliza validación estricta con Pydantic (`ArticuloBlogger`) garantizando que la salida sea un objeto JSON parseable sin markdown sobrante.
- **Configuración Dinámica de LLMs**: Soporte integrado para OpenAI, Google Gemini, NVIDIA NIM y Ollama (local).
- **Entrada Doble**:
  - Interfaz de consola interactiva (CLI) para pruebas y depuración local rápida (`main.py`).
  - API FastAPI lista para producción (`api.py`), compatible con webhooks y herramientas de automatización como **n8n**.

---

## Estructura del Proyecto

```text
tech-news-blogger-agent/
├── app/
│   ├── agents/
│   │   └── agents.py           # Definición de Agentes (Periodista Investigador, Editor Jefe)
│   ├── core/
│   │   ├── config.py           # Configuración tipada de variables de entorno (Pydantic Settings)
│   │   └── llm_setup.py        # Inicialización del LLM activo (Ollama, OpenAI, Gemini, Nvidia)
│   ├── crews/
│   │   └── crew.py             # Clase orquestadora SimpleCrew (conecta agentes y tareas secuencialmente)
│   ├── tasks/
│   │   └── tasks.py            # Definición de Tareas (Investigar/Redactar y Humanizar/Formatear)
│   └── tools/
│       └── custom_tools.py     # Herramientas personalizadas para los agentes
├── .dockerignore
├── .env.example
├── .gitignore
├── api.py                      # Servidor FastAPI
├── Dockerfile                  # Configuración de contenedor Docker
├── docker-compose.yml          # Orquestación local por Docker Compose
├── main.py                     # Cliente interactivo de consola (CLI)
├── README.md                   # Documentación del proyecto
└── requirements.txt            # Dependencias de Python
```

---

## Configuración e Instalación Local

### 1. Crear y Activar el Entorno Virtual

**En Windows (PowerShell):**
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
Ideal para verificar el comportamiento de tus agentes y la interacción entre ellos:
```bash
python main.py
```
Introduce un tema para el artículo (ej: *"El impacto de la inteligencia artificial en el desarrollo web en 2026"*) y observa el flujo de trabajo de investigación y edición.

### Modo API (FastAPI)
Ejecuta el servidor web local:
```bash
python api.py
```
El endpoint de salud estará disponible en [http://localhost:8000/health](http://localhost:8000/health).
La interfaz interactiva de Swagger UI para probar los endpoints se encuentra en [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Integración con la API y Formato de Respuesta

Para solicitar la generación de un artículo, realiza una petición POST a:
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
  "mensaje": "El auge de los agentes de software autónomos en 2026",
  "session_id": "sesion-123"
}
```

### Estructura de la Respuesta JSON (en el campo `respuesta`):
La respuesta final se devuelve serializada como un string JSON en el campo `respuesta` de la respuesta de FastAPI, con la siguiente estructura exacta:

```json
{
  "title": "Título atractivo y optimizado para SEO",
  "content": "<h2>Sección 1</h2><p>Párrafo principal...</p><ul><li>Punto clave</li></ul>...",
  "excerpt": "Resumen SEO de máximo 160 caracteres",
  "status": "publish",
  "categories": [10, 23],
  "featured_image_prompt": "Detailed cinematic image generation prompt in English...",
  "featured_image_alt": "Descripción corta en español de la imagen destacada para accesibilidad"
}
```
