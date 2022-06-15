# Check whether parenthesis are properly formatted:
# ()()() - True
# ((() - False
# )(() - False

def bla(string: str) -> bool:
...     count = 0
...     for s in string:
...         if s == "(":
...             count += 1
...         elif s == ")":
...             count -= 1
...             if count < 0: 
...                 return False
...     if count == 0:
...         return True
...     else:
...         return False

assert bla("()()()") == True
assert bla("((()") == False
assert bla(")(()") == False
