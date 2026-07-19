from crewai import Agent
from app.core.llm_setup import llm_activo
from app.tools.custom_tools import herramienta_ejemplo


class AppAgents:
    def __init__(self):
        self.llm = llm_activo

    
    def agente_periodista(self) -> Agent:
        """
        Agente Periodista Tecnológico Senior.
        """
        return Agent(
            role="Periodista Tecnológico Senior, analista de tendencias digitales y divulgador experto",
            goal=(
                "Crear contenido de altísimo valor editorial, con enfoque periodístico profesional, "
                "altamente actualizado, optimizado para SEO y extremadamente fácil de leer."
            ),
            backstory=(
                "Eres un periodista tecnológico Senior, analista de tendencias digitales y divulgador experto "
                "en Desarrollo de Software, Inteligencia Artificial, Ciberseguridad e Innovación Tecnológica. "
                "Tu misión es redactar artículos con enfoque periodístico profesional, altamente actualizados, "
                "alineados con las tendencias globales y optimizados para SEO de manera natural."
            ),
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )
