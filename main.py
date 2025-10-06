# ...existing code...
from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

l = {
    "1": "apple",
    "2": "banana",
    "3": "grape",
    "4": "orange",
    "5": "mango"
}


@app.get("/getlist/")
def get_list():
    return l


@app.get("/Rehan/")
def hello_rehan():
    return {"Hello": "Rehan"}


@app.post("/postList/")
async def post_list(request: Request):
    # parse JSON body if possible, otherwise try to decode raw bytes
    try:
        data = await request.json()
    except Exception:
        raw = await request.body()
        try:
            data = {"item": raw.decode("utf-8")}
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid request body")

    if not isinstance(data, dict) or "item" not in data:
        raise HTTPException(status_code=400, detail="JSON body must be an object with an 'item' key")

    new_id = str(len(l) + 1)
    l[new_id] = data["item"]

    # print full request info for debugging (will appear in the server terminal/log)
    print({
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "query_params": dict(request.query_params),
        "path_params": dict(request.path_params),
        "client": {
            "host": request.client.host if request.client else None,
            "port": request.client.port if request.client else None,
        },
        "body": data,
    })

    return {"id": new_id, "item": l[new_id]}
# ...existing code...