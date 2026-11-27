class DriverAccount:
    def __init__(self, name, vehicle_plate):
        self.name = name 
        self.vehicle_plate = vehicle_plate
        self.__ratings = []
        self.__total_trips = 0
        self.average_rating = 5.0

    def add_rating(self, new_rating):
        if new_rating < 1.0 or new_rating > 5.0:
            raise ValueError("Invalid Rating!")
        else:
            self.__ratings.append(new_rating)

        self.__total_trips += 1 
        self.average_rating = sum(self.__ratings)/len(self.__ratings)

    def get_rating_info(self):
        return f"Current Average Rating: {self.average_rating:.2f} | Total Trips: {self.__total_trips}"