from fastapi import FastAPI
from api.routes.search import router
from fastapi.middleware.cors import CORSMiddleware
from download_data import ensure_data
ensure_data()



app = FastAPI()
app.include_router(router)



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)