from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.application.rest import patient_route, visit_route

app = FastAPI(
    root_path="",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient_route)
app.include_router(visit_route)


import uvicorn

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1")
