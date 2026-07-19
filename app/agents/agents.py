from crewai import Agent
from app.core.llm_setup import llm_activo
from app.tools.custom_tools import herramienta_ejemplo


class AppAgents:
    def __init__(self):
        self.llm = llm_activo

    
    def agente_periodista(self) -> Agent:
        """
        Agente Periodista Investigador y Redactor.
        """
        return Agent(
            role="Periodista Investigador Tecnológico Senior",
            goal=(
                "Investigar temas de tecnología de actualidad (2026) y redactar un borrador de alta "
                "calidad periodística con estructura HTML y selección de categorías."
            ),
            backstory=(
                "Eres un periodista e investigador tecnológico senior. Tu fuerte es analizar las últimas "
                "tendencias globales, contrastar información veraz y redactar borradores bien estructurados "
                "con la información técnica y de negocio más relevante."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )

    def agente_editor(self) -> Agent:
        """
        Agente Editor y Reescritor Humano.
        """
        return Agent(
            role="Editor Jefe y Experto en Humanización de Contenido",
            goal=(
                "Pulir y reescribir la redacción del borrador para que tenga un tono 100% humano, natural, "
                "cercano, fácil de entender y que parezca una investigación de autoría propia, "
                "eliminando cualquier rastro de lenguaje automatizado o patrones típicos de IA."
            ),
            backstory=(
                "Eres un Editor Jefe y Copywriter de élite especializado en humanizar textos tecnológicos. "
                "Tu superpoder es transformar borradores técnicos o densos en lecturas fluidas, naturales "
                "y extremadamente atractivas. Odias las frases trilladas de las IAs (como 'en resumen', "
                "'es crucial', 'en conclusión') y los tonos demasiado académicos o robóticos. Reescribes "
                "el contenido como si fuera tu propia investigación personal, usando un vocabulario sencillo "
                "pero profesional, asegurando que sea accesible para todo tipo de público y manteniendo la estructura HTML."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )
