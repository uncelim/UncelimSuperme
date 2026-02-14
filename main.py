from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"durum": "Sistem Aktif", "operator": "Uncelim Supreme"}
