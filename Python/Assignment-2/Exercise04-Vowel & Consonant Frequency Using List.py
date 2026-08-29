def count_in_String():

    # Taking User Input 
    sting=input("Enter a string:")

    # Converting into lower not to miss anything
    sting=sting.lower()

    summ=0 # Sum of total vowels
    vowels=["a","e","i","o","u"]

    # Iterating through list of vowels    
    for i in vowels:
      print(f"{i}={sting.count(i)}")

      # Total no.of vowels in string  
      summ=summ+sting.count(i)
    print(f"Total number of vowels in string is {summ}")

    # Removing frequency of vowels and whitespace from len of string to get FREQ of CONSONENTS
    print("consonents=",len(sting)-(summ+sting.count(" ")))

count_in_String()