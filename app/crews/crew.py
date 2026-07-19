from crewai import Crew, Process
from app.agents.agents import AppAgents
from app.tasks.tasks import AppTasks

class SimpleCrew:
    def __init__(self):
        self.agentes = AppAgents()
        self.tareas = AppTasks()

    def procesar_solicitud(self, mensaje: str) -> str:
        """Procesa una solicitud utilizando un flujo de agente y tarea de redacción periodística."""
        # 1. Obtener agente periodista
        agente = self.agentes.agente_periodista()
        
        # 2. Obtener tarea de redacción de artículo
        tarea = self.tareas.tarea_redactar_articulo(agente, mensaje)
        
        # 3. Inicializar tripulación (Crew)
        crew = Crew(
            agents=[agente],
            tasks=[tarea],
            process=Process.sequential,
            verbose=True
        )
        
        # 4. Ejecutar y retornar resultado
        resultado = crew.kickoff()
        
        # Retornar como JSON string para mantener compatibilidad
        if resultado.json:
            import json
            return json.dumps(resultado.json, ensure_ascii=False)
            
        return str(resultado).strip()
