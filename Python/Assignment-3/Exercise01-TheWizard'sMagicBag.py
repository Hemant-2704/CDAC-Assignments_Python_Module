"""Scenario:Awizardhasamagicbagcontainingasequenceofitems:["staff", "potion","spellbook"].Whenthewizardstepsthroughamagicportal,twothingshappen:1.Anewitementersthebag(promptstheusertoinputtheitemnametoappendtotheend).2.Theoldestiteminthebag(atindex0)isdissolvedandejected.Writeaprogramtosimulatethisportaltransitionandprintthefinalbagcontents.SampleInput:(Userinputs"amulet")SampleOutput:Scenario:
A wizard has a magic bag containing a sequence of items: ["staff", "potion", "spellbook"]. 

When the wizard steps through a magic portal, two things happen:
1. A new item enters the bag (prompts the user to input the item name to append to the end).
2. The oldest item in the bag (at index 0) is dissolved and ejected.

Write a program to simulate this portal transition and print the final bag contents.

Sample Input:
(User inputs "amulet")

Sample Output:
Portal transition activated!
Ejected oldest item: staff
Current items in the magic bag: ['potion', 'spellbook', 'amulet']

"""

def MagicBag():
    magic_bag=["staff", "potion", "spellbook"] # default  list
    # Looping untill  user wanna stop
    while(True):
        
        print(80*"_")
        print("***Wizard Stepping through Magic Portal***")
        print(f"{magic_bag=}") # showing list

        new_item=input("Enter new item to add to Magic Bag:") # Taking user input
        magic_bag.append(new_item) # new item is added at last-newest in bag
        print(f"Ejected oldest item:{magic_bag.pop(0)}") # Removing and returning oldest-first element in list
        print(f"Current items in the magic bag:{magic_bag}")

        # Repeating unless user doesnt enter "y"
        step=input("Do you wanna STEP in Portal Again? y/n:")
        if(step.strip().lower()[0]!="y"):
            return()

MagicBag()