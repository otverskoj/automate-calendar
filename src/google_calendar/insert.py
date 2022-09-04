from typing import Any, Mapping

from src.google_calendar.event import Event
from src.google_calendar.setup import CalendarService


def insert_event(
    service: CalendarService,
    event: Event,
    calendar_id: str = 'primary'
) -> Mapping[str, Any]:
    body = event.dict(by_alias=True)
    return service.events().insert(
        calendarId=calendar_id,
        body=body
    ).execute()
