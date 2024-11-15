def fun(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n>1:
        return fun(n-1)+fun(n-2)
    
result=int(input("请输入位置序号"))
print(f"第{result}个裴波那切数是{fun(result-1)}")
