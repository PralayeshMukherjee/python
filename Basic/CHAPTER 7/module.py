def myfunc():
    print("hello world");
myfunc();
print(__name__)# it show which file I import this file

if __name__ == "__main__":
    # if this code is directly executed by running the file it present in means if we run modhule file and it is imported in main.py file then only this block of code executed
    print("we are directly running this code");