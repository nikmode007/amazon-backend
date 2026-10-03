from fastapi import FastAPI


from app.database.connection_db import Base, engine
from app.routes.Vender_routes import router
from app.routes.User_routes import routers
from app.routes.Admin_routes import routersAdmin




Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Vender API",
    version="1.0"
)

app.include_router(router)
app.include_router(routers)
app.include_router(routersAdmin)



@app.get("/")
def home():

    return {
        "message": "FastAPI + MySQL MVC Application"
    }