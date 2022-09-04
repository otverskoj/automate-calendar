from typing import Optional, List
from datetime import datetime

from pydantic import BaseModel, Field


class EventDateTime(BaseModel):
    date_time: str = Field(datetime.now().isoformat(), alias='dateTime')
    time_zone: str = Field('Asia/Omsk', alias='timeZone')


class AttendeeEmail(BaseModel):
    email: str


class ReminderMethod(BaseModel):
    method: str = 'popup'  # 'email'
    minutes: int = 24 * 60


class Reminder(BaseModel):
    use_default: bool = Field(True, alias='useDefault')
    overrides: Optional[List[ReminderMethod]] = None


class Event(BaseModel):
    summary: str
    location: Optional[str] = None
    description: Optional[str] = None
    start: EventDateTime
    end: EventDateTime
    recurrence: Optional[List[str]] = None  # ['RRULE:FREQ=DAILY;COUNT=2']
    attendees: Optional[List[AttendeeEmail]] = None
    reminders: Optional[Reminder] = None
