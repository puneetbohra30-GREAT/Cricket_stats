from pydantic import BaseModel

class MatchBase(BaseModel):
    team1: str
    team2: str
    score: str
    status: str

class MatchResponse(MatchBase):
    id: int

    class Config:
        orm_mode = True