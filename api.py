import time
import uuid
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from app.core.config import settings
from app.crews.crew import SimpleCrew

API_SECRET_KEY = settings.API_SECRET_KEY

app = FastAPI(title="FastAPI CrewAI Agentic Template API")


class MensajeRequest(BaseModel):
    mensaje: Optional[str] = None
    session_id: Optional[str] = None
    chatInput: Optional[str] = None
    sessionId: Optional[str] = None

    def obtener_mensaje(self) -> str:
        mensaje = self.mensaje or self.chatInput
        if not mensaje or not mensaje.strip():
            raise HTTPException(
                status_code=422,
                detail="Debes enviar 'mensaje' o 'chatInput'.",
            )
        return mensaje.strip()

    def obtener_session_id(self) -> Optional[str]:
        session_id = self.session_id or self.sessionId
        return session_id.strip() if session_id else None


class MensajeResponse(BaseModel):
    session_id: str
    respuesta: str
    output: str
    text: str
    tiempo_ejecucion: str


@app.get("/")
async def root():
    return {"status": "ok", "service": "Agentic API Template"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


def procesar_chat_sync(request: MensajeRequest, x_api_key: Optional[str]):
    # Verificar API Key si se ha configurado un Secret Key
    if API_SECRET_KEY and API_SECRET_KEY != "default-secret-key-change-me":
        if x_api_key != API_SECRET_KEY:
            raise HTTPException(status_code=403, detail="Acceso denegado: API Key inválida")

    start_time = time.time()
    mensaje = request.obtener_mensaje()
    session_id = request.obtener_session_id() or str(uuid.uuid4())

    try:
        # Ejecutar la tripulación simple
        crew = SimpleCrew()
        respuesta_final = crew.procesar_solicitud(mensaje)

        # Calcular tiempo transcurrido
        duracion = time.time() - start_time
        if duracion >= 60:
            tiempo_str = f"{int(duracion // 60)}m {int(duracion % 60)}s"
        else:
            tiempo_str = f"{int(duracion)}s"

        return MensajeResponse(
            session_id=session_id,
            respuesta=respuesta_final,
            output=respuesta_final,
            text=respuesta_final,
            tiempo_ejecucion=tiempo_str,
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Error procesando chat: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


async def procesar_chat(request: MensajeRequest, x_api_key: Optional[str]):
    return await run_in_threadpool(procesar_chat_sync, request, x_api_key)


@app.post("/chat", response_model=MensajeResponse)
async def chat(request: MensajeRequest, x_api_key: Optional[str] = Header(None)):
    return await procesar_chat(request, x_api_key)


@app.post("/api/chat", response_model=MensajeResponse)
async def api_chat(request: MensajeRequest, x_api_key: Optional[str] = Header(None)):
    return await procesar_chat(request, x_api_key)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
