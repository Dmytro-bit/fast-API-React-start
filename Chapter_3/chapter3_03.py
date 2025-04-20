from datetime import datetime


def format_date(dt: datetime) -> str:
    """:return time format 2025-04-31 22:12:12"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


now = datetime.now()

print(format_date(now))
