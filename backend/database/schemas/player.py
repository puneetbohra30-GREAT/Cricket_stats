from pydantic import BaseModel


class PlayerBase(BaseModel):
    name: str
    team: str


class PlayerCreate(PlayerBase):
    runs: int = 0
    matches_played: int = 0


class PlayerResponse(PlayerBase):
    id: int
    runs: int

    class Config:
        from_attributes = True