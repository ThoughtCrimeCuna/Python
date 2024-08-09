# Levi Peachey-Stoner
# Token-Based access Scheme

# initialize simulation parameters
import random

T = 15
service_times = [6, 6, 6]
switch_over_time = 1
arrival_times = [2, 4, 6]
interarrival_times = [10, 15, 20]

# initialize clocks
MC = 0              # Main Clock
runtime = 100        # How long the simulation will run
DT = 0              # Departure time clock
TOUT = 0            # Time out clock for token
ANN = 0             # Arrival next node
arrival_clocks = arrival_times
# initialize queues and token position
queue_lengths = [0, 0, 0]
token_position = 0

# initialize packet transmission variables
packet_transmitted = False
num_transmissions = 0

def movetoken():
    global token_position, ANN
    token_position += 1
    ANN = MC + switch_over_time
    if token_position >= len(queue_lengths):
        token_position = 0
        
def PRINT():
    lyst = [MC,arrival_clocks,queue_lengths,old_token,DT,TOUT,ANN,num_transmissions]
    print("\t".join(str(x) for x in lyst))

def transmit_packet():
    global packet_transmitted, num_transmissions
    packet_transmitted = random.choices([True, False], [0.99, 0.01])[0] # simulate transmission error with 1% probability
    num_transmissions += 1
    PRINT()

def reset_packet():
    global packet_transmitted, num_transmissions
    packet_transmitted = False
    num_transmissions = 0

print('MC\tArrivals\tQueues\t\tNode\tDepart\tTimeOut\tANN\tAttempt')
while MC <= runtime:
    old_token = token_position
    for x in range(len(arrival_clocks)):  # This section handles arrivals
        if arrival_clocks[x] == MC:
            arrival_clocks[x] += interarrival_times[x]
            queue_lengths[x] += 1
            PRINT()

    if ANN == MC:   # This section handles moving the token
        if queue_lengths[token_position] >= 1:
            DT = MC + service_times[token_position]
        else:
            movetoken()
        PRINT()

    elif MC == DT:  # This section handles departures
        queue_lengths[token_position] -= 1
        if not packet_transmitted:
            transmit_packet()
        if packet_transmitted or num_transmissions >= 5: # packet transmitted correctly or maximum number of re-transmissions reached
            reset_packet()
            DT = MC + service_times[token_position]
            if MC >= TOUT or queue_lengths[token_position] < 1: # This section handles timeouts
                TOUT = MC + T + switch_over_time
                movetoken()
        else: # re-transmit packet
            DT = MC
            PRINT()

    MC += 1
