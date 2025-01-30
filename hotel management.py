class Room:
    def __init__(self, room_number, room_type, price, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = is_available
        self.guest_name = None

    def book_room(self, guest_name):
        if self.is_available:
            self.is_available = False
            self.guest_name = guest_name
            print(f"Room {self.room_number} booked successfully for {guest_name}!")
        else:
            print(f"Sorry, Room {self.room_number} is already booked.")

    def checkout(self):
        if not self.is_available:
            print(f"Guest {self.guest_name} has checked out from Room {self.room_number}.")
            self.is_available = True
            self.guest_name = None
        else:
            print(f"Room {self.room_number} is already vacant.")

    def display_details(self):
        status = "Available" if self.is_available else f"Booked by {self.guest_name}"
        print(f"Room {self.room_number} | Type: {self.room_type} | Price: ${self.price:.2f} | Status: {status}")


class Hotel:
    def __init__(self):
        self.rooms = {
            101: Room(101, "Single", 50),
            102: Room(102, "Double", 80),
            103: Room(103, "Suite", 150),
            104: Room(104, "Single", 50),
            105: Room(105, "Suite", 150)
        }

    def view_rooms(self):
        print("\n--- Room Availability ---")
        for room in self.rooms.values():
            room.display_details()

    def book_room(self):
        room_number = int(input("Enter room number to book: "))
        if room_number in self.rooms:
            if self.rooms[room_number].is_available:
                guest_name = input("Enter guest name: ")
                self.rooms[room_number].book_room(guest_name)
            else:
                print("Room is already booked!")
        else:
            print("Invalid room number!")

    def checkout_guest(self):
        room_number = int(input("Enter room number for checkout: "))
        if room_number in self.rooms:
            self.rooms[room_number].checkout()
        else:
            print("Invalid room number!")

    def run(self):
        while True:
            print("\n--- Hotel Management System ---")
            print("1. View Rooms")
            print("2. Book a Room")
            print("3. Checkout")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.view_rooms()
            elif choice == "2":
                self.book_room()
            elif choice == "3":
                self.checkout_guest()
            elif choice == "4":
                print("Thank you for using the Hotel Management System!")
                break
            else:
                print("Invalid choice! Please try again.")


if __name__ == "__main__":
    hotel = Hotel()
    hotel.run()
