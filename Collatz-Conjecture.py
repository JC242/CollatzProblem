import random
import time


def math():
    #Declaring variables 
    number = random.randint(1,100)
    result = [0,0,0]
    print(number)

    #Creating a while loop with the condition that once the pattern is achive it closes the loop. 
    while result != [1,2,4]:
        #Ading the condition that if is a par is divided by two 
        if number % 2 == 0:
            number = number /2
        #If is not a par is multiply by 3 and add 1 
        else:
            number = (3 * number) + 1
        #Inserted into the first element of the array
        result.insert(0,number)
        #Pop out the last element 
        result.pop()
        time.sleep(2)
        #print the number
        print(number)

if __name__ == "__main__":
    math()