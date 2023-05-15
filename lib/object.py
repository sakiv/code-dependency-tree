
def has_key(object: object, path: str):
    keys: list = path.split('.')
    rv = object
    for key in keys:
        if key in rv:
            rv = rv[key]
        else:
            return False
    return True

def get_value(object: object, path: str):
    keys: list = path.split('.')
    rv = object
    for key in keys:
        rv = rv[key]
    return rv

def set_value(object: object, path: str, value: object):
    keys: list = path.split('.')
    rv = object
    for key in keys[:-1]:
        rv = rv[key]
    rv[keys[-1]] = value
    