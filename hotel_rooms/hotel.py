from hotel_rooms.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        self.guests += people
        return room.take_room(people)

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number][0]
        self.guests -= room.guests
        return room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]

        result += f"Free rooms: {', '.join(free_rooms)}\n"
        result += f"Taken rooms: {', '.join(taken_rooms)}"

        return result
