"""Exercise 11: Group Anagrams
Write a program that starts with a list of strings defined at the top of your script 
e.g. 
words = ["eat","tea", "tan", "ate", "nat", "bat"]
and groups the anagrams (words formed by rearranging
letters together. Print the final grouped list of lists.

Hardcoded Input: 
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output: 
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]"""

def main():

    # Hardcoded Input
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    ans={}

    # Iterating through words
    for i in words:
        arranged = ''.join(sorted(i))

        # arranged is already a key      
        if(arranged in ans):
            ans[arranged].append(i)

        else: # arranged is not in dict
            ans[arranged]=[i]
    print(f"{ans.values()}")
    return()

main()