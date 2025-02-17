x=0
def outer():
    def inner():
        print(x)
    print(id(inner))
    return inner

fun=outer
fun()
print(id(outer))
print(id(fun))
print("Case 2")
# case 2
def outer2():

    def inner2():
        print(x)
    print(id(inner2))
    return inner2

fun2=outer2()
print(id(outer2))
print(id(fun2))
print("Case 3")
 # case 3
def outer3():
    def inner3():
        print(x)
    print(id(inner3))
    return inner3()

fun3=outer3()
print(id(outer3))
print(id(fun3))
fun4=None
print((id(fun4)))