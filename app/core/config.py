from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # --- API / Seguridad ---
    API_SECRET_KEY: str = "default-secret-key-change-me"

    # --- Proveedor de LLM activo (ollama, nvidia, openai, gemini) ---
    MODEL_PROVIDER: str = "openai"

    # --- Ollama (Local) ---
    OLLAMA_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "ollama/gemma4:e2b"

    # --- NVIDIA NIM ---
    NVIDIA_API_KEY: Optional[str] = None
    NVIDIA_MODEL: str = "nvidia_nim/google/gemma-3n-e4b-it"

    # --- OpenAI ---
    OPENAI_API_KEY: Optional[str] = None
    OPENAI_MODEL: str = "openai/gpt-4o-mini"

    # --- Gemini ---
    GEMINI_API_KEY: Optional[str] = None
    GEMINI_MODEL: str = "gemini/gemini-2.5-flash"

    # --- Agrega aquí tus variables para APIs externas o herramientas ---
    # EJEMPLO_API_KEY: Optional[str] = None

    # --- WordPress ---
    WORDPRESS_CATEGORIES_URL: str = "https://blog.apolanco.com/wp-json/wp/v2/categories"


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
