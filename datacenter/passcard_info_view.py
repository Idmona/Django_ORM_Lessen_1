from datacenter.models import Passcard, Visit
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import localtime
from .utils import format_duration
from datetime import timedelta


def is_visit_long(visit):
    duration = visit.get_duration()
    return duration > timedelta(hours=1)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)

    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = visit.get_duration()
        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit)
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
