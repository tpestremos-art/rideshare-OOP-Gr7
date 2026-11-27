class RideDispatcher:
    def process_ride_queue(self, ride_list):
        print("---Dispatching Ride Queue---")
        total_revenue = 0.0

        for ride in ride_list:
            ride.start_ride()
            total_revenue += ride.calculate_fare()
            ride.complete_ride()

        print(f"\nTotal Revenue for this batch: php{total_revenue:.2f}")
