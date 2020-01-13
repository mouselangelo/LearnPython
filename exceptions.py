import sys

class CustomException(Exception):    
    def __init__(self, message):
        print("custom CustomException
     initialized...", message)
        self.value = message

def alwaysThrows():
    10 / 0

def raises(num):
    if num == 0:
        raise CustomException("Invalid argument")
    elif num == 1:
        raise Exception("One")
    elif num == 2:
        raise NoneType  ## raises NameError as NoneType is not defined
    elif num == 3:
        raise ## raises TypeError

def doSomething(value):
    try:
        if value in (0,1,2,3):
            raises(value)
        elif value == 4:
            alwaysThrows()
        else:
            raises(value)
    except ZeroDivisionError:
        print("ZeroDivisionError handler", sys.exc_value)
    except CustomException:
        print("CustomException handler", sys.exc_value)
    except Exception:
        print("Exception handler", sys.exc_value)
    except:
        ## never called?
        print("generic handler", sys.exc_value)
    else:
        print("no exception thrown - do something...")
    finally:
        print("done!")


for num in range(6):
    print("when: %s" % num)
    doSomething(num)
    print("")

