import functools
globalDict = {}

def tracecall(f):

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        global globalDict
        key = "%s (%d)" % (f.__name__, id(f))

        # Count the number of calls
        if key in globalDict:
            globalDict[key] += 1
        else:
            globalDict[key] = 1
        return f(*args, **kwargs)

    return wrapper


@tracecall 
def myfunc1():
     pass

myfunc1()
myfunc1()

@tracecall
def myfunc1():
     pass

a = myfunc1
myfunc1 = 42

a()

print(globalDict)
