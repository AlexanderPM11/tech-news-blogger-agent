from crewai import Task

class AppTasks:
    def tarea_responder_solicitud(self, agente, mensaje_usuario: str) -> Task:
        """
        Tarea de ejemplo: Procesa y responde la solicitud del usuario de forma directa.
        """
        return Task(
            description=(
                f"Procesa el siguiente requerimiento del usuario: '{mensaje_usuario}'.\n"
                f"Si el usuario pide ejecutar la acción de ejemplo, utiliza la herramienta de ejemplo disponible.\n"
                f"Responde siempre de forma clara, amable y concisa."
            ),
            expected_output="Respuesta clara y directa al usuario confirmando la resolución o acción.",
            agent=agente,
        )
