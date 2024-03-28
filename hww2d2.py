# 1. Tuple Mastery in Python
# Task 1: Formatting Flight Itineraries
flight_itinerary = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]
def itinerary():
    index = 0
    for name, origin, destination in flight_itinerary:
        print(f"Itinerary {index + 1} : {name} - From {origin} to {destination}")
        index += 1

itinerary()


# 2. Python Data Structure Challenges in Real-World Scenarios
# Task 1: Library System Enhancement
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# print(library[1])
def add_book(book, author,):
    library_tuple = (book, author,)
    library.append(library_tuple)
    dups = set(library)
    main_list = list(dups)
    return main_list

print(add_book("Love her Wild", "Atticus"))

# 3. Python Loops and Tuples in Analytical Applications
# Task 1: Stock Market Data Analysis
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def stock_analysis(symbol):
    avg = "DNE"
    total = {}
    count = {}
    total.setdefault(symbol, 0)
    count.setdefault(symbol, 0)
    for stock, date, price in stock_data:
        stock.count(symbol)
        if stock == symbol:
            total[symbol] += price
            count[symbol] += 1
        if count[symbol] != 0:
            avg = total[symbol] / count[symbol]
    print(f"The average total of {symbol} is {avg}")


stock_analysis("AAPL")

# Task 2: Event Attendance Tracker
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]

def attendance():
    for name, event in attendees:
        print(f"{name} is attending {event}")

def count_attendees():
    attendances = {}
    for name, event in attendees:
        attendances.update ({event : 0})
    for name, event in attendees:
        attendances[event] += 1
    return attendances

print(count_attendees())
attendance()