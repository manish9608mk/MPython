"""
Create a class Movie with the following:

Attributes:
movie_name   -> Name of the movie
total_seats  -> Total seats available in the theatre
ticket_price -> Price per ticket
booked_seats -> Starts at 0

Methods:
book_ticket(num_tickets)
    - Books the given number of tickets.
    - If enough seats are available:
        . Confirm the booking.
        . Show the total amount to pay.
    - Otherwise:
        . Show "Sorry, not enough seats available."

show_status()
    - Displays:
        . Movie name
        . Available seats
        . Booked seats so far
"""

class Movie:

    # Constructor
    def __init__(self, movie_name: str, total_seats: int, ticket_price: int):
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    # Book movie tickets
    def book_ticket(self, num_tickets: int) -> None:

        # Calculate available seats
        available_seats = self.total_seats - self.booked_seats

        if num_tickets > available_seats:
            print("Sorry, not enough seats available.\n")

        else:
            self.booked_seats += num_tickets

            print("Your ticket is booked.")
            print(f"Total Price = {self.ticket_price * num_tickets}\n")

    # Display current movie status
    def show_status(self) -> None:

        available_seats = self.total_seats - self.booked_seats

        print(f"Movie Name      : {self.movie_name}")
        print(f"Total Seats     : {self.total_seats}")
        print(f"Booked Seats    : {self.booked_seats}")
        print(f"Available Seats : {available_seats}\n")


# Create Movie Object
movie = Movie("F1", 500, 99)

movie.show_status()

movie.book_ticket(200)
movie.show_status()

movie.book_ticket(100)
movie.show_status()

movie.book_ticket(250)
movie.show_status()

'''
OUTPUT

Movie Name      : F1
Total Seats     : 500
Booked Seats    : 0
Available Seats : 500

Your ticket is booked.
Total Price = 19800

Movie Name      : F1
Total Seats     : 500
Booked Seats    : 200
Available Seats : 300

Your ticket is booked.
Total Price = 9900

Movie Name      : F1
Total Seats     : 500
Booked Seats    : 300
Available Seats : 200

Sorry, not enough seats available.

Movie Name      : F1
Total Seats     : 500
Booked Seats    : 300
Available Seats : 200
'''