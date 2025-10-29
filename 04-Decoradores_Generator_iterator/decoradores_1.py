import functools

def meu_decorator(func):
    @functools.wraps(func)
    def exemplo():    
        print("====== ANTES ======")
        res = func()
        print("====== DEPOIS ======")
        return res
    return exemplo

@meu_decorator
def ex01():
    print("executei ex01")


ex01()
print(ex01.__name__)


