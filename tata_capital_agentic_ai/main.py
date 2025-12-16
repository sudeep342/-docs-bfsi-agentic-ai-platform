from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from pathlib import Path
from agents.master_agent import master_agent_flow

app = FastAPI()

class LoanRequest(BaseModel):
    phone: str
    amount: int


@app.post("/chat")
def chat(req: LoanRequest):
    return master_agent_flow(req.phone, req.amount)


@app.get("/")
def root():
    file_path = Path(__file__).parent / "response.html"
    if file_path.exists():
        return FileResponse(str(file_path), media_type="text/html")
    return {"detail": "response.html not found"}