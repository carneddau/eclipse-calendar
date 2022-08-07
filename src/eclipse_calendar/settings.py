from functools import cache

from pydantic import BaseSettings, Field, HttpUrl


class Settings(BaseSettings):
    log_level: str = "ERROR"
    catalog_url: HttpUrl = Field(
        default="https://eclipse.gsfc.nasa.gov/5MCSE/5MCSEcatalog.txt"
    )
    catalog_header_lines: int = 10
    start_year: int = 2000
    end_year: int = 2100
    separate_output: bool = True

    class Config:
        env_file = ".env"


@cache
def get_settings():
    return Settings()
