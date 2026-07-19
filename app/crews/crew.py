from crewai import Crew, Process
from app.agents.agents import AppAgents
from app.tasks.tasks import AppTasks

class SimpleCrew:
    def __init__(self):
        self.agentes = AppAgents()
        self.tareas = AppTasks()

    def procesar_solicitud(self, mensaje: str) -> str:
        """Procesa una solicitud utilizando un flujo de agente y tarea único."""
        # 1. Obtener agente de ejemplo
        agente = self.agentes.agente_asistente()
        
        # 2. Obtener tarea de ejemplo
        tarea = self.tareas.tarea_responder_solicitud(agente, mensaje)
        
        # 3. Inicializar tripulación (Crew)
        crew = Crew(
            agents=[agente],
            tasks=[tarea],
            process=Process.sequential,
            verbose=True
        )
        
        # 4. Ejecutar y retornar resultado
        resultado = crew.kickoff()
        return str(resultado).strip()
