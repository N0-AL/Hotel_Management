def remove_reservation(rooms):
    room_remove = int(input("choose a room number to remove from: "))
    for room in rooms:
        if room["number"] == room_remove:
            if not room["availability"]:
                room["availability"] = True
                print(f"room number {room_remove} has been removed from you")
                print()
            else:
                print(f"room number {room_remove} in unavailable")
                print()
            return


def list_available(rooms):
    for room in rooms:
        if room["availability"]:
            print("room number", room["number"], "is available")
    print()


def list_unavailable(rooms):
    for room in rooms:
        if not room["availability"]:
            print("room number", room["number"], "is unavailable")
    print()


def check_room(rooms):
    select_room = int(input("type in a room number to see specifics: "))
    for room in rooms:
        if room['number'] == select_room:
            print(room)
            print()
    if select_room != rooms:
        print("room doesnt exist")
        print()


def capacity_stats(rooms):
    total_capacity = 0
    available = 0
    unavailable = 0
    for room in rooms:
        total = 50 * room['number']
        total_capacity = total_capacity + room['capacity']
        available = total - total_capacity
        unavailable = total_capacity - available
    print(f"there is {total_capacity} spaces in total")
    print(f"{available} of the spaces are open")
    print(f"{unavailable} of the spaces are taken")
    print()


def add_reservation(rooms):
    room_ask = int(input("choose a room number to reserve: "))
    for room in rooms:
        if room["number"] == room_ask:
            if room["availability"]:
                room["availability"] = False
                print(f"room number {room_ask} has been reserved")
                print()
            else:
                print(f"room number {room_ask} in unavailable")
                print()
            return
