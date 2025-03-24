from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Home Route
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

# About Page
@app.get("/about")
def about():
    return {"info": "This is a basic FastAPI application."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
