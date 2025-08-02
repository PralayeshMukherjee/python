# it can store different data types 
# it start wit 0th index
fruit = ["apple", "orange", 5, 32.23, False];
print(fruit[0]);
fruit[1] = False;
print(fruit[1]); #it is mutable

print(fruit); #it print entire list

fruit.append("raj"); # add element at the end of the list 
print(fruit);

number = [5,2,3,1,4];
number.sort() # to sort the list
print(number);
number.reverse() # to reverse the list
print(number);

number.insert(2, 10); # insert 10 at index 2
print(number);

returnValue = number.pop(2);# remove the element at ith index and return it
print(returnValue);
print(number);