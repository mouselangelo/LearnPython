import sys

class ZeroException(Exception):    
    def __init__(self, message):
        print("custom ZeroException initialized...", message)
        self.value = message

def throws():
    10 / 0

def raises(num):
    if num == 0:
        raise ZeroException("Invalid argument")
    elif num == 1:
        raise Exception("One")
    elif num == 2:
        raise NoneType  ## raises NameError as NoneType is not defined
    elif num == 3:
        raise ## raises TypeError

def doSomething(value):
    try:
        print("value: %s" % (value))
        if value in (0,1,2,3):
            raises(value)
        elif value == 4:
            throws()
        else:
            raises(value)
    except ZeroDivisionError:
        print("ZeroDivisionError handler", sys.exc_value)
    except ZeroException:
        print("ZeroException handler", sys.exc_value)
    except Exception:
        print("Exception handler", sys.exc_value)
    except:
        ## never called?
        print("generic handler", sys.exc_value)
    else:
        print("hurray")
    finally:
        print("done!")
        print("")


for num in range(6):
    doSomething(num)
