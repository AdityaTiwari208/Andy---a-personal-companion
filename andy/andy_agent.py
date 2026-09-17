from fastapi import FastAPI, Request

app = FastAPI()

def andy_reacts_to(event_type: str) -> str:
    reactions = {
        "vscode_save": "Andy looks attentive",
        "vscode_debug_start": "Andy leans in curiously",
        "vscode_debug_end": "Andy relaxes",
        "git_commit": "Andy looks proud",
        "voice_query": "Andy is listening",
    }
    return reactions.get(event_type, f"Andy looks neutral (unknown event: {event_type})")

@app.post("/event")
async def receive_event(request: Request):
    data = await request.json()
    reaction = andy_reacts_to(data.get("type", ""))
    print(f"Event: {data} -> {reaction}")
    return {"status": "ok", "reaction": reaction}