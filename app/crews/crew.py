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
        import json
        articulo_dict = None
        
        # 1. Intentar obtener desde resultado.json (puede ser dict o str)
        if resultado.json:
            if isinstance(resultado.json, dict):
                articulo_dict = resultado.json
            elif isinstance(resultado.json, str):
                try:
                    articulo_dict = json.loads(resultado.json)
                except Exception:
                    pass

        # 2. Si falló, intentar parsear desde el resultado crudo (raw)
        if not isinstance(articulo_dict, dict) and resultado.raw:
            try:
                # Quitar posibles marcas de markdown del texto crudo antes de parsear
                raw_clean = resultado.raw.replace("```json", "").replace("```", "").strip()
                articulo_dict = json.loads(raw_clean)
            except Exception:
                pass

        # 3. Si logramos obtener un diccionario, inyectamos la métrica y serializamos
        if isinstance(articulo_dict, dict):
            articulo_dict["tiempo_ejecucion"] = tiempo_str
            return json.dumps(articulo_dict, ensure_ascii=False)
            
        return str(resultado).strip()
