from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages



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

# widok wszystkich pokoii:
def rooms(request):
    context = {
        'Room': Room.objects.all()
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
        return redirect('rooms')


def modify_room(request):
    context = {
        'Room': Room.objects.all()
    }
    return render(request, 'Workshop_RoomsMgt/rooms.html', context)


def delete_room(request):
    context = {
        'Room': Room.objects.all()
    }
    return render(request, 'Workshop_RoomsMgt/rooms.html', context)


def room_detail(request):
    context = {
        'Room': Room.objects.all()
    }
    return render(request, 'Workshop_RoomsMgt/rooms.html', context)