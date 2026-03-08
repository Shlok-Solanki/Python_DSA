#Dicitonary

dict = {
    "Name": "Shlok",
    "CGPA": 7.8,
    "Age": 20
}
print(dict)
print(dict["Age"])#Accessing the value of a key
dict["Age"] = 21
print(dict)#Updating the value of a key

#Nested Dictionary
Classroom = {
    "Student1": {
        "Name": "Shlok",
        "CGPA": 7.8,
        "Age": 20
    },
    "Student2": {
        "Name": "Rohan",
        "CGPA": 8.5,
        "Age": 21
    }
}
print(Classroom)
print(Classroom["Student1"]["Name"])#Accessing the value of a key in a nested dictionary

#Dictionary Methods
print(dict.keys())#Returns a list of all the keys in the dictionary
print(dict.values())#Returns a list of all the values in the dictionary
print(dict.items())#Returns a tuple of all the key-value pairs in the dictionary
dict.pop("Age")#Removes the key-value pair with the specified key
print(dict.get("Name"))#Returns the value of the specified key
dict.clear()#Removes all the key-value pairs from the dictionary
dict.update({"Name": "Shlok", "CGPA": 7.8, "Age": 20})#Updates the dictionary with the specified key-value pairs
print(dict)

#Set
set = {1, 2, 3, 4, 5}
print(set)

#Set Methods

set.add(6)#Adds an element to the set
print(set)
set.remove(3)#Removes an element from the set
print(set)
set.pop()#Removes and returns an arbitrary element from the set
print(set)
set.clear()#Removes all the elements from the set
print(set)
set.union({7, 8, 9})#Returns a new set that is the union of the two sets
print(set.union({7, 8, 9}))
set.intersection({1, 2, 3})#Returns a new set that is the intersection of the two sets
print(set.intersection({1, 2, 3}))
set.difference({1, 2, 3})#Returns a new set that is the difference of the two sets
print(set.difference({1, 2, 3}))


#Store following word meanings in a dictionary and print them:
# Table: "A piece of furniture", "List of facts & figures"
#Cat: "A small animal" 
word_meanings = {
    "Table": ["A piece of furniture", "List of facts & figures"],
    "Cat": "A small animal"
}
print(word_meanings)

#You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are nedded by all students.
subjects = ["Maths", "Physics", "Chemistry", "Biology", "English"]
classrooms_needed = len(subjects)
print("Number of classrooms needed:", classrooms_needed)


#Write a program to enter marks of 3 subjects from the user and store them in a dictionary.Start with an empty dicitonary & add the key-value pairs one by one. Finally, print the dictionary.
marks = {}
marks["Maths"] = int(input("Enter marks for Maths: "))
marks["Physics"] = int(input("Enter marks for Physics: "))
marks["Chemistry"] = int(input("Enter marks for Chemistry: "))
print(marks)

#Store 9 & 9.0 as a seprate values in the Set
my_set = {9," 9.0"}
print(my_set)
