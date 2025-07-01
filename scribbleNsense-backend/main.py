from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from constants import SERVER_URL, PORT, ENV
from apps.calculator.route import router as calculator_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://scribble-n-sense.vercel.app",
        "http://localhost:5173",
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def root():
    return {"message": "Server is running"}

app.include_router(calculator_router, prefix='/calculate', tags=['calculator'])

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", PORT))
    host = "0.0.0.0" if os.environ.get("ENVIRONMENT") == "production" else SERVER_URL
    uvicorn.run("main:app", host=host, port=port, reload=(ENV == "dev"))