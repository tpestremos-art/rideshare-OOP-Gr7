from driver import DriverAccount
from dispatcher import RideDispatcher

class Passenger:
    def __init__(self, name):
        self.name = name
        self.__balance = 0.0

    def get_balance(self):
        return self.__balance

    def top_up(self, amount):
        if amount <= 0:
            raise ValueError("Top up must be more than 0")
        self.__balance += amount

    def pay_fare(self, amount):
        if amount > self.__balance:
            raise ValueError("Not enough funds")
        self.__balance -= amount

def main():
    print("===== RIDESHARE SYSTEM =====")

    driver1 = DriverAccount("John Doe", "ABC-123")
    passenger1 = Passenger("Maria Santos")

    print("\n--- Driver Information ---")
    print("Name:", driver1.name)
    print("Vehicle Plate:", driver1.vehicle_plate)

    driver1.add_rating(5.0)
    driver1.add_rating(4.5)
    print(driver1.get_rating_info())

    print("\n--- TEST 1: Negative Top-Up ---")
    try:
        passenger1.top_up(-100)
        print("FAILED: Negative top-up accepted!")
    except ValueError as e:
        print("SUCCESS: Top-up rejected:", e)

    print("\n--- TEST 2: Insufficient Funds ---")
    try:
        passenger1.pay_fare(500)
        print("FAILED: Payment accepted without funds!")
    except ValueError as e:
        print("SUCCESS: Payment rejected:", e)

    print("\n--- TEST 3: Invalid Driver Rating ---")
    try:
        driver1.add_rating(10)
        print("FAILED: 10-star rating accepted!")
    except ValueError as e:
        print("SUCCESS: Rating rejected:", e)

    print("\n--- FINAL INFORMATION ---")
    print("Passenger:", passenger1.name)
    print("Passenger Balance:", passenger1.get_balance())
    print(driver1.get_rating_info())

if __name__ == "__main__":
    main()
