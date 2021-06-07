from fastapi import FastAPI
from starlette.responses import JSONResponse


app = FastAPI(
    title="{{ cookiecutter.project_name }}",
    version="0.0.1"
)


@app.on_event("startup")
def startup():
    print("Start server")


@app.on_event("shutdown")
def shutdown():
    print("Shutdown server")


# app.include_router(api_router, prefix=config.API_V1_STR)


@app.get("/")
async def get_index():
    return JSONResponse(content={"Hello": "World!"})
