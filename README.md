# Plantilla de Agente Autónomo de Investigación Tecnológica con FastAPI

Esta plantilla proporciona una estructura modular, desacoplada y limpia para un **Agente Autónomo de Investigación Tecnológica** basado en **CrewAI** y **FastAPI**. 

El agente está diseñado para iniciarse de forma 100% autónoma. No espera preguntas del usuario ni requiere ingresar un tema específico. Al invocarse, el agente investiga tendencias actuales, selecciona el tema tecnológico de mayor impacto, profundiza en su investigación y genera artículos técnicos en un formato JSON estructurado listo para ser publicado en plataformas como WordPress (a través de automatizaciones como n8n).

## Características Principales

- **Flujo Especializado de Doble Agente**:
  - **Periodista Investigador (`agente_periodista`)**: Identifica autónomamente las tendencias del desarrollo de software y tecnología del año actual (2026). Evalúa popularidad, actualidad e impacto para elegir el mejor tema del sector tecnológico, e investiga y redacta el borrador en formato HTML.
  - **Editor Jefe y Humanizador (`agente_editor`)**: Pule el borrador, elimina modismos y clichés de IA ("En conclusión", "Es crucial", etc.), optimiza el SEO y reescribe el texto para que tenga un tono cercano, natural y de autoría humana propia.
- **Salida JSON Estructurada Garantizada**: Utiliza validación estricta con Pydantic (`ArticuloBlogger`) garantizando que la salida sea un objeto JSON parseable.
- **Configuración Dinámica de LLMs**: Soporte integrado para OpenAI, Google Gemini, NVIDIA NIM y Ollama (local).
- **Entrada Doble**:
  - Interfaz de consola (`main.py`) que ejecuta inmediatamente el proceso autónomo de investigación.
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
├── main.py                     # Cliente de consola de ejecución autónoma (CLI)
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

### Modo Consola (CLI)
Ejecuta el script para iniciar la investigación y redacción de manera autónoma de inmediato:
```bash
python main.py
```
El agente buscará tendencias, seleccionará la más relevante, generará el artículo e imprimirá el JSON resultante en pantalla.

### Modo API (FastAPI)
Ejecuta el servidor web local:
```bash
python api.py
```
El endpoint de salud estará disponible en [http://localhost:8000/health](http://localhost:8000/health).
La interfaz interactiva de Swagger UI se encuentra en [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Integración con la API y Formato de Respuesta

Para solicitar la generación de un artículo de manera autónoma, realiza una petición POST sin cuerpo a:
```text
POST /investigar
```

### Headers Requeridos:
```http
Content-Type: application/json
x-api-key: <Tu valor de API_SECRET_KEY configurado en .env>
```

### Estructura de la Respuesta JSON:
La respuesta de FastAPI devuelve un objeto con el tiempo de ejecución y el JSON del artículo en el campo `articulo`:

```json
{
  "articulo": "{\"title\": \"...\", \"content\": \"...\", ...}",
  "tiempo_ejecucion": "12s"
}
```

La propiedad `articulo` contiene el string JSON de salida del agente con la siguiente estructura:

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
