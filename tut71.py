
def function1(function):
    def wrapper():
        print("print")
        function()
        print("welcome to python edureka tutorial")
    return wrapper
def function2():
    print("pythoist")

function2 = function1(function2)

function2()