# it is a data structure that stores only unique data
s = {1,3,4,3.2,2}
s1 = set(); # to make a empty set because if we do s1 = {} then it will create a empty dictionary
print(s); # it only store unique data with unordered way
# can't access the data using index
print(len(s)); # for the length of the set
s.remove(3.2); # it remove the element from the set
print(s);
s.pop(); # it remove random element from the set
s.clear(); # it will clear the set\

s1 = {1,23,43};
s2 = {1,23,43,5,6,7};
print(s1.union(s2));
print(s1.intersection(s2));
print(s1.difference(s2)); # it is like s1 - s2