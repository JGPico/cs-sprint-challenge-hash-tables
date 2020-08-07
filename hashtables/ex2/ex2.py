#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    route = []
    dictionary = {}
    for ticket in tickets:
        dictionary[ticket.source] = ticket.destination

    route.append(dictionary["NONE"])

    for i in range(length - 1):
        route.append(dictionary[route[i]])

    return route
