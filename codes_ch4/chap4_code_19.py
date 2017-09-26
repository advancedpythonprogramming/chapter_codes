class System:
    # users_dict = {}  we will do this automatically inside __new__

    # cls is the object that represents the class
    def __new__(cls, *args, **kwargs):
        cls.users_dict = {}
        cls.id_ = cls.generate_user_id()
        # object has to create the class (everything inherits from object)
        return super().__new__(cls)

    # recall that self is the object that represents the instance of the class
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        return [System.users_dict[ar] for ar in args]

    @staticmethod
    def generate_user_id():
        count = 0
        while True:
            yield count
            count += 1

    def add_user(self, name):
        System.users_dict[name] = next(System.id_)


if __name__ == "__main__":
    e = System("Zoni")
    e.add_user("KP")
    e.add_user("CP")
    e.add_user("BS")
    print(e.users_dict)
    print(e("KP", "CP", "BS"))
    print(System.mro())  # prints the class and superclasses
