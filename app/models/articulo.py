from pydantic import BaseModel, Field
from typing import List

class ArticuloBlogger(BaseModel):
    title: str = Field(..., description="Título atractivo y optimizado para SEO")
    content: str = Field(..., description="Artículo completo en HTML válido usando <h2>, <p>, <ul> y/o <ol>. Mínimo 500 palabras.")
    excerpt: str = Field(..., description="Resumen SEO de máximo 160 caracteres")
    status: str = Field("publish", description="Estado de publicación del artículo (por defecto 'publish')")
    categories: List[int] = Field(..., description="Lista de IDs numéricos de categorías seleccionadas")
    featured_image_prompt: str = Field(..., description="Detailed cinematic image generation prompt in English, describing the concept")
    featured_image_alt: str = Field(..., description="Descripción corta en español de la imagen generada, ideal para el alt_text de WordPress (máximo 125 caracteres, descriptivo, natural, sin términos técnicos)")
