from crewai import LLM
from app.core.config import settings

# ==========================================
# CONFIGURACIONES DE PROVEEDORES
# ==========================================

# 1. MODELO LOCAL (OLLAMA)
local_llm = LLM(
    model=settings.OLLAMA_MODEL,
    base_url=settings.OLLAMA_URL,
    extra_body={"options": {"num_ctx": 8192}}
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
