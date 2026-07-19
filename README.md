# Plantilla de Agente Investigador de Tecnología con FastAPI

Esta plantilla proporciona una estructura modular, desacoplada y limpia para un **Agente Investigador de Tecnología** automatizado basado en **CrewAI** y **FastAPI**. 

El agente está diseñado para recibir un tema o palabra clave de tecnología, investigar y redactar artículos técnicos de alta calidad con salida JSON estructurada y pulida por un editor humano. Adicionalmente, cuenta con un filtro para rechazar solicitudes que no pertenezcan al ámbito tecnológico e informático.

## Características Principales

- **Flujo Especializado de Doble Agente**:
  - **Periodista Investigador (`agente_periodista`)**: Evalúa si el tema propuesto es de tecnología/informática. Si lo es, investiga las tendencias más recientes de este año (2026), selecciona categorías del blog de WordPress y crea un borrador inicial en HTML. Si el tema no es de tecnología, detiene la ejecución y genera una respuesta de rechazo estructurada.
  - **Editor Jefe y Humanizador (`agente_editor`)**: Pule el borrador, elimina modismos y clichés de IA ("En conclusión", "Es crucial", etc.), optimiza el SEO y reescribe el texto para que tenga un tono cercano, natural y de autoría humana propia.
- **Salida JSON Estructurada Garantizada**: Utiliza validación estricta con Pydantic (`ArticuloBlogger`) garantizando que la salida sea un objeto JSON parseable.
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
│   ├── models/
│   │   └── articulo.py         # Definición del esquema de datos Pydantic (ArticuloBlogger)
│   ├── services/
│   │   └── wordpress.py        # Consulta dinámica de categorías a la API REST de WordPress
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
Introduce un tema para el artículo (ej: *"Arquitectura de microservicios en 2026"* o un tema no tecnológico para verificar el rechazo) y observa el flujo de trabajo de investigación y edición.

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
POST /investigar
```

### Headers Requeridos:
```http
Content-Type: application/json
x-api-key: <Tu valor de API_SECRET_KEY configurado en .env>
```

### Payload de la Petición:
```json
{
  "tema": "El auge de los agentes de software autónomos en 2026"
}
```

### Estructura de la Respuesta JSON:
La respuesta de FastAPI devuelve un objeto con la siguiente estructura:

```json
{
  "tema": "El auge de los agentes de software autónomos en 2026",
  "articulo": "{\"title\": \"...\", \"content\": \"...\", ...}",
  "tiempo_ejecucion": "12s"
}
```

La propiedad `articulo` contiene un string JSON válido con la siguiente estructura:

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

*Nota: Si el tema no es de tecnología, el campo `title` será "Tema no admitido", `status` será "draft", `categories` será [1] y `content` tendrá un mensaje aclarando el rechazo.*
