def funa():
    print("无参数方法")
    print("无返回值")


def funb(a, b):
    print(f"有参数方法,参数分别为:{a,b}")
    print("有返回值")
    return a+b


print(f"无返回值的默认返回值: {funa()}")
print(f"方法返回值为: {funb(1,2)}")