from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/event")
async def receive_event(request: Request):
    data = await request.json()
    print(f"Andy received: {data}")
    return {"status": "ok"}