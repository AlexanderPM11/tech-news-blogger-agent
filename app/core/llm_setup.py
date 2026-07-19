import os
import litellm
from crewai import LLM
from app.core.config import settings

# Registrar el modelo de Ollama en LiteLLM para evitar el límite por defecto de 4096 tokens
custom_model = settings.OLLAMA_MODEL
if custom_model.startswith("ollama/") and hasattr(litellm, "model_cost"):
    litellm.model_cost[custom_model] = {
        "max_tokens": 16384,
        "input_cost_per_token": 0.0,
        "output_cost_per_token": 0.0,
        "litellm_provider": "ollama"
    }

# Asegurar que las API keys estén presentes en las variables de entorno para compatibilidad con LiteLLM
if settings.NVIDIA_API_KEY:
    os.environ["NVIDIA_NIM_API_KEY"] = settings.NVIDIA_API_KEY
    os.environ["NVIDIA_API_KEY"] = settings.NVIDIA_API_KEY

if settings.OPENAI_API_KEY:
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

if settings.GEMINI_API_KEY:
    os.environ["GEMINI_API_KEY"] = settings.GEMINI_API_KEY

# ==========================================
# CONFIGURACIONES DE PROVEEDORES
# ==========================================

# 1. MODELO LOCAL (OLLAMA)
local_llm = LLM(
    model=settings.OLLAMA_MODEL,
    base_url=settings.OLLAMA_URL,
    extra_body={"options": {"num_ctx": 16384, "num_predict": 8192}},
    max_tokens=8192
)

# 2. NVIDIA NIM
nvidia_llm = LLM(
    model=settings.NVIDIA_MODEL,
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=settings.NVIDIA_API_KEY
)

# 3. OPENAI
openai_llm = LLM(
    model=settings.OPENAI_MODEL,
    api_key=settings.OPENAI_API_KEY
)

# 4. GOOGLE GEMINI
gemini_llm = LLM(
    model=settings.GEMINI_MODEL,
    api_key=settings.GEMINI_API_KEY
)

# ==========================================
# SELECCIÓN DINÁMICA DEL MODELO
# ==========================================
# Opciones: 'ollama', 'nvidia', 'openai', 'gemini'
provider = settings.MODEL_PROVIDER.lower().strip()

if provider == "ollama":
    llm_activo = local_llm
    modelo_nombre = settings.OLLAMA_MODEL
elif provider == "openai":
    llm_activo = openai_llm
    modelo_nombre = settings.OPENAI_MODEL
elif provider == "gemini":
    llm_activo = gemini_llm
    modelo_nombre = settings.GEMINI_MODEL
else:
    # NVIDIA NIM por defecto
    llm_activo = nvidia_llm
    modelo_nombre = settings.NVIDIA_MODEL

print(f"[LLM] Usando proveedor: {provider} | Modelo: {modelo_nombre}")
