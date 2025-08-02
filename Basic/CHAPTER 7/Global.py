a = 3;
def fun():
    global a;# this help to change the value of global a directly
    a = 20;
    print(a);
fun();
print(a);