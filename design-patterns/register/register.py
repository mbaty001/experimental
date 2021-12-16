registry = []

def register(func):
    print(f"Registering {func}...")
    registry.append(func)
    return func

@register
def f1():
    print ("f1")

@register
def f2():
    print("f2")

if __name__  == "__main__":
    print(f"Registry: {registry}")
    for function in registry:
        function()