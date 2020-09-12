#  Hint:  You may not need all of these.  Remove the unused functions.
"""
Understand
    tickets = [
    Ticket{ source: "NONE", destination: "LAX" },
    Ticket{ source: "LAX", destination: "SFO" },
    Ticket{ source: "SFO", destination: "BHM" },
    Ticket{ source: "BHM", destination: "FLG" }
    Ticket{ source: "FLG", destination: "XNA" },
    Ticket{ source: "XNA", destination: "CID" },
    Ticket{ source: "CID", destination: "SLC" },
    Ticket{ source: "SLC", destination: "PIT" },
    Ticket{ source: "PIT", destination: "ORD" },
    Ticket{ source: "ORD", destination: "NONE" },
]

Plan
    create ht
    create array 
    loop through tickets 
        if ticket.source == None 
            make the destination of said ticket first in array to return
        make hash entries {source, destination }
    loop through again
        assign route[index] to ht[index-1]


Execute
Review
"""
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    ht = {}
    route = [None] * length

    for i in range( len(tickets) ):
        if tickets[i].source == "NONE":
            route[0] = tickets[i].destination
        ht[tickets[i].source] = tickets[i].destination

    print(ht)
    print(route)
    for i in range( len(tickets) ):
        if route[i-1] is not None: 
            route[i] = ht[route[i-1]]
    return route


