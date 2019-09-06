from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
import datetime


# using module from django:
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )


from .models import Room, Reservation


def preparing_rooms(request):
    Room.objects.create(
        name="Chłopicki",
        capacity=65,
        projector_availability=True,
    )
    Room.objects.create(
        name="Wysocki",
        capacity=30,
        projector_availability=True,
    )
    Room.objects.create(
        name="Skrzynecki",
        capacity=50,
        projector_availability=True,
    )
    Room.objects.create(
        name="Małachowski",
        capacity=75,
        projector_availability=False,
    )
    Room.objects.create(
        name="Rybiński",
        capacity=25,
        projector_availability=False,
    )
    Room.objects.create(
        name="Radziwił",
        capacity=20,
        projector_availability=False,
    )
    return_str = "Dodano!"
    return HttpResponse(return_str)

def preparing_rooms2(request):

    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=2),
    )
    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=3),
    )
    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=4),
    )
    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=5),
    )
    Reservation.objects.create(
        date=datetime.date.today(),
        comment="Konferencja",
        rooms=Room.objects.get(id=6),
    )
    return_str = "Dodano!"
    return HttpResponse(return_str)

def preparing_rooms3(request):

    Reservation.objects.create(
        date="2019-09-08",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date="2019-09-03",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date="2019-09-02",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date="2019-09-01",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date="2019-09-18",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    Reservation.objects.create(
        date="2019-09-28",
        comment="Konferencja",
        rooms=Room.objects.get(id=1),
    )
    return_str = "Dodano!"
    return HttpResponse(return_str)

# widok wszystkich pokoii:
def rooms(request):
    context = {
        'Room': Room.objects.all(),
        'Reservation': Reservation.objects.all(),
        'now': datetime.date.today()
    }
    return render(request, 'Workshop_RoomsMgt/rooms.html', context)

# dodanie nowego pokoju:
def add_room(request):
    if request.method == "GET":
        return render(request, 'Workshop_RoomsMgt/add_room.html')
    if request.method == "POST":
        N = request.POST['Name']
        print(N)
        C = int(request.POST['Capacity'])
        print(C)
        py = request.POST['projector_availability']
        print(py)
        pa = False
        if py == "True":
            pa = True
        else:
            pa = False
        Room.objects.create(name=N, capacity=C, projector_availability=pa)
        messages.success(request, 'Your room has been added sucessfully! ')
        return redirect('room')

# Szczegóły danego pokoju - wersja z wykorzystanie url to przekazywania zapytania GET.
# Reserwacje filtrowane po dacie i przekazywane do strony.
def room_detail(request, pk):
    if request.method == 'GET':
        today = datetime.date.today()
        r = Reservation.objects.filter(rooms=Room.objects.get(pk=pk)).filter(date__gte=today).order_by('date')
        context = {
            'Room': Room.objects.get(pk=pk),
            'Reservation': r
        }
        return render(request, 'Workshop_RoomsMgt/room_detail.html', context)


# Modyfikacja wybranej sali, widoczne stare wartości.
def modify_room(request, pk):
    N = ""
    C = 0
    pa = False
    if request.method == "GET":
        context = {
            'Room': Room.objects.get(pk=pk)
        }
        return render(request, 'Workshop_RoomsMgt/modify_room.html', context)
    if request.method == "POST":
        N = request.POST['Name']
        C = int(request.POST['Capacity'])
        py = request.POST['projector_availability']
        if py == "True":
            pa = True
        else:
            pa = False
    edited_room = Room.objects.get(pk=pk)
    edited_room.name = N
    edited_room.capacity = C
    edited_room.projector_availability = pa
    edited_room.save()
    messages.success(request, 'Your room has been modified sucessfully! ')
    return redirect('rooms')

# Usunięcie wybranej sali, upewnianie się czy użytkownik tego chce.
def delete_room(request, pk):
    if request.method == "GET":
        context = {
            'Room': Room.objects.get(pk=pk)
        }
        return render(request, 'Workshop_RoomsMgt/delete_room.html', context)
    if request.method == "POST":
        deleted_room = Room.objects.get(pk=pk)
        deleted_room.delete()
        messages.success(request, 'Your room has been modified sucessfully! ')
        return redirect('rooms')

# reservation of specific room direct from specific room detail or genenral view room details.
def reservation(request, pk):
    if request.method == "GET":
        context = {
            'Room': Room.objects.get(pk=pk)
        }
        return render(request, 'Workshop_RoomsMgt/reservation.html', context)
    if request.method == "POST":
        dates = request.POST['date']
        comments = request.POST['comment']
        Reservation.objects.create(
            date=dates,
            comment=comments,
            rooms=Room.objects.get(pk=pk),
        )
        messages.success(request, 'Your reservation has been added sucessfully! ')
        return redirect('rooms')

# Generalny widok do dodawania rezerwacji na każdej sali.
def reservation_select(request):
    if request.method == "GET":
        context = {
            'Room': Room.objects.all()
        }
        return render(request, 'Workshop_RoomsMgt/reservation_select.html', context)
    if request.method == "POST":
        PK = int(request.POST['rooms'])
        print(PK)
        dates = request.POST['date']
        print(dates)
        comments = request.POST['comment']
        print(comments)
        room = Room.objects.get(pk=PK)
        print(room.name)
        Reservation.objects.create(
            date=dates,
            comment=comments,
            rooms=Room.objects.get(pk=PK),
        )
        messages.success(request, 'Your reservation has been added sucessfully! ')
        return redirect('rooms')