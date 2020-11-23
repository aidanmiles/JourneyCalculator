from JourneyToAirport import Journey


class Main:
    NewJourney = Journey(int(input('enter the number of passengers')),
                         input('enter the airport and miles e.g (A10)'),
                         input('Enter your destination airport'))
# This will return the cheapest vehicle and cost to the airport
# At the moment it also calls 'departure' and returns the shortest
# flight path and cost however this needs to be changed to be more
# independent as I don't think this is best practice
