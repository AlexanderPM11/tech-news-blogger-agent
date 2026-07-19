from app.crews.crew import SimpleCrew

def iniciar_investigador_interactivo():
    print("="*60)
    print(" 🚀 INICIANDO AGENTE INVESTIGADOR DE TECNOLOGÍA (CLI)")
    print("    (Escribe 'salir', 'exit' o 'quit' para terminar)")
    print("="*60)

    # 1. Instanciamos la tripulación
    crew = SimpleCrew()
    
    # 2. Bucle del investigador de consola
    while True:
        try:
            tema_investigacion = input("\n📝 Tema a investigar: ")
        except (KeyboardInterrupt, EOFError):
            print("\n[👋] Apagando el investigador tecnológico. ¡Hasta luego!")
            break
            
        if tema_investigacion.lower().strip() in ['salir', 'exit', 'quit']:
            print("\n[👋] Apagando el investigador tecnológico. ¡Hasta luego!")
            break

        if not tema_investigacion.strip():
            continue

        print("\n🔍 Investigando y redactando contenido (Por favor espera)...\n")
        
        # Enviamos el tema al agente
        respuesta = crew.procesar_solicitud(tema_investigacion)
        
        # Imprimir respuesta en consola
        print("\n========================================")
        print("         ARTÍCULO / INVESTIGACIÓN       ")
        print("========================================")
        print(f"🤖 Resultado:\n{respuesta}\n")

if __name__ == "__main__":
    iniciar_investigador_interactivo()
