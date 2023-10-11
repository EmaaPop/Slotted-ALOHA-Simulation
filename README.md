# Slotted-ALOHA-Simulation
Slotted ALOHA is a protocol used for the MAC layer of application. This simulates the most efficient method to send packets across. 

### Rules:

* Nodes transimit new packets according to a Poisson process and retransmit packets after some random time if collision is detected
* Time is slotted, and a packet can only be transmitted at the beginning of the slot
* After transmitting a packet, the node transmits a new packet after a random time offset, regardless of whether the transmission was successful or not
* The random time offset follows the uniform distribution within [0, W)

### Tasks:

* Simulates N senders for 100000 time slots
* The **slot efficiency** is defined as *# of successful slots / # of total slots*
  * Successful slot means that there is one and only one transmitted packet in the slot
  * No transmission or two or more transmission in a slot is considered not successful
* Implements the slotted ALOHA simulation
* Represents in a Pandas Dataframe our results (Number of nodes, Slot efficiency)
* Plots the slot efficiency graph while varying the number of nodes N from 1 to 64
* Each group has a different window size:
    * Group 1 --> 4
    * Group 2 --> 8
    * Group 3 --> 16
    * Group 4 --> 32
    * Group 5 --> 64
    * Group 6 --> 128

### Tips:

* Iterate through different scenarios of numbers of nodes (first only one, then two, ...)
* Each Node has a TTL (number of slots after which it will transmit, for example if a node has TTL=7, it will wait 7 slots before transmitting). TTL has to be generated randomly (between a specific range...)
* Consider each slot and the number of nodes you have for that scenario, see how many nodes are going to transmit during that particular slot. If only one transmits, that is a successful slot (remember that after the transmission, the node may want to transmit again later). If no nodes or more than one nodes transmit, that is a not successful slot (remember what happens after a collision...)
* For each slot, calculate its efficiency


![](https://github.com/EmaaPop/Slotted-ALOHA-Simulation/blob/main/Week%202%20Outcome%202.png)https://github.com/EmaaPop/Slotted-ALOHA-Simulation/blob/main/Week%202%20Outcome%202.png)

