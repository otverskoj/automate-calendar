import json
from typing import Optional, Sequence, Any, Dict

import requests
from pydantic import BaseModel


__all__ = [
    'Lesson',
    'get_term_id',
    'get_schedule_json',
    'get_schedule_as_lessons'
]


class Lesson(BaseModel):
    auditorium: str
    beginLesson: str
    building: str
    date: str
    dayOfWeek: int
    dayOfWeekString: str
    discipline: str
    endLesson: str
    kindOfWork: str
    lecturer: str


def get_term_id(term: str, term_type: str) -> int:
    url = f'https://rasp.omgtu.ru/api/search?term={term}&type={term_type}'
    return json.loads(requests.get(url).text)[0]['id']


def get_schedule_json(
    term_type: str,
    term_id: int,
    date_start: Optional[str] = None,
    date_finish: Optional[str] = None
) -> Sequence[Dict[str, Any]]:
    url = f'https://rasp.omgtu.ru/api/schedule/{term_type}/{term_id}"?start={date_start}&finish={date_finish}&lng=1'
    return json.loads(requests.get(url).text)


def get_schedule_as_lessons(
    term_type: str,
    term_id: int,
    date_start: Optional[str] = None,
    date_finish: Optional[str] = None
) -> Sequence[Lesson]:
    schedule = get_schedule_json(
        term_type=term_type,
        term_id=term_id,
        date_start=date_start,
        date_finish=date_finish
    )

    return [
        Lesson(**elem)
        for elem in schedule
    ]
