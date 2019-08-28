from functools import wraps

def decorator(func):
    @wraps(func)
    def wrap():
        print('before')
        func()
        print('after')
    return wrap

@decorator
def decorateMe():
    print('Boring stuff')

decorateMe()