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
        
        # 5. Ejecutar y retornar resultado midiendo el tiempo
        import time
        start_time = time.time()
        resultado = crew.kickoff()
        duracion = time.time() - start_time
        
        # Formatear duración de manera legible
        if duracion >= 60:
            tiempo_str = f"{int(duracion // 60)}m {int(duracion % 60)}s"
        else:
            tiempo_str = f"{int(duracion)}s"
        
        # Retornar como JSON string inyectando la métrica de tiempo
        if resultado.json:
            import json
            articulo_dict = dict(resultado.json)
            articulo_dict["tiempo_ejecucion"] = tiempo_str
            return json.dumps(articulo_dict, ensure_ascii=False)
            
        return str(resultado).strip()
