# args_example.py

def method2(f_arg, *argv):
    print("first arg normal: {}".format(f_arg))
    for arg in argv:
        print("the next arg is: {}".format(arg))

if __name__ == "__main__":
    method2("Lorem", "ipsum", "ad", "his", "scripta")
