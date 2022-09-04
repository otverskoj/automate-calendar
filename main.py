from datetime import datetime
from pprint import pprint

from src.google_calendar.event import Event
from src.google_calendar.insert import insert_event
from src.google_calendar.setup import calendar_setup
from src.parse_omstu_rasp import get_term_id, get_schedule_as_lessons


def main() -> None:
    term = 'ФИТм-221'
    term_type = 'group'

    date_start = '2022.09.01'
    date_finish = '2023.01.15'

    term_id = get_term_id(term=term, term_type=term_type)

    lessons = get_schedule_as_lessons(
        term_type=term_type,
        term_id=term_id,
        date_start=date_start,
        date_finish=date_finish
    )

    service = calendar_setup(
        creds_path='src/credentials/credentials.json'
    )
    dt_format = "%Y.%m.%d %H:%M"

    for lesson in lessons:
        raw_dt_start = f"{lesson.date} {lesson.beginLesson}"
        raw_dt_end = f"{lesson.date} {lesson.endLesson}"

        dt_start = datetime.strptime(raw_dt_start, dt_format)
        dt_end = datetime.strptime(raw_dt_end, dt_format)

        event_payload = {
            'summary': f'{lesson.discipline} {lesson.auditorium}',
            'description': f'{lesson.kindOfWork} {lesson.lecturer}',
            'start': {
                'dateTime': dt_start.isoformat(),
                'timeZone': 'Asia/Omsk',
            },
            'end': {
                'dateTime': dt_end.isoformat(),
                'timeZone': 'Asia/Omsk',
            }
        }

        event = Event(**event_payload)

        try:

            insert_event(
                service=service,
                event=event
            )
        except Exception as e:
            pprint(e)


if __name__ == '__main__':
    main()
