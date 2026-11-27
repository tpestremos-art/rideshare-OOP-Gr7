from driver import DriverAccount
from dispatcher import RideDispatcher

def main():
    print("===== RIDESHARE SYSTEM =====")

    driver1 = DriverAccount("John Doe", "ABC-123")

    driver1.add_rating(5.0)
    driver1.add_rating(4.5)

    print("\n--- Driver Information ---")
    print("Name:", driver1.name)
    print("Vehicle Plate:", driver1.vehicle_plate)
    print(driver1.get_rating_info())

    print("\n--- Testing Invalid Rating ---")
    try:
        driver1.add_rating(10.0)
    except ValueError as e:
        print("10-star rating rejected:", e)


if __name__ == "__main__":
    main()
