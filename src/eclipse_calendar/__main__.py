from .calendar import create_calendar_from_records
from .data import get_catalog, process_catalog


def main():
    records = process_catalog(get_catalog())
    create_calendar_from_records(records)


if __name__ == "__main__":
    main()
