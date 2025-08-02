# store the data in key value pair like hashmap but store in a unordered way
marks = {
    "harry": 100,
    "subham": 53,
    "rohan": 32,
}
print(marks)
print(type(marks));
print(marks["harry"]); # to access value

# fetching time complexity is O(1) where we want to perform this operation in list of list that may take O(n^2) time complexity
# is is mutable
# it is indexed by keys
# can't contian duplicate keys
b = marks.items(); # it will return a view object that displays a list of a dictionary's key-value tuple pairs
print(b);
print(type(b))
print(marks.keys()) #it gives all the keys of the dictionary
print(marks.values()) #it gives all the values of the dictionary
marks.update({"rohan":99}); # it will update the value and also used to insert new key value pair
print(marks.get("rohan")); # another method to access value

# what is the difference between get and [] operator?
# ans:- if the key is not present in the dictionary then get will return None but [] operator will give error
print(marks.get("rohan1")); # it will return None
print(marks.get("roahn1", "not found")); # it will return not found (custom default value)