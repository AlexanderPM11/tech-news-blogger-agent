from typing import List
from pydantic import BaseModel, Field
from crewai import Task

class ArticuloBlogger(BaseModel):
    title: str = Field(..., description="Título atractivo y optimizado para SEO")
    content: str = Field(..., description="Artículo completo en HTML válido usando <h2>, <p>, <ul> y/o <ol>. Mínimo 500 palabras.")
    excerpt: str = Field(..., description="Resumen SEO de máximo 160 caracteres")
    status: str = Field("publish", description="Estado de publicación del artículo (por defecto 'publish')")
    categories: List[int] = Field(..., description="Lista de IDs numéricos de categorías seleccionadas")
    featured_image_prompt: str = Field(..., description="Detailed cinematic image generation prompt in English, describing the concept")
    featured_image_alt: str = Field(..., description="Descripción corta en español de la imagen generada, ideal para el alt_text de WordPress (máximo 125 caracteres, descriptivo, natural, sin términos técnicos)")

class AppTasks:
    
    def tarea_redactar_articulo(self, agente, tema_o_mensaje: str) -> Task:
        """
        Tarea para redactar un artículo periodístico tecnológico basado en un tema específico,
        seleccionando las categorías apropiadas de la lista disponible y estructurando la salida en JSON.
        """
        description = f"""
        Actúa como un periodista tecnológico Senior, analista de tendencias digitales y divulgador experto en Desarrollo de Software, Inteligencia Artificial, Ciberseguridad e Innovación Tecnológica. Tu misión es crear contenido de altísimo valor editorial, con enfoque periodístico profesional, altamente actualizado, optimizado para SEO y extremadamente fácil de leer.

        OBJETIVO PRINCIPAL:
        Generar EXACTAMENTE UN (1) artículo semanal sobre tendencias tecnológicas actuales, noticias recientes del sector tecnológico, inteligencia artificial, desarrollo de software, programación, innovación digital o ciberseguridad.
        El tema/entrada a desarrollar es: '{tema_o_mensaje}'.

        CONTEXTO DE CATEGORÍAS:
        Analiza cuidadosamente la siguiente lista de categorías disponibles en el blog y selecciona únicamente las que realmente correspondan con el tema del artículo.
        IDs y Nombres:
        25 - _highlights, 24 - _servicesonly, 13 - (P) - Aplicaciones Web, 14 - (P) - Ecommerce, 19 - aaPanel, 5 - Bases de Datos, 18 - Corporativo, 3 - Desarrollo Web, 4 - DevOps y Cloud, 9 - Educación y Tecnología, 16 - Finanzas, 6 - Frameworks y Librerías, 27 - Habilidades, 17 - Inmobiliaria, 21 - Mail, 22 - n8n, 10 - Noticias y Actualizaciones, 12 - projects, 8 - Proyectos y Casos Prácticos, 7 - Seguridad y Redes, 15 - Social, 23 - Tech Semanal, 11 - Tips y Snippets, 1 - Uncategorized, 20 - WebMail

        REGLAS DE INVESTIGACIÓN Y ACTUALIDAD (MUY IMPORTANTE):
        1. El artículo DEBE estar basado en información ACTUAL y RECIENTE.
        2. Debes investigar tendencias, noticias o tecnologías vigentes utilizando información de la semana actual, el mes actual o el año actual (2026).
        3. Prioriza noticias recientes relacionadas con: Inteligencia Artificial generativa, Desarrollo de software moderno, Programación, Cloud Computing, Ciberseguridad, Automatización, DevOps, Open Source, Big Data, Machine Learning, Startups tecnológicas, Innovación empresarial o Tecnología global.
        4. El contenido debe sentirse moderno, relevante y alineado con la actualidad tecnológica mundial. Evita temas obsoletos o tecnologías desactualizadas.
        5. Incluye referencias contextuales temporales como: “En 2026”, “Actualmente”, “En los últimos meses”, “Recientemente”, “Durante este año”.
        6. El artículo debe mezclar: análisis tecnológico, contexto de negocio, impacto social o empresarial, aplicaciones reales y tendencias futuras.

        REGLAS CRÍTICAS DE REDACCIÓN:
        1. Escribe como un periodista tecnológico profesional de alto nivel.
        2. El estilo debe ser: humano, natural, profesional, dinámico, claro, moderno.
        3. El artículo debe tener: introducción sólida, desarrollo lógico, subtítulos claros, conclusión contundente.
        4. Debe ser fácil de leer incluso para personas no técnicas. Evita lenguaje robótico o repetitivo. Usa storytelling periodístico cuando sea apropiado.
        5. El contenido debe parecer escrito para un portal tecnológico premium.

        REGLAS DE ESTRUCTURA HTML:
        1. El contenido debe estar completamente en HTML válido en la propiedad 'content'.
        2. Usa obligatoriamente: <h2> para secciones, <p> para párrafos, <ul> para enumeraciones, <ol> para rankings, pasos o procesos.
        3. NO uses Markdown dentro de 'content'. NO insertes imágenes dentro del HTML.
        4. El contenido de 'content' debe tener MÍNIMO 500 palabras.
        5. Puedes usar también: <strong>, <em>, <blockquote>.

        REGLAS SEO:
        1. El título debe ser atractivo, moderno y optimizado para SEO.
        2. El excerpt debe tener máximo 160 caracteres.
        3. Incluye naturalmente keywords relacionadas con: IA, desarrollo, tecnología, programación, innovación, software. Evita keyword stuffing.

        REGLAS DE IMAGEN Y ACCESIBILIDAD (MUY IMPORTANTE):
        1. La propiedad `featured_image_prompt` DEBE estar escrita en INGLÉS. Esto mejora enormemente la calidad y precisión de la imagen generada.
        2. La propiedad `featured_image_alt` DEBE estar escrita en ESPAÑOL. Debe ser una descripción corta y natural de la escena para accesibilidad (máximo 125 caracteres, descriptivo, natural, sin términos técnicos). No incluyas palabras clave de prompts como "cyberpunk style", "cinematic", "photorealistic", etc.
        """

        return Task(
            description=description,
            expected_output="Un único objeto JSON válido que representa el artículo completo.",
            agent=agente,
            output_json=ArticuloBlogger
        )
