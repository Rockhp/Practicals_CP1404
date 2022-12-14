"""
Ragul
CP1404 Practical8
SilverServiceTaxi class tests
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test Silver_Service_Taxi."""
    taxi = SilverServiceTaxi("Tester00", 100, 10, 48.78)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()