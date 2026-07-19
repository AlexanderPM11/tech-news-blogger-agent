from crewai import Crew, Process
from app.agents.agents import AppAgents
from app.tasks.tasks import AppTasks
from app.services.wordpress import obtener_categorias_wordpress

class SimpleCrew:
    def __init__(self):
        self.agentes = AppAgents()
        self.tareas = AppTasks()

    def procesar_solicitud(self) -> str:
        """Procesa el flujo autónomo de investigación y redacción tecnológica."""
        # 1. Obtener agentes
        periodista = self.agentes.agente_periodista()
        editor = self.agentes.agente_editor()
        
        # 2. Obtener categorías dinámicas
        categorias = obtener_categorias_wordpress()
        
        # 3. Obtener tareas
        borrador_task = self.tareas.tarea_investigar_y_redactar(periodista, categorias)
        edicion_task = self.tareas.tarea_humanizar_y_formatear(editor, borrador_task)
        
        # 4. Inicializar tripulación (Crew)
        crew = Crew(
            agents=[periodista, editor],
            tasks=[borrador_task, edicion_task],
            process=Process.sequential,
            verbose=True
        )
        
        # 5. Ejecutar y retornar resultado
        resultado = crew.kickoff()
        
        # Retornar como JSON string para mantener compatibilidad
        if resultado.json:
            import json
            return json.dumps(resultado.json, ensure_ascii=False)
            
        return str(resultado).strip()
