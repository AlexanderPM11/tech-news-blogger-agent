from crewai.tools import tool

@tool("herramienta_ejemplo")
def herramienta_ejemplo(parametro: str) -> str:
    """
    Herramienta de ejemplo que realiza una acción simulada en el sistema.
    Úsala cuando el usuario te pida explícitamente ejecutar la acción de ejemplo.
    """
    print(f"[TOOL herramienta_ejemplo] Ejecutada con el parámetro: {parametro}")
    return f"Éxito: La acción de ejemplo fue procesada correctamente con el parámetro '{parametro}'."
