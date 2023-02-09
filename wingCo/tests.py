#documentation: https://docs.djangoproject.com/en/4.1/topics/testing/overview/
from django.test import TestCase
from .models import Airport, Flight, Passenger

# Create your tests here.

# write test case class
class FlightTestCase(TestCase):
    def setUp(self):
        #create airports
        airport1 = Airport.objects.create(airportCode="AAA", city="City A")
        airport2 = Airport.objects.create(airportCode="BBB", city="City B")

        #create flights to test
        Flight.objects.create(origin=airport1, destination=airport2, duration=100) #valid
        Flight.objects.create(origin=airport1, destination=airport1, duration =100) #invalid (Same origin and destination)
        Flight.objects.create(origin=airport1, destination=airport2, duration=0) #invalid(no duration)
        Flight.objects.create(origin=airport2, destination=airport1, duration=-100) #invalid(neg duration)

    #test arrival counts
    def test_departures_count(self):
        airport = Airport.objects.get(airportCode="AAA")
        self.assertEqual(airport.departures.count(), 3)

    #test departure counts
    def test_arrivals_count(self):
        airport = Airport.objects.get(airportCode="AAA")
        self.assertEqual(airport.arrivals.count(), 2)

    def test_is_valid_flight(self):
        airport1 = Airport.objects.get(airportCode="AAA")
        airport2 = Airport.objects.get(airportCode ="BBB")
        flight = Flight.objects.get(origin=airport1, destination=airport2, duration=100)
        self.assertTrue(flight.is_valid_flight())

    def test_invalid_flight_duration(self):
        airport1 = Airport.objects.get(airportCode="AAA")
        airport2= Airport.objects.get(airportCode ="BBB")
        flight = Flight.objects.get(origin=airport1, destination=airport2, duration=0)
        self.assertFalse(flight.is_valid_flight())

    def test_invalid_flight_destination(self):
        airport1 = Airport.objects.get(airportCode="AAA")
        flight = Flight.objects.get(origin=airport1, destination=airport1)
        self.assertFalse(flight.is_valid_flight())