from crewai import Crew, Process
from app.agents.agents import AppAgents
from app.tasks.tasks import AppTasks

class SimpleCrew:
    def __init__(self):
        self.agentes = AppAgents()
        self.tareas = AppTasks()

    def procesar_solicitud(self, mensaje: str) -> str:
        """Procesa una solicitud utilizando un flujo de dos agentes: redacción y edición/humanización."""
        # 1. Obtener agentes
        periodista = self.agentes.agente_periodista()
        editor = self.agentes.agente_editor()
        
        # 2. Obtener tareas
        borrador_task = self.tareas.tarea_investigar_y_redactar(periodista, mensaje)
        edicion_task = self.tareas.tarea_humanizar_y_formatear(editor, borrador_task)
        
        # 3. Inicializar tripulación (Crew)
        crew = Crew(
            agents=[periodista, editor],
            tasks=[borrador_task, edicion_task],
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
