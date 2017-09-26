# property_without_decorator.py

class Color:
    
    def __init__(self, rgb_code, name):
        self.rgb_code = rgb_code
        self._name = name
        
    def set_name(self, name):
        self._name = name
        
    def get_name(self):
        return self._name
   
    name = property(get_name, set_name)