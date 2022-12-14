"""
Ragul
CP1404 Practical8
Test taxi
"""

from taxi import Taxi


def main():
    """Test Taxi class."""
    my_taxi = Taxi("Prius 1", 100)
    my_taxi.drive(40)
    my_taxi.price_per_km(1.23)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)

