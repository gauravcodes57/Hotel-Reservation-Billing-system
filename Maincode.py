rooms = {
    "101": ["Single", 1200, 1, "No", "Single Bed", "Garden View", "Available"],
    "102": ["Single", 1200, 1, "No", "Single Bed", "Garden View", "Available"],
    "103": ["Double", 1800, 2, "Yes", "Queen Bed", "City View", "Available"],
    "104": ["Double", 1800, 2, "Yes", "Queen Bed", "City View", "Available"],
    "105": ["Deluxe", 2500, 2, "Yes", "King Bed", "Garden View", "Available"],
    "106": ["Suite", 3500, 3, "Yes", "King Bed", "Premium View", "Available"]
}

booking = {}
services = []


def show_rooms():
    print("\n" + "=" * 65)
    print(f"{'AVAILABLE ROOMS':^65}")
    print("=" * 65)
    # Using fixed character widths (<8, <12, etc.) so columns never shift out of line
    print(f"{'Room':<8}{'Type':<12}{'Price/Night':<15}{'Max Guests':<12}{'Status'}")
    print("-" * 65)

    for room in rooms:
        if rooms[room][6] == "Available":
            print(f"{room:<8}{rooms[room][0]:<12}Rs. {rooms[room][1]:<11}{rooms[room][2]:<12}Available")


def select_room():
    while True:
        choice = input("\nEnter room number or room type: ").strip().lower()

        # 1. Check if user typed an exact room number
        if choice in rooms:
            if rooms[choice][6] == "Available":
                return choice
            print("This room is already booked.")

        # 2. If not a room number, search for matching available room types
        else:
            found_rooms = []
            for room in rooms:
                if rooms[room][0].lower() == choice and rooms[room][6] == "Available":
                    found_rooms.append(room)

            if found_rooms:
                if len(found_rooms) == 1:
                    return found_rooms[0]
                
                # If multiple rooms match the type, let them pick the exact room number
                print(f"Available rooms of type '{choice.capitalize()}': {', '.join(found_rooms)}")
                room_choice = input("Please specify the exact room number: ").strip()
                if room_choice in found_rooms:
                    return room_choice
                print("Invalid room selection.")
            else:
                print("Room or available room type not found.")


def show_details(room):
    print("\n" + "=" * 65)
    print(f"{'ROOM DETAILS':^65}")
    print("=" * 65)
    print("Room       :", room)
    print("Type       :", rooms[room][0])
    print("Price      : Rs.", rooms[room][1], "per night")
    print("Max Guests :", rooms[room][2])
    print("Bed        :", rooms[room][4])
    print("Balcony    :", rooms[room][3])
    print("View       :", rooms[room][5])
    print("Facilities : AC, Wi-Fi, Smart TV, Attached Bathroom")


def book_room():
    show_rooms()
    room = select_room()
    show_details(room)

    choice = input("\nSelect this room? (yes/no): ").strip().lower()

    if choice != "yes":
        return book_room()

    name = input("\nEnter primary guest name: ").strip()
    phone = input("Enter contact number: ").strip()

    # Dynamic guest handling: Allows solo travelers in multi-person rooms
    max_guests = rooms[room][2]
    while True:
        try:
            num_guests = int(input(f"Enter total number of staying guests (Max {max_guests}): "))
            if 1 <= num_guests <= max_guests:
                break
            print(f"Invalid entry. This room can accommodate between 1 and {max_guests} guests.")
        except ValueError:
            print("Please enter a valid number.")

    guests = [name]
    for i in range(1, num_guests):
        guests.append(input(f"Enter guest {i + 1} name: ").strip())

    while True:
        try:
            nights = int(input("Enter number of nights: "))
            if nights > 0:
                break
            print("Number of nights must be 1 or more.")
        except ValueError:
            print("Please enter a valid number.")

    booking["room"] = room
    booking["name"] = name
    booking["phone"] = phone
    booking["guests"] = guests
    booking["nights"] = nights

    rooms[room][6] = "Booked"


def choose_services():
    print("\n1. Breakfast - Rs.250")
    print("2. Food - Rs.300")
    print("3. Laundry - Rs.200")
    print("4. Room Service - Rs.150")
    print("5. Finish")

    while True:
        choice = input("\nEnter service number or name: ").strip().lower()

        if choice == "1" or choice == "breakfast":
            services.append(["Breakfast", 250])
            print("Breakfast added.")
        elif choice == "2" or choice == "food":
            services.append(["Food", 300])
            print("Food added.")
        elif choice == "3" or choice == "laundry":
            services.append(["Laundry", 200])
            print("Laundry added.")
        elif choice == "4" or choice == "room service":
            services.append(["Room Service", 150])
            print("Room service added.")
        elif choice == "5" or choice == "finish":
            break
        else:
            print("Invalid choice.")


def bill():
    room = booking["room"]

    room_charge = rooms[room][1] * booking["nights"]
    service_charge = 0

    for service in services:
        service_charge += service[1]

    subtotal = room_charge + service_charge
    gst = subtotal * 0.18
    total = subtotal + gst

    print("\n" + "=" * 65)
    print(f"{'FINAL BILL':^65}")
    print("=" * 65)
    print("Guest       :", booking["name"])
    print("Room        :", room)
    print("Room Type   :", rooms[room][0])
    print("Nights      :", booking["nights"])
    print("Room Charge : Rs.", room_charge)
    print("Services    : Rs.", service_charge)
    print("Subtotal    : Rs.", subtotal)
    print("GST (18%)   : Rs.", round(gst, 2))
    print("-" * 65)
    print("TOTAL       : Rs.", round(total, 2))
    print("=" * 65)

    return total


# --- SYSTEM INITIATION ---
print("\n" + "=" * 65)
print(f"{'THE GRAND AURELIA HOTEL':^65}")
print(f"{'RESERVATION SYSTEM':^65}")
print("=" * 65)

book_room()

choice = input("\nAdd hotel services? (yes/no): ").strip().lower()
if choice == "yes":
    choose_services()

choice = input("\nAny special request? (yes/no): ").strip().lower()
if choice == "yes":
    booking["request"] = input("Enter request: ").strip()
else:
    booking["request"] = "None"

total = bill()

print("\nPayment Method")
print("1. Cash")
print("2. UPI")
print("3. Card")

while True:
    payment = input("Select number or enter method: ").strip().lower()

    if payment == "1" or payment == "cash":
        payment = "Cash"
        break
    elif payment == "2" or payment == "upi":
        payment = "UPI"
        break
    elif payment == "3" or payment == "card":
        payment = "Card"
        break
    else:
        print("Invalid choice.")

print("\n" + "=" * 65)
print(f"{'BOOKING CONFIRMATION':^65}")
print("=" * 65)
print("Guest          :", booking["name"])
print("Room           :", booking["room"])
print("Total Amount   : Rs.", round(total, 2))
print("Payment Method :", payment)
print("Special Request:", booking["request"])

choice = input("\nConfirm booking? (yes/no): ").strip().lower()

if choice == "yes":
    print("\nBooking confirmed.")
    print("Thank you for choosing The Grand Aurelia Hotel.")
else:
    rooms[booking["room"]][6] = "Available"
    print("\nBooking cancelled.")