from app.crews.crew import SimpleCrew

def ejecutar_investigacion_autonoma():
    print("="*60)
    print(" 🚀 EJECUTANDO AGENTE AUTÓNOMO DE INVESTIGACIÓN TECNOLÓGICA (CLI)")
    print("="*60)
    print("\n🔍 Detectando tendencias, seleccionando tema y redactando contenido (Por favor espera)...\n")

    # 1. Instanciamos la tripulación
    crew = SimpleCrew()
    
    # 2. Ejecutar el flujo autónomo
    try:
        respuesta = crew.procesar_solicitud()
        
        # Imprimir respuesta en consola
        print("\n========================================================")
        print("      ARTÍCULO / INVESTIGACIÓN GENERADA AUTÓNOMAMENTE   ")
        print("========================================================")
        print(f"🤖 Resultado:\n{respuesta}\n")
    except Exception as e:
        print(f"\n[ERROR] Ocurrió un fallo en la ejecución autónoma: {e}")

if __name__ == "__main__":
    ejecutar_investigacion_autonoma()
