# https://www.geeksforgeeks.org/bus-reservation-system-in-c/
class Bus:
    def __init__(self, bus_number, source, destination, total_seats, available_seats, fare):
        self.bus_number = bus_number
        self.source = source
        self.destination = destination
        self.total_seats = total_seats
        self.available_seats = available_seats
        self.fare = fare

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def display_main_menu():
    print("\n=== Main Menu ===")
    print("1. Login")
    print("2. SignUp")
    print("3. Exit")
    return input("Enter your choice: ")


def display_user_menu():
    print("\n=== User Menu ===")
    print("1. Book a Ticket")
    print("2. Cancel a Ticket")
    print("3. Check Bus Status")
    print("4. Logout")
    return input("Enter your choice: ")


def login_user(users, username, password):
    for index, user in enumerate(users):
        if user.username == username and user.password == password:
            return index
    return -1


def sign_up_user(users):
    username = input("Enter new username: ")
    password = input("Enter new password: ")
    
    # Check if the username already exists
    if any(user.username == username for user in users):
        print("Username already exists. Try a different one.")
        return None

    new_user = User(username, password)
    users.append(new_user)
    print(f"Sign-up successful! Welcome, {username}!")
    return len(users) - 1


def book_ticket(buses):
    bus_number = int(input("\nEnter Bus Number: "))
    bus = next((bus for bus in buses if bus.bus_number == bus_number), None)

    if bus:
        seats_to_book = int(input("Enter Number of Seats: "))
        if bus.available_seats < seats_to_book:
            print(f"Sorry, only {bus.available_seats} seats are available.")
        else:
            bus.available_seats -= seats_to_book
            print(f"Booking successful! {seats_to_book} seats booked on Bus Number {bus_number}.")
    else:
        print(f"Bus with Bus Number {bus_number} not found.")


def cancel_ticket(buses):
    bus_number = int(input("\nEnter Bus Number: "))
    bus = next((bus for bus in buses if bus.bus_number == bus_number), None)

    if bus:
        seats_to_cancel = int(input("Enter Number of Seats to Cancel: "))
        booked_seats = bus.total_seats - bus.available_seats

        if seats_to_cancel > booked_seats:
            print("Error: You can't cancel more seats than were booked.")
        else:
            bus.available_seats += seats_to_cancel
            print(f"Cancellation successful! {seats_to_cancel} seats canceled on Bus Number {bus_number}.")
    else:
        print(f"Bus with Bus Number {bus_number} not found.")


def check_bus_status(buses):
    bus_number = int(input("\nEnter Bus Number: "))
    bus = next((bus for bus in buses if bus.bus_number == bus_number), None)

    if bus:
        print(f"\nBus Number: {bus.bus_number}")
        print(f"Source: {bus.source}")
        print(f"Destination: {bus.destination}")
        print(f"Total Seats: {bus.total_seats}")
        print(f"Available Seats: {bus.available_seats}")
        print(f"Fare: {bus.fare:.2f}")
    else:
        print(f"Bus with Bus Number {bus_number} not found.")


def main():
    users = [
        User("user1", "pass1"), User("user2", "pass2"),
        User("user3", "pass3"), User("user4", "pass4"), User("user5", "pass5")
    ]
    buses = [
        Bus(101, "City A", "City B", 50, 50, 500.0),
        Bus(102, "City C", "City D", 40, 40, 400.0),
        Bus(103, "City E", "City F", 30, 30, 300.0)
    ]

    logged_in_user_id = None

    while True:
        if logged_in_user_id is None:
            choice = display_main_menu()

            if choice == '1':
                username = input("Enter Username: ")
                password = input("Enter Password: ")

                logged_in_user_id = login_user(users, username, password)
                if logged_in_user_id == -1:
                    print("Login failed. Please check your username and password.")
                else:
                    print(f"Login successful. Welcome, {username}!")
            elif choice == '2':
                logged_in_user_id = sign_up_user(users)
                if logged_in_user_id is not None:
                    print(f"Welcome, {users[logged_in_user_id].username}!")
            elif choice == '3':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please try again.")
        else:
            user_choice = display_user_menu()

            if user_choice == '1':
                book_ticket(buses)
            elif user_choice == '2':
                cancel_ticket(buses)
            elif user_choice == '3':
                check_bus_status(buses)
            elif user_choice == '4':
                print("Logging out.")
                logged_in_user_id = None
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()