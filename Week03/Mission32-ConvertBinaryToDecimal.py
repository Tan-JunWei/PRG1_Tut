#Programming I

################################
#      Mission 3.2             #
#   Convert Binary to Decimal  #
################################

#Background
#==========
#A binary value can be converted to a decimal value by taking the sum of each 
#binary digit times their power of 2 (you may refer to the steps and example
#given in Coursemology.

#Write a Python program to convert a 4-digit binary value to a decimal value.


#Important Notes
#===============
#1) You are required to include a function called binaryToDecimal(), which
#   accepts a string of 4-digit binary value, converts it to decimal value
#   and returns the result
#2) When testing the program in IDLE, you should prompt the user for the input
#   value. However, you must comment out the input prompt before submitting it
#   in coursemology


#START CODING FROM HERE
#======================
#Prompt and obtain input of a 4-digit binary value and assign it to binary_value
#Note: Do not change the input to int type.
#binary_value = str(input("Please input a 4-digit binary value:"))

#Do not edit/remove the next line
def binaryToDecimal(binary_value):
    binary_list = [int(digit) for digit in binary_value]
    currentDigitIndex = -1
    resultList = [] 
    n = 0
    
    for i in range(len(binary_value)):
        x = 2**n 
        result = int(binary_list[currentDigitIndex] * x)
        resultList.append(result)
        currentDigitIndex -=1
        n+=1
    
    
    #Return the result
    decimal_value = sum(resultList)
    return decimal_value #Do not remove this line

#Prompt for a 4-digit binary value (do not convert it to int type) and assign it
#to binary_value. You must remove this statement when submitting in Coursemology


#Do not edit/remove the next line that calls the function 
decimal_value = binaryToDecimal(binary_value)

#Modify the statement to display the decimal value
print(decimal_value)

#input '1011' output 11
#input '1100' output 12
