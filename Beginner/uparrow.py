
#This program will simulate the up arrow notation. This will be focused on getting the functionality down. The idea is apparently all we need is number 1,
#number 2 and the number of Up Arrows. The program could then be edited to take syntax ie 2 | 3 could be broken apart with the number of arrows counted, etc.

#Terminal will ask for first number, second number and arrow number, then compute.

def KunthArrow(num1, num2, arrownum):
    #We'll place this in its own function and opt to test it manually before setting it against the input given.
    #AHA! It's our best friend recursion.

    #CASE 1: if there's only one arrow.
    #==============================================================================================
    if arrownum == 1:
        return pow(num1,num2)


    #CASE 2: if arrownum is => 1 AND num2 = 0
    #==============================================================================================
    elif arrownum >= 1 and num2 == 0:
        return 1


    #CASE 3: anything else.
    #==============================================================================================
    else:
        return KunthArrow(num1, KunthArrow(num1, num2-1, arrownum), arrownum-1)


print(KunthArrow(2, 4, 2))
