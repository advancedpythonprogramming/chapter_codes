import time
import hashlib
import pickle

cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):

    key = pickle.dumps((function.__name__, args, kw))
    # returns the pickle representation of an object as a byte object
    # instead of writing it on a file

    # creates a key from the "frozen" key generated in the last step
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # do we have the value on cache?
            if key in cache and not is_obsolete(cache[key], duration):
                print('we already have the value')
                return cache[key]['value']

            # if we didn't
            print('calculating...')
            result = function(*args, **kw)
            # storing the result
            cache[key] = {'value': result, 'time': time.time()}
            return result

        return __memoize

    return _memoize
