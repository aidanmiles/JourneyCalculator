# JourneyCalculator

Hi all, 

Here is an almost complete journey calculator, there may be a need to install the pip library (pip install git+git://github.com/ahojukka5/dijkstra.git) however this shouldn't
be necessary.

if you download all the files and open them up in your proffered IDE, then run the main function. 

In the console you will be prompted to enter how many passangers are taking the journey, enter any number you like or see the below test cases. 

you will then be prompted to enter an airport and distance to that airport, this can be any letter from A-F and any distance that you like. In future this letter option can be expanded as I integrate an upload option for the flight data.

next you will be prompted for a destination, again this can be any letter from A-F. Once you hit enter you will be presented with the cheapest vehicle to get to the airport, along with a charge. (please note this journey is 2 way and contains a £3 fee for every car you need to travel in, this fee is not applied to taxis)

Lastly you will also be presented with the shortest flight path and the cost of that flight path.   

**AREAS THAT NEED COMPLETION**

upload of flight paths - by completing this it will allow for a wider variety of different flight paths, I looked at using a reduce function however upon research in python 3.9 it is advised to use a loop instead (for readability purposes) So I haven't quite had chance to implement this yet.

calculation of the return trip - current attempts to do this have been faced with an error in the dijkstra function, from what I can tell the nodes are not resetting once the first route has been planned, so when the return journey tries to run it is told that the node is not acceptable and fails. 

So I am currently looking at ways to rest the nodes once the first path has been planned.

Totals - Once the total cost of the vehicle has been returned as well as the outbound and inbound flight costs I want to add a total cost over all, this should be relatively simple and just a case of accessing the variable storing this information and adding them.

Error handling - there is some basic error handling at the moment although it could be perceived as just a print statement (however it fills a criteria) I would like to add proper try catch statements for the functions to ensure no failings occur

Lastly I would like to use libraries in future to steam line areas ( however this being the first real project I have attempted in python I wanted to ensure I had the correct logic before using libraries)
