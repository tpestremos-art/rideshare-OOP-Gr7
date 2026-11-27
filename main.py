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
    driver1 = DriverAccount("John Doe", "ABC-123")
    passenger1 = Passenger("Maria Santos")

    driver1.add_rating(5.0)
    driver1.add_rating(4.5)
    print(driver1.get_rating_info())

    try:
        passenger1.top_up(-100)
    except ValueError as e:
        print("Top up rejected:", e)

    try:
        passenger1.pay_fare(500)
    except ValueError as e:
        print("Payment rejected:", e)

    try:
        driver1.add_rating(10)
    except ValueError as e:
        print("Rating rejected:", e)

    print("Balance of Passenger:", passenger1.get_balance())
    print(driver1.get_rating_info())

if __name__ == "__main__":
    main()
