"""
Scenario
Student feedback records contain ratings from 1 to 5 stars. Due to raw data entry issues, the feedback
database has some course entries with list values that are empty, or lists containing invalid elements
(such as string annotations like "Excellent" or None values).

Problem Description
Write a function compile_feedback(ratings_dict) that processes course feedback:
The parameter ratings_dict is a dictionary where keys are course names (strings) and values
are lists of ratings (which should be numeric but may contain invalid types).
The function must return a dictionary mapping each course name to its average rating, rounded to
2 decimal places.

Implement the following error handling criteria:
1. For each rating inside a course's list, attempt to convert it to a float. If a rating cannot be
   converted (throws a ValueError or TypeError), catch the exception, print a warning:
   "Warning: Invalid rating value '<val>' in course '<course>' skipped.",
   and continue processing the rest of the list.

2. If a course has no valid ratings (the list is empty or contains no convertible numbers),
   computing the average will trigger a division-by-zero error. Catch ZeroDivisionError,
   print a warning: "Warning: No valid ratings found for course '<course>'. Rating set to 0.0.", 
   and assign the course an average rating of 0.0.

Sample Input
feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}

Expected Output
Console Warnings Printed:
Warning: Invalid rating value 'Great' in course 'Python Programming' skipped.
Warning: No valid ratings found for course 'Machine Learning'. Rating set to 0.0.
Warning: Invalid rating value 'Good' in course 'Deep Learning' skipped.
Warning: Invalid rating value 'Average' in course 'Deep Learning' skipped.
Warning: Invalid rating value 'None' in course 'Deep Learning' skipped.
Warning: No valid ratings found for course 'Deep Learning'. Rating set to 0.0.

Returned Dictionary:
{
    "Python Programming": 4.5,
    "Machine Learning": 0.0,
    "Deep Learning": 0.0
}
"""



global  feedback_data
# Hardcoded Input in form of dictionary containing Lists as values of string keys
feedback_data = {
    "Python Programming": [5, 4, "4", "Great", 5],
    "Machine Learning": [],
    "Deep Learning": ["Good", "Average", None]
}
#  Line function for displaying line of ______
def line():
    print("_"*80)
    return()

def compile_feedback(feedback_data):

    # Looping through keys
    for subject in feedback_data.keys():

        # Resetting Addition to 0
        add_rating=0

        # Resetting not considered values in average
        remove=0

        # Getting Value of key which is a list
        subject_rating=feedback_data[subject]

        # If list is empty directly print warning
        if(len(subject_rating)==0):
            average_rating=0.00
            print(f"Warning: No valid ratings found for course {subject}. Rating set to {average_rating}")
            line()
            continue
        
        # Interating through each subject list
        for i in range(len(subject_rating)):

            # Checking if they are float convertable or not
            try:
                rating=subject_rating[i]

                # Turning into float upto 2 decimal
                rating=f"{float(rating):.2f}" # Found syntax from Internet
                # Adding each valid float Value
                print(rating)
                add_rating+=rating
                

            # If not float convertable raising warning and poping the invalid input from  List
            except:
                print(f"Warning: Invalid rating value {rating} in course {subject} skipped.")
                remove+=1
                continue
        
        # Checking if list has addition of 0 then average=0 (all were invalid values )
        if(add_rating==0):
            average_rating=0.00
            print(f"Warning: No valid ratings found for course {subject}. Rating set to {average_rating}")
            line()
        else:
        # Taking average of valid rating's
            average_rating=add_rating/(len(subject_rating)-remove)
            print(f"average rating={average_rating}")
            line()

    return()

compile_feedback(feedback_data)