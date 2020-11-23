from Departure import dijkstra, graph


class Journey:

    def __init__(self, passengers, miles, destination):
        passengers = passengers
        miles = miles
        destination = destination

        # below splits the airport and miles to make it more usable
        departureAirport = (miles[0])
        destinationAirport = int(miles[1:])

        # statement to find the number of cars/taxis needed
        spaces = 4
        numberOfVehicles = 0
        people = passengers
        # people assumes the value of passengers, this is because the while loop alters the value
        # passengers is also used in flights to calculate the fuel cost
        # while loop could be swapped out for a math operator
        while people > 0:
            numberOfVehicles += 1
            people = (people - spaces)

        # fee calculation based on the number of cars needed.
        # this then prints out the cheaper vehicle and fee
        taxi = (destinationAirport * 0.8) * numberOfVehicles
        car = (destinationAirport * 0.4) * numberOfVehicles + (numberOfVehicles * 3)

        if taxi < car:
            totalvehicle = taxi
            print('Cheapest vehicle = Taxi', '\n', 'Vehicle return cost = £' + str(taxi))
        else:
            totalvehicle = car
            print('Cheapest vehicle = Car', '\n', 'Vehicle return cost = £' + str(car))
        # this needs to be returned so that it can be used in the total function ?

        print(dijkstra(graph, departureAirport, destination, passengers))
