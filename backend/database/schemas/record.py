from pydantic import BaseModel


class MatchBase(BaseModel):
    team1: str
    team2: str
    venue: str


class MatchCreate(MatchBase):
    date: str


class MatchResponse(MatchBase):
    id: int
    score_team1: str
    score_team2: str

    class Config:
        from_attributes = True