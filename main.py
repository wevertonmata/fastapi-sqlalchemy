from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from src.core.configs import settings
from src.api.v1.api import api_router_v1

app = FastAPI(
    title="Crud com PostgresSQL",
    version='1.0.0',
    description="API de estudo FastAPI com SqlAlchemy."
)

# Redirect to docs

@app.get("/",  include_in_schema=False)
async def docs_redirect():
    return RedirectResponse(url='/docs')


## Routes

app.include_router(api_router_v1, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, log_level='info')