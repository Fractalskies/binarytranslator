#Import the required libraries/library
import math

#Welcome the user and give options
def start():
    startcon = input('''Welcome to binary code translator!
                     Press b for binary to decimal
                     Press q to quit
                     (Coming soon: Decimal to binary) ''')
    
    #Check options
    if startcon.lower() == "b":
        mainbin()
    elif startcon.lower() == "q":
        exit(0)
    else:
        print("Please choose a valid option.")
        start()


#Main function for binary code to decimal translation
def mainbin():

    #Setting up variables
    resulttosum = []
    powerslist = []
    bin = input("Enter the binary code to translate ")
    binaryinput = list(bin)
    binaryinput.reverse()

    #Check the list for values greater than 1 and less than 0

    #Iterating through the list, then returning the results to sum (I'm too lazy to describe this yk what I mean)
    for i in range(len(binaryinput)):
        powerslist.append(2**i)
        resulttosum.append(int(binaryinput[i])*int(powerslist[i]))
    
    finalans = sum(resulttosum)

    # These were just for debugging purposes, I'm gonna leave them here anyways tho
    #print(powerslist)
    #print(resulttosum)

    #Print the final sum
    print(finalans)
