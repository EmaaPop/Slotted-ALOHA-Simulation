import random
import pandas as pd
import matplotlib.pyplot as plt

# Total number of slots
TSLOTS = 100000

# This class represents a node that wants to transmit. It will transmit after a certain number of slots (ttl)
# Each node needs to have a classNode instance with a random ttl

class classNode:
	def __init__(self, ttl):
		self.ttl = ttl # number of slots left until transmission
	def tick(self):
		self.ttl = self.ttl - 1 # Decrease number of slots

## My Code
# Import necessary libraries
import random  # For generating random numbers
import pandas as pd  # For data analysis (not used in this code)
import matplotlib.pyplot as plt  # For creating plots

# Total number of time slots in the simulation
TSLOTS = 100000

# Define a class to represent a network node
class classNode:
    def __init__(self, ttl):
        self.ttl = ttl  # Initialize the time-to-live (ttl) for the node

    def tick(self):
        self.ttl = self.ttl - 1  # Decrease the ttl by 1 to count down

# Main function where the simulation takes place
def main():
    random.seed()  # Initialize the random number generator

    # Iterate over different window sizes
    for window_size in [8, 16, 32, 64, 128]:
        Nlist = []  # List to store the number of nodes
        selist = []  # List to store slot efficiency
        print("Window size: {0:2d}".format(window_size))  # Print the current window size

        # Iterate over different numbers of nodes
        for N in range(1, 64):
            # Create a list of network nodes with random ttl values
            snode = [classNode(random.randrange(0, window_size)) for _ in range(N)]
            successful_slots = 0  # Counter for successful slots
            slot_efficiency = 0  # Measure of network efficiency

            # Simulate the network over a large number of time slots
            for slot in range(TSLOTS):
                transmitted_nodes = []  # List to track nodes that transmit in the current slot

                # Check each node's ttl and determine if it can transmit
                for i in range(N):
                    if not snode[i].ttl:
                        transmitted_nodes.append(i)  # Node can transmit
                        snode[i].ttl = random.randrange(0, window_size)  # Set a new random ttl
                    else:
                        snode[i].tick()  # Decrease the ttl of nodes that can't transmit

                # Check the outcome of this time slot
                if not transmitted_nodes:
                    pass  # No nodes transmitted, so no change

                if len(transmitted_nodes) == 1:
                    successful_slots = successful_slots + 1  # One node successfully transmitted

                if len(transmitted_nodes) > 1:
                    for j in transmitted_nodes:
                        snode[j].ttl = random.randrange(0, window_size)  # Collision, nodes retry

                # Calculate slot efficiency as the ratio of successful slots to total slots
                slot_efficiency = (successful_slots / float(TSLOTS))

            # Print the results for the current number of nodes
            print("N = {0:2d}: {1:f}".format(N, slot_efficiency))

            # Store the results in lists for plotting
            Nlist.append(N)
            selist.append(slot_efficiency)

        # Plot the results for the current window size
        plt.plot(Nlist, selist)
        print("")

    # Add labels and legends to the plot, and display it
    plt.xlabel("# of Nodes")
    plt.ylabel("Slot Efficiency")
    plt.legend(['W = 8', 'W = 16', 'W = 32', 'W = 64', 'W = 128'], loc='upper right')
    plt.axis([0, 64, 0, 0.5])  # Set the axis limits
    plt.title('Slotted ALOHA Efficiency')  # Set the plot title
    plt.grid(linestyle='--')  # Add a grid to the plot
    plt.show()

    return

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function to start the simulation
