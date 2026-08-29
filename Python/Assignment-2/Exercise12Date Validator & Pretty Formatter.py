"""Your program must:
1. Verify if the date is valid. To be valid:
The month must be between 1 and 12 inclusive.
The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
For February, the day must be at most 29 in a leap year (divisible by 4, except for centuries not divisible by 400) and at most 28 in standard years.

2. If the date is valid, use a tuple of month names 
("January", "February", ...) to format and

print the date in a long-form readable layout: 
"MonthName DD, YYYY"
.
3. If the date is invalid, print 
"Invalid Date"
.
Sample Input: 
"26/08/2026"
Sample Output: 
"August 26, 2026"
Sample Input: 
"29/02/2026"
 (2026 is not a leap year)
Sample Output: 
"Invalid Date"
Sample Input: 
"31/04/2026"
 (April only has 30 days)
Sample Output: 
"Invalid Date"""

def valid_date(dd,mm,yyyy):
    max_days=0
    month={1:"January",2:"Febuary",3:"March",4:"April",5:"May",6:"June",7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    is_leap=0
    # Finding yyyy>0 
    if(yyyy<0):
        print("Invalid: Year must be above 0")
        return()
    elif((yyyy%4==0 and yyyy%100!=0) or yyyy%400==0):
        is_leap=1

    # Checking month
    if(mm<1 or mm>12):
        print("Month should be between 0-12 ")
        return()
    elif(mm in [4,6,9,11]):
        max_days=30
    elif(mm==2):
        if(is_leap):
            max_days=29
        else:
            max_days=28
    else:
        max_days=31

    # Checking days
    if(dd<=0 or dd>max_days):
        print(f"Invalid Input! {month[mm]} has {max_days} only!")
        return()

    # Printing Valid Output
    print("Valid Input!")
    print(f"{month[mm]} {dd}, {yyyy}")


    return()


def main():

    # Taking Input
    date=input("Enter a date:")

    # Looping untill two / are present
    while(True):
        try:
            # Unpacking Date/Month/Year
            dd,mm,yyyy=date.split("/")

        except:
            print("Wrong Input!")
            try_again=input("Wanna Try Again?y/n: ")
            if(try_again.strip().lower()=="y"):
                date=input("Enter a date:")
            else:
                print("...Exiting...")
                return()
        else:

            break

    # Looping untill the input are integer only int/int/int
    while(True):
        try:
            dd=int(dd)
            mm=int(mm)
            yyyy=int(yyyy)
            
        

        except Exception as err:
            print("Wrong Input!")
            print("Python says:",err)
            try_again=input("Wanna Try Again?y/n: ")
            if(try_again.strip().lower()=="y"):
                date=input("Enter a date:")
                dd,mm,yyyy=date.split("/")
            else:
                print("...Exiting...")
                return()
        else:
            break

    # moving to next func with int dd,mm and yyyy    
    valid_date(dd,mm,yyyy)

    return()

main()
        
