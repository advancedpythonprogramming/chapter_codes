def mydecorator(function):
    def _mydecorator(*args, **kw):
        # Do stuff here before calling the original function
        # call the function
        res = function(*args, **kw)
        # Do more stuff after calling the function
        return res

    # return the sub-function
    return _mydecorator
