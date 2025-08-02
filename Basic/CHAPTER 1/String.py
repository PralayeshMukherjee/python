# their are 3 ways to define a string in python
a = "raj";
b = 'raj';
c = """raj""";
print(a, type(a), b, type(b), c, type(c));
# strings are immutable in python
# the index start from 0
print(a[0]);
# way to make a substring (last index is exclusive)
print(a[1:3]);
# their are also negative indexing of string like last character of the string is -1
print(a[-1]);
print(a[-3:-1]);
word = "0123456789";
print(word[1:2:2]);