from fastapi import FastAPI
from dotenv import dotenv_values
from fastapi.responses import RedirectResponse, PlainTextResponse
import requests
print("i'm inside of main.py")

app = FastAPI()

config = dotenv_values(".env")
BASE_URL = config.get('FB_REALTIME_DB_URL')
print(BASE_URL)

@app.get("/")
def test():
    return {"message":"Hello World"}

@app.get("/{campus}/{room}")
def process(campus:str, room:str):
    slug = f"/{campus.upper()}/{room}"
    URL = BASE_URL+f'?orderBy="slug"&equalTo="{slug}"'
    req = requests.get(URL)
    data = req.json()
    try:
        obj = data.popitem()
        return RedirectResponse(obj[1]['redirectTo'])
    except:
        return PlainTextResponse('Does not exist',status_code=404)