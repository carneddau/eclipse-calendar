from datetime import date, datetime
from io import StringIO
from typing import Any, Optional, Tuple

from requests import get

from .schemas import CatalogRecord, EclipseSubType, EclipseType
from .settings import get_settings


def get_catalog() -> str:

    url = get_settings().catalog_url
    response = get(url)

    return response.text


def _date_from_str(eclipse_date: str) -> date:
    input_date_format = "%Y %b %d"
    output_date_format = "%Y-%m-%d"

    eclipse_date_iso_str = datetime.strptime(eclipse_date, input_date_format).strftime(
        output_date_format
    )

    return date.fromisoformat(eclipse_date_iso_str)


def _eclipse_types_from_str(input: str) -> Tuple[EclipseType, Optional[EclipseSubType]]:

    type = EclipseType(input[0])
    sub_type = EclipseSubType(input[1]) if len(input) > 1 else None

    return type, sub_type


def process_catalog(catalog_text: str) -> list[CatalogRecord]:
    settings = get_settings()

    lines = StringIO(catalog_text).readlines()

    records: list[CatalogRecord] = []

    for i, line in enumerate(lines):
        if i < settings.catalog_header_lines:
            continue

        fields = line.split()
        date_fields = fields[2:5]

        year = int(date_fields[0])
        if year < settings.start_year or year > settings.end_year:
            continue

        type, sub_type = _eclipse_types_from_str(fields[9])

        parsed_data: dict[str, Any] = {
            "eclipse_date": _date_from_str(" ".join(date_fields)),
            "lat": fields[12],
            "lon": fields[13],
            "type": type,
            "sub_type": sub_type,
        }

        records.append(CatalogRecord(**parsed_data))
    return records
