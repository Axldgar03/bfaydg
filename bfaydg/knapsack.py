from typing_extensions import Sequence
import itertools
def suma_de_valores(values, keys):
    # Initializes the sum to 0
    sum=0
    # Gets the number of elements in the 'values' list
    n=len(values)
    # Iterates through the elements and calculates the weighted sum
    for i in range(n):
        sum+=values[i]*keys[i]
    # Returns the calculated sum
    return sum
#Capacidad de la mochila
def prblema_mochila(capacity, goal, weights, profits):
    # capacity is the maximum weight the knapsack can hold
    # weights is a list representing the weights of the items
    # profits is a list representing the profits of the items
    # goal is the minimum profit required

    n=len(weights)
    sequence=itertools.product([0, 1], repeat=n)
    for k in sequence:
        if suma_de_valores(weights, k) <= capacity:
            if suma_de_valores(profits, k) >= goal:
                return k
    return False
