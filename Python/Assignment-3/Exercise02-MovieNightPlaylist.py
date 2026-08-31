"""
Scenario:
You are organizing a movie marathon. You start with a playlist: ["Inception", "The Matrix", "Interstellar"]. 

Prompt the user to enter the name of a movie they want to add. 
1. If the movie is already in the list, print "Already added!" and do not insert it. 
2. If it is not in the list, append it to the end of the list. 

Finally, sort the movie list alphabetically and print the updated playlist.

Sample Input 1:
"Interstellar"

Sample Output 1:
Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']

Sample Input 2:
"Avatar"

Sample Output 2:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']

"""

def Playlist():
    playlist= ["Inception", "The Matrix", "Interstellar"] # Default list/playlist
    keep_adding="y"
    while(True): # looping again

        print(80*"_")
        print(f"Current{playlist=}")
        
        add_movie=input("Enter a movie to Watch: ")




        #  Taking user input
        if(add_movie in playlist): # if movie to watch already in playlist
            print("Movie Already Added!")
            print(f"Alphabetical Playlist:{sorted(playlist)}") # Showing Sorted list 

            # Continue the program or loop arround
            keep_adding=input("Do You Wish to Continue y/n: ")
            if(keep_adding.strip().lower()[0]!="y"):
                print("...Exiting...")
                print("_"*80)
                return()

        # if movie to add is not present in playlist
        else: 

            playlist.append(add_movie) #  Added at end
            print(f"Added {add_movie}") # added movie is displayed
            print(f"Alphabetical Playlist:{sorted(playlist)}") # new updated and sorted list is viewed

            #  If wanna continue
            keep_adding=input("Do You Wish to Continue y/n: ")
            if(keep_adding.strip().lower()[0]!="y"):
                print("...Exiting...")
                print("_"*80)
                return()

            

Playlist()