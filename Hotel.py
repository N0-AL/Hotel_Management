from RoomManagement import *
import random


def setup_rooms():
    rooms = []
    room_num = 1
    count = int(input("How many rooms do you want to start with: "))
    while room_num <= count:
        room_capacity = random.randint(1, 50)
        room_availability = random.choice([True, False])
        room = {
            "number": room_num,
            "capacity": room_capacity,
            "availability": room_availability
        }
        rooms.append(room)
        room_num = room_num + 1
    return rooms


def main():

    rooms = setup_rooms()
    while True:
        print("1 = add reservation / 2 = remove reservation \n",
              "3 = list available / 4 = list unavailable \n",
              "5 = check room / 6 = show capacity / 7 = exit")
        choice = input("check what rooms we have and choose what option you are going to go with: ")
        print()
        if choice == "1":
            add_reservation(rooms)
        elif choice == "2":
            remove_reservation(rooms)
        elif choice == "3":
            list_available(rooms)
        elif choice == "4":
            list_unavailable(rooms)
        elif choice == "5":
            check_room(rooms)
        elif choice == "6":
            capacity_stats(rooms)
        elif choice == "7":
            exit("you closed the program")


main()
