# using lambda as function 
add= lambda a,b: a+b
print(add(4,3),"Addition with lambda as function")

# sorting dictionary by keys(for values you can just put a:a[1])
memo = {"name":"jack" , "age":3}
memo = sorted(memo.items(), key = lambda a:a[0])
print(dict(memo),"is new dictionary sorted interms of keys")

# using filters to return those who meet the condition
def even_number(num):
    if num%2==0:
        return num
    
numbers = [1,2,3,4,5,6,7,8]

# '''the use of list here is to convert the filter object into a list.'''

new_numbers = list(filter(even_number,numbers))
print(new_numbers,"are even numbers")

# using filter with lambda 
# '''So Let's filter odd numbers'''

odd_numbers = list(filter(lambda num:num%2!=0,numbers))
print(odd_numbers,"are odd number")

# using map with lambda

fruits = ["banana","apple","orange"]
berries = ["rasberry","blueberry","strawberry"]

list(map(lambda berry:fruits.append(berry),berries))
print(fruits,"Using map with lambda to add berries in to list of fruits")

# using reduve with lambda
from functools import reduce
cost = [1,2,3,4,5,6,7,8,9,10]
total = reduce(lambda acc,cur:acc+cur,cost,10)
print(total,"is the sum of all cost but with initial value = 10")