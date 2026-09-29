from fastapi import FastAPI


from app.database.connection import Base, engine
from app.routes.Vender_routes import router


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Vender API",
    version="1.0"
)

class vender(Base):
    name: str
    email: str
    age: int



app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "FastAPI + MySQL MVC Application"
    }