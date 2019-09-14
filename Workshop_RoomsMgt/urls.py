from django.urls import path, re_path
# prework:
from .views import preparing_rooms, preparing_rooms2, preparing_rooms3
# Workshop:
from .views import rooms, add_room, modify_room, delete_room, room_detail, reservation, reservation_select


# Main paths for Workshop 3 Rooms Mgt:

urlpatterns = [
    path('room/', rooms, name="rooms"),
    path('room/new', add_room, name="new"),
    path('room/modify/<int:pk>', modify_room, name="modify"),
    path('room/delete/<int:pk>', delete_room, name="delete"),
    path('room/reservation/<int:pk>', reservation, name="reservation"),
    path('room/reservation/', reservation_select, name="reservation_select"),
    path('room/<int:pk>', room_detail, name="room"),
    path('preparing_rooms/', preparing_rooms, name="preparation"),
    path('preparing_rooms2/', preparing_rooms2, name="preparation2"),
    path('preparing_rooms3/', preparing_rooms3, name="preparation2"),

]

