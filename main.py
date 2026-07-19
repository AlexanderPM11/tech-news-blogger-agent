from app.crews.crew import SimpleCrew

def iniciar_chat_interactivo():
    print("="*60)
    print(" 🚀 INICIANDO MODO CHAT INTERACTIVO - DEPURADOR DE AGENTES (SIMPLE)")
    print("    (Escribe 'salir', 'exit' o 'quit' para terminar)")
    print("="*60)

    # 1. Instanciamos la tripulación simple
    crew = SimpleCrew()
    
    # 2. Bucle del chat de consola
    while True:
        try:
            mensaje_usuario = input("\n🧑 Usuario: ")
        except (KeyboardInterrupt, EOFError):
            print("\n[👋] Apagando el chat interactivo. ¡Hasta luego!")
            break
            
        if mensaje_usuario.lower().strip() in ['salir', 'exit', 'quit']:
            print("\n[👋] Apagando el chat interactivo. ¡Hasta luego!")
            break

        if not mensaje_usuario.strip():
            continue

        print("\n🤖 Procesando solicitud (Por favor espera)...\n")
        
        # Enviamos el mensaje al agente de la tripulación simple
        respuesta = crew.procesar_solicitud(mensaje_usuario)
        
        # Imprimir respuesta en consola
        print("\n========================================")
        print("          RESPUESTA DEL ASISTENTE       ")
        print("========================================")
        print(f"🤖 Asistente: {respuesta}\n")

if __name__ == "__main__":
    iniciar_chat_interactivo()
