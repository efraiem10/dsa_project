import tkinter as tk
from tkinter import messagebox

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

class BusBookingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bus Booking System")
        self.root.geometry("400x300")  # Set the window size to 600x400 pixels

        self.users = [
            User("user1", "pass1"), User("user2", "pass2"),
            User("user3", "pass3"), User("user4", "pass4"), User("user5", "pass5")
        ]

        self.buses = [
            Bus(101, "City A", "City B", 50, 50, 500.0),
            Bus(102, "City C", "City D", 40, 40, 400.0),
            Bus(103, "City E", "City F", 30, 30, 300.0)
        ]

        self.logged_in_user = None

        self.main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def main_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="Bus Booking System", font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Login",font=("Arial", 17), command=self.login_screen).pack(pady=5)
        tk.Button(self.root, text="Sign Up", font=("Arial", 15),command=self.sign_up_screen).pack(pady=5)
        tk.Button(self.root, text="Exit",font=("Arial", 18), command=self.root.quit).pack(pady=5)

    def login_screen(self):
        self.clear_screen()
        
        tk.Label(self.root, text="Login", font=("Arial", 20)).pack(pady=10)
        tk.Label(self.root, text="Username",font=("Arial", 16)).pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        tk.Label(self.root, text="Password",font=("Arial", 16)).pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()
            
            for user in self.users:
                if user.username == username and user.password == password:
                    self.logged_in_user = user
                    messagebox.showinfo("Success", "Login successful!")
                    self.user_menu()
                    return

            messagebox.showerror("Error", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login,font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu,font=("Arial", 12)).pack(pady=5)

    def sign_up_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Sign Up", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Username").pack()
        username_entry = tk.Entry(self.root)
        username_entry.pack()
        tk.Label(self.root, text="Password").pack()
        password_entry = tk.Entry(self.root, show="*")
        password_entry.pack()

        def sign_up():
            username = username_entry.get()
            password = password_entry.get()
            
            if any(user.username == username for user in self.users):
                messagebox.showerror("Error", "Username already exists.")
                return

            self.users.append(User(username, password))
            messagebox.showinfo("Success", "Sign-up successful!")
            self.main_menu()

        tk.Button(self.root, text="Sign Up", command=sign_up).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.main_menu).pack(pady=5)

    def user_menu(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome, {self.logged_in_user.username}", font=("Arial", 14)).pack(pady=10)
        tk.Button(self.root, text="Book a Ticket", command=self.book_ticket_screen).pack(pady=5)
        tk.Button(self.root, text="Cancel a Ticket", command=self.cancel_ticket_screen).pack(pady=5)
        tk.Button(self.root, text="Check Bus Status", command=self.check_bus_status_screen).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=5)

    def book_ticket_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Book a Ticket", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Bus Number").pack()
        bus_number_entry = tk.Entry(self.root)
        bus_number_entry.pack()
        tk.Label(self.root, text="Number of Seats").pack()
        seats_entry = tk.Entry(self.root)
        seats_entry.pack()

        def book():
            bus_number = int(bus_number_entry.get())
            seats = int(seats_entry.get())
            
            for bus in self.buses:
                if bus.bus_number == bus_number:
                    if bus.available_seats >= seats:
                        bus.available_seats -= seats
                        messagebox.showinfo("Success", f"{seats} seats booked on Bus {bus_number}.")
                        self.user_menu()
                        return
                    else:
                        messagebox.showerror("Error", f"Only {bus.available_seats} seats available.")
                        return

            messagebox.showerror("Error", "Bus not found.")

        tk.Button(self.root, text="Book", command=book).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.user_menu).pack(pady=5)

    def cancel_ticket_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Cancel a Ticket", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Bus Number").pack()
        bus_number_entry = tk.Entry(self.root)
        bus_number_entry.pack()
        tk.Label(self.root, text="Number of Seats to Cancel").pack()
        seats_entry = tk.Entry(self.root)
        seats_entry.pack()

        def cancel():
            bus_number = int(bus_number_entry.get())
            seats = int(seats_entry.get())
            
            for bus in self.buses:
                if bus.bus_number == bus_number:
                    booked_seats = bus.total_seats - bus.available_seats
                    if seats <= booked_seats:
                        bus.available_seats += seats
                        messagebox.showinfo("Success", f"{seats} seats canceled on Bus {bus_number}.")
                        self.user_menu()
                        return
                    else:
                        messagebox.showerror("Error", "Cannot cancel more seats than booked.")
                        return

            messagebox.showerror("Error", "Bus not found.")

        tk.Button(self.root, text="Cancel", command=cancel).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.user_menu).pack(pady=5)

    def check_bus_status_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Check Bus Status", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="Bus Number").pack()
        bus_number_entry = tk.Entry(self.root)
        bus_number_entry.pack()

        def check():
            bus_number = int(bus_number_entry.get())
            
            for bus in self.buses:
                if bus.bus_number == bus_number:
                    messagebox.showinfo("Bus Status", f"Bus Number: {bus.bus_number}\nSource: {bus.source}\nDestination: {bus.destination}\nTotal Seats: {bus.total_seats}\nAvailable Seats: {bus.available_seats}\nFare: {bus.fare:.2f}")
                    return

            messagebox.showerror("Error", "Bus not found.")

        tk.Button(self.root, text="Check", command=check).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.user_menu).pack(pady=5)

    def logout(self):
        self.logged_in_user = None
        messagebox.showinfo("Logout", "You have been logged out.")
        self.main_menu()

if __name__ == "__main__":
    root = tk.Tk()
    app = BusBookingApp(root)
    root.mainloop()
