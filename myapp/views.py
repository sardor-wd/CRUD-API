from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CalendarEvent
import json

@csrf_exempt
def get_events(request):
    events = CalendarEvent.objects.all()
    data = []
    for event in events:
        data.append({
            'id': event.id,
            'title': event.title,
            'date': event.date.strftime('%Y-%m-%d'),
            'time': event.time.strftime('%H:%M')
        })
    return JsonResponse(data, safe=False)


@csrf_exempt
def create_event(request):
    data = json.loads(request.body)
    event = CalendarEvent(
        title=data['title'],
        date=data['date'],
        time=data['time']
    )
    event.save()
    return JsonResponse({'message': 'Event created successfully'})


@csrf_exempt
def delete_event(request, event_id):
    event = get_object_or_404(CalendarEvent, pk=event_id)
    event.delete()
    return JsonResponse({'message': 'Event deleted successfully'})


@csrf_exempt
def update_event(request, event_id):
    if request.method == 'PUT':
        event = CalendarEvent.objects.filter(id=event_id).first()

        if not event:
            return JsonResponse({'message': 'Event not found'})

        data = json.loads(request.body)
        title = data.get('title', event.title)
        date = data.get('date', event.date)
        time = data.get('time', event.time)

        event.title = title
        event.date = date
        event.time = time
        event.save()

        return JsonResponse({'message': 'Event updated successfully'})

    return JsonResponse({'message': 'Invalid request method'})

