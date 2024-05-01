def greet(name):
    return(f"Hello {name}")
    
a = greet("佐藤")
b = greet("鈴木")
print(a, b)

global_num = 10
def make_num():
    make_num = 20
    return make_num

a = make_num()
b = global_num
print(a, b)

def add_10(num):
    try:
        add_num = num + 10
        print(f"add_num is {add_num}")
        return add_num
    except:
        print("Error!!!!")
        
add_10(10)
add_10("二十")

def add_10(num):
    if not isinstance(num, int):
        print("Invalid num")
        return False
    add_num = num + 10
    print(f"add_num is {add_num}")
    
add_10(10)
add_10("二十")

for i in range(3):
    ans = i + 10
    print(ans)

from typing import Optional
from typing import Union

def divide_num(a: int, b: int)->Optional[int]:
    if b == 0:
        return None
    return a // b

def multiply_num(a: Union[int, str], b: Union[int, str])->int:
    a_int = int(a)
    b_int = int(b)
    return a_int * b_int

def make_greet(name: str) ->str:
    greet = f'Hello {name}-san'
    return greet

print(make_greet("aya"))
