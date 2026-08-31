"""Scenario:
A nightclub bouncer maintains a list of VIP guests who are allowed inside: ["Guido", "Esha", "Rajan", "Kishori"]. As guests arrive at the door, the bouncer prompts the user to enter their name. 

1. If the guest is on the VIP list, move them from their current position in the queue and insert them at the front of the queue (index 0). 
2. If the guest is not on the VIP list, print "Access denied. Not on the VIP list." and do not modify the list. 

Run this program in a loop. The loop should stop when the user types "exit". Print the updated queue state after each guest arrives.

Sample Walkthrough:
Current VIP queue: ['Guido', 'Esha', 'Rajan', 'Kishori']
Enter guest name: Rajan
Rajan moved to the front!
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: Vinod
Access denied. Not on the VIP list.
Current VIP queue: ['Rajan', 'Guido', 'Esha', 'Kishori']

Enter guest name: exit
"""

def Vip_Queue():
    VIP_queue= ['Guido', 'Esha', 'Rajan', 'Kishori'] # default Provided

    # Iterating untill exit condition hits
    while(True):
        print(80*"_") 
        guest=input("Enter Name of Guest:")

        # Checking exiting condition
        if(guest.lower().strip()=="exit"): 
            print(f"Current VIP queue: {VIP_queue}")
            print("...Exiting...")
            break

        # if guest is in not vip list
        if(guest not in VIP_queue):
            print(f"Access denied. {guest} is not on the VIP list.")
            print(f"Current VIP queue: {VIP_queue}")


        else:
            # if guest in vip list
            VIP_queue.remove(guest)  # Remove guest from list
            VIP_queue.insert(0,guest) # Add guest at front
            print(f"{guest} moved to the front!") 
            print(f"Current VIP queue: {VIP_queue}") # display updated list

    return()

Vip_Queue()


