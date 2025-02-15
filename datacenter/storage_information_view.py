from datacenter.models import Passcard, Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from .utils import format_duration

def storage_information_view(request):
    non_closed_visits = []
    active_visits = Visit.objects.filter(leaved_at__isnull=True)

    for visit in active_visits:
        duration = visit.get_duration()
        formatted_duration = format_duration(duration)
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at).strftime('%Y-%m-%d %H:%M:%S'),
            'duration': formatted_duration,
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)