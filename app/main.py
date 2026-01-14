from fastapi import FastAPI

app = FastAPI(title="AI Application Engineer Journey")

@app.get("/")

def root():
    return {"message": "AI Application Engineer Journey Started"}