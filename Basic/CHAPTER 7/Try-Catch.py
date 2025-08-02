# try-except(try-catch) block in python
try:
    a = 10;
    b = 0;
    print(a/b);
except Exception as e:
    print(e);

# this block of code used to raised an exception
c : int = 0;
if(c==0):
    raise ZeroDivisionError("Hey our progrom not divide by zero");
else:
    print(c)
# try-except block with else
# what happend here? -> if try block executed then only else block execute
try:
    a = 10;
except Exception as e:
    print(e);
else:
    print("else executed");
# try-except-finally
# reason? finally block always executed 
try:
    a = 10;
    b = 0;
    print(a/b);
except Exception as e:
    print(e);
finally:
    print("final");
# but what is the actual use of finally block because we achieve this simple print statement outside the try-except block right?
# when we use try-catch block in function then if we return from try/except block then also finally block executed - that is the actuall use of finally keyword
def div():
    try:
        a = 10;
        b = 0;
        print(a/b);
        return;
    except Exception as e:
        print(e);
        return
    finally:
        print("final block");
div();