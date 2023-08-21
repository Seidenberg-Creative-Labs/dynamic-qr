from fastapi import FastAPI
print("i'm inside of main.py")

app = FastAPI()

@app.get("/")
def test():
    return {"message":"Hello World"}