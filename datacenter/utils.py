SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours, remainder = divmod(total_seconds, SECONDS_IN_HOUR)
    minutes, seconds = divmod(remainder, SECONDS_IN_MINUTE)
    return f"{hours}:{minutes:02d}:{seconds:02d}"
