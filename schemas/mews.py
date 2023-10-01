from typing import List, Optional

from pydantic import BaseModel, Field


class MewsRoom(BaseModel):
    """Message model for Mews Room data."""
    room_number: str = Field(..., alias="RoomNumber")
    room_id: str = Field(..., alias="RoomId")
    room_name: str = Field(..., alias="RoomName")
    room_description: str = Field(..., alias="RoomDescription")
    status: str = Field(..., alias="Status")
    is_cleaning_required: bool = Field(..., alias="IsCleaningRequired")
    is_cleaning_in_progress: bool = Field(..., alias="IsCleaningInProgress")
    is_cleaning_finished: bool = Field(..., alias="IsCleaningFinished")


class MewsData(BaseModel):
    """Base model for Mews data."""

    id: str = Field(..., alias="Id")
    name: str = Field(..., alias="Name")
    description: str = Field(..., alias="Description")
    rooms: List[MewsRoom] = Field(..., alias="Rooms")
    is_active: Optional[bool] = Field(..., alias="IsActive")
