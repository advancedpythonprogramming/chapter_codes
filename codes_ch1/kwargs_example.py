# kwargs_example.py

def method(arg1, arg2, arg3):
    print("arg1: {}".format(arg1))
    print("arg2: {}".format(arg2))
    print("arg3: {}".format(arg3))


if __name__ == "__main__":
    kwargs = {"arg3": 3, "arg2": "two"}
    method(1, **kwargs)
