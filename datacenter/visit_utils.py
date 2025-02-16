from datetime import timedelta

MAX_VISIT_DURATION = timedelta(hours=1)


def is_visit_long(visit):
    duration = visit.get_duration()
    MAX_VISIT_DURATION = timedelta(hours=1)
    return duration > MAX_VISIT_DURATION
