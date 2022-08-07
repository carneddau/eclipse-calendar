from icalendar import Calendar, Event

from eclipse_calendar.settings import get_settings

from .schemas import SUB_TYPE_TO_SUMMARY, TYPE_TO_SUMMARY, CatalogRecord, EclipseType


def create_calendar_from_records(input: list[CatalogRecord]):
    calendars: dict[EclipseType, Calendar] = {
        EclipseType.P: Calendar(),
        EclipseType.A: Calendar(),
        EclipseType.T: Calendar(),
        EclipseType.H: Calendar(),
    }

    for record in input:
        event = Event()

        event.add("dtstart", record.eclipse_date)
        event.add("dtend", record.eclipse_date)
        event.add("location", " ".join([record.lat, record.lon]))
        event.add("summary", f"{TYPE_TO_SUMMARY[record.type]} solar eclipse")

        if record.sub_type is not None:
            event.add("description", SUB_TYPE_TO_SUMMARY[record.sub_type])
        calendars[record.type].add_component(event)

    settings = get_settings()

    if settings.separate_output:
        for type, cal in calendars.items():
            with open(f"Eclipse-{TYPE_TO_SUMMARY[type]}.ics", "wb") as file:
                file.write(cal.to_ical())
    else:
        with open("Eclipse-All.ics", "wb") as file:
            calendar_all = Calendar()
            for cal in calendars.values():
                for event in cal.subcomponents:
                    calendar_all.add_component(event)

            file.write(calendar_all.to_ical())
