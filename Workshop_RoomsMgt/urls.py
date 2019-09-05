from django.urls import path, re_path
# prework:
from .views import preparing_rooms
# Workshop:
from .views import rooms, add_room, modify_room, delete_room, room_detail



# Main paths for Workshop 3 Rooms Mgt:

urlpatterns = [
    path('rooms/', rooms, name="rooms"),
    path('room/new', add_room, name="new"),
    path('room/modify/{id}', modify_room, name="modify"),
    path('room/delete/{id}', delete_room, name="delete"),
    path('room/{id}', room_detail, name="room"),
    path('preparing_rooms/', preparing_rooms, name="preparation"),

]

