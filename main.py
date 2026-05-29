from fastapi import FastAPI

app = FastAPI()


@app.get("/hello")
def hello():
    return {"message": "Hello and welcome!"}


@app.get("/goodbye")
def goodbye():
    return {"message": "Goodbye!"}
