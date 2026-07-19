import time
from typing import Optional

from fastapi import FastAPI, Header, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel

from app.core.config import settings
from app.crews.crew import SimpleCrew

API_SECRET_KEY = settings.API_SECRET_KEY

app = FastAPI(title="FastAPI CrewAI Technology Researcher API")


class InvestigacionResponse(BaseModel):
    articulo: str
    tiempo_ejecucion: str


@app.get("/")
async def root():
    return {"status": "ok", "service": "Technology Researcher API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}


def procesar_investigacion_sync(x_api_key: Optional[str]):
    # Verificar API Key si se ha configurado un Secret Key
    if API_SECRET_KEY and API_SECRET_KEY != "default-secret-key-change-me":
        if x_api_key != API_SECRET_KEY:
            raise HTTPException(status_code=403, detail="Acceso denegado: API Key inválida")

    start_time = time.time()

    try:
        # Ejecutar la tripulación del investigador de forma autónoma
        crew = SimpleCrew()
        respuesta_final = crew.procesar_solicitud()

        # Calcular tiempo transcurrido
        duracion = time.time() - start_time
        if duracion >= 60:
            tiempo_str = f"{int(duracion // 60)}m {int(duracion % 60)}s"
        else:
            tiempo_str = f"{int(duracion)}s"

        return InvestigacionResponse(
            articulo=respuesta_final,
            tiempo_ejecucion=tiempo_str,
        )

    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] Error procesando investigación autónoma: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


async def procesar_investigacion(x_api_key: Optional[str]):
    return await run_in_threadpool(procesar_investigacion_sync, x_api_key)


@app.post("/investigar", response_model=InvestigacionResponse)
async def investigar(x_api_key: Optional[str] = Header(None)):
    return await procesar_investigacion(x_api_key)


@app.post("/api/investigar", response_model=InvestigacionResponse)
async def api_investigar(x_api_key: Optional[str] = Header(None)):
    return await procesar_investigacion(x_api_key)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
