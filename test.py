capitalsdict = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid"
}
for key in capitalsdict:
    print(key, ":", capitalsdict[key])

#formating strings
# print("The capital of France is {}".format(capitalsdict["France"]))
# print("The capital of Germany is {}".format(capitalsdict["Germany"]))

# name="John"
# age=30
# print("My name is {} and I am {} years old".format(name, age))
# print("My name is {0} and I am {1} years old".format(name, age))
# print("My name is {1} and I am {0} years old".format(age, name))
# print("My name is {name} and I am {age} years old".format(name=name, age=age))
# print(f"My name is {name} and I am {age} years old")


#for loop      
# Grades = [90, 80, 85, 70, 95]
# for n, i in enumerate(Grades):
#     print(f"Student {n+1} has a grade of {i}")
# print("Student {0} has a grades of {1}".format(n+1, i))
print("**************************************")
# names = ["Alice", "Bob", "Charlie"]
# addresses = ["123 Main St", "456 Elm St", "789 Oak St"]
# ages = [25, 30, 35]
# for n,a,g, in zip(names, addresses, ages):
#     print(f"{n} lives at {a} and is {g} years old")
# print("Student {0} lives at {1} and is {2} years old".format(n, a, g))


#Nested for loop
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# list3 = ['x', 'y', 'z']
# for i in list1:
#     for j in list2:
#         for k in list3:
#             print(i, j, k)
# print("Student {0} lives at {1} and is {2} years old".format(i, j, k))

# list comprehension
# squares = [x**2 for x in range(10)]
# print(squares)
# print("**************************************")
# Grades = [90, 80, 85, 70, 95]
# values = [i for i in Grades if i > 80]
# print(values)
# values = [i*2 for i in Grades if i > 80]
# print(values)

#Class with constructor and method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
        
person = Person("Alice", 30)
person.greet()
 
