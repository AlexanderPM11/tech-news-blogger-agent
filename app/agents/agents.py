from crewai import Agent
from app.core.llm_setup import llm_activo
from app.tools.custom_tools import herramienta_ejemplo


class AppAgents:
    def __init__(self):
        self.llm = llm_activo

    def agente_asistente(self) -> Agent:
        """
        Agente de ejemplo encargado de responder al usuario.
        """
        return Agent(
            role="Asistente de Ejemplo",
            goal="Ayudar al usuario resolviendo sus dudas y ejecutando la herramienta de ejemplo si es necesario.",
            backstory=(
                "Eres un asistente virtual muy atento. Tu objetivo es procesar la "
                "solicitud del usuario de manera clara, concisa y utilizando tus "
                "herramientas disponibles de forma efectiva."
            ),
            tools=[herramienta_ejemplo],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
        )
