from fastapi import FastAPI
from app.database import init_db
from app.routes import products, categories, users

app = FastAPI(title="Jewelry App API", version="1.0.0")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(products.router)
app.include_router(categories.router)
app.include_router(users.router)

@app.get("/")
def root():
    return {"message": "Jewelry App API is running!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)