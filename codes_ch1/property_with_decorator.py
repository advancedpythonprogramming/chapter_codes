# property_with_decorator.py

class Color:
    
    def __init__(self, rgb_code, name):
        self._rgb_code = rgb_code
        self._name = name
    
    # Create the property using the name of the attribute. Then we
    # define how to get/set/delet it.
    @property
    def name(self):
        print("Function to get the name color")
        return self._name
        
    @name.setter    
    def name(self, new_name):
        print("Function to set the name as {}".format(new_name))
        self._name = new_name
        
    @name.deleter
    def name(self):
        print("Erase the name!!")
        del self._name