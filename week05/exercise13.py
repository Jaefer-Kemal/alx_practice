'''Exercise 3: Write a program to generate a random set of numbers between 1 and ten. 
    Use set operations to remove duplicates and display the unique numbers.'''
import random   
def unique_number(n):
    random_numbers=[]
    
    for _ in range(n):
        rand = random.randint(0,10)
        random_numbers.append(rand)
        
        unique = set(random_numbers)
        
    print(f"\nList of random numbers are {unique}")
    print(f"List of unique nmbers are {random_numbers}")
        
unique_number(int(input("Generating random unique numbers\n input a number: ")))