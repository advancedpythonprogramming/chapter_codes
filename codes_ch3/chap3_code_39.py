class User:
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized("Not telling you!!")  # exceptions coming soon!
            return function(*args, **kw)

        return __protect

    return _protect


john = User(('admin', 'user'))
peter = User(('user',))


class Secret:
    @protect('admin')
    def pisco_sour_recipe(self):
        print('Use lots of pisco!')


s = Secret()
user = john
s.pisco_sour_recipe()
user = peter
s.pisco_sour_recipe()
