# Program that deals with the queue datastructure

from collections import deque

clients = deque()


# Walk in function, deals with customer arrivals
def walk_in(customer):
    clients.append(customer)


# Serviced function to demonstrate attendance
def serviced():
    customer_serviced = clients.popleft()
    print(clients, ' Serviced!!')


# Function calling and printing
walk_in('Joshsh')
walk_in('HGHGH')
serviced()
print(clients)
