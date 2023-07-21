from django.shortcuts import render
from django.http import HttpResponse
from event.models import Event
from schedule.models import Schedule
from speaker.models import Speaker
from django.db.models import Sum
from payment.models import Payment
from .forms import EventForm

def all_events_view(request):
    events = Event.objects.all()
    print("EV 1", events[0].title, events[0].start_date)

    return render(request, 'event/events.html', context={"events": events})

def one_event_view(request, title):
    event = Event.objects.get(title=title)
    return render(request, 'event/event.html', context={"event": event})

def schedules_of_specific_event(request, id):
    eventId = int(id)
    schedules= Schedule.objects.filter(event_id=eventId)
    for schedule in schedules:
        print(schedule.id, schedule.topic, schedule.event_id)
    return HttpResponse("Schedules")

def list_of_free_events(request):
    events = Event.objects.filter(is_free='True')
    for event in events:
        print("****** FREE EVENT *******", event.title, " # ", event.is_free)
    return HttpResponse("FREE Events")

def list_of_paid_events(request):
    events = Event.objects.filter(is_free='False')
    for event in events:
        print("****** PAID EVENT *******", event.title, " # ", event.is_free)
    return HttpResponse("PAID Events")

def speaker_of_specific_event(request, id):
    eventId = int(id)
    speakers = ''
    schedules=Schedule.objects.filter(event_id=eventId)
    for schedules in schedules:
        speakers = speakers + ' ' +   str(schedules.speaker) + ', '
        print( "speaker of specific event", schedules.speaker)
    return HttpResponse("speakers: " + speakers )

def total_amount_paid_for_specific_event(request, id):
    eventId = int(id)
    event = Event.objects.get(id=eventId)
    sum = Payment.objects.filter(event_id=eventId).aggregate(Sum('amount_paid'))
    return HttpResponse('Total amount paid for event, ' + event.title + ' is ' + str(sum['amount_paid__sum']))

def add_event_view(request):
    try:
        pass
    except:
        pass
    if request.method == 'POST':
        form = EventForm()
        if form.is_valid:
            newEvent = form.save(commit=False)
            newEvent.is_free = False
            newEvent.start_date = request.POST['start_date']
            newEvent.category_id = int(request.POST['category'])
            newEvent.title = request.POST['title']
            newEvent.location = request.POST['location']
            newEvent.description = request.POST['description']
            newEvent.end_date = request.POST['end_date']
            if request.POST['start_date'] == 'on':
                newEvent.is_free = False
            newEvent.save()
            return render(request, 'event/successFormSubmission.html', context={"title": newEvent.title, "description":newEvent.description, "category": newEvent.category_id, "end_date": newEvent.end_date, "entrance": newEvent.is_free, "start_date": newEvent.start_date, "location": newEvent.location  })
    form = EventForm()
    context={"form": form }
    return render(request, 'event/addEventForm.html', context)
