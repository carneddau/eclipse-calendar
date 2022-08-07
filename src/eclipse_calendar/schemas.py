from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class EclipseSubType(str, Enum):
    M = "m"
    N = "n"
    S = "s"
    PL = "+"
    MI = "-"
    TW = "2"
    TH = "3"
    B = "b"
    E = "e"


class EclipseType(str, Enum):
    P = "P"
    A = "A"
    T = "T"
    H = "H"


TYPE_TO_SUMMARY: dict[EclipseType, str] = {
    EclipseType.P: "Partial",
    EclipseType.A: "Annular",
    EclipseType.T: "Total",
    EclipseType.H: "Hybrid",
}

SUB_TYPE_TO_SUMMARY: dict[EclipseSubType, str] = {
    EclipseSubType.M: "Middle eclipse of Saros series",
    EclipseSubType.N: "Central eclipse with no northern limit",
    EclipseSubType.S: "Central eclipse with no southern limit",
    EclipseSubType.PL: "Non-central eclipse with no northern limit",
    EclipseSubType.MI: "Non-central eclipse with no southern limit",
    EclipseSubType.TW: "Hybrid path begins total and ends annular",
    EclipseSubType.TH: "Hybrid path begins annular and ends total",
    EclipseSubType.B: "Saros series begins (first eclipse in series)",
    EclipseSubType.E: "Saros series ends (last eclipse in series)",
}


class CatalogRecord(BaseModel):
    eclipse_date: date
    type: EclipseType
    sub_type: Optional[EclipseSubType]
    lat: str
    lon: str
