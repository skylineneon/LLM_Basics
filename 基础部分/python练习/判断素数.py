def prime_num(n):
    
    for _i in range(2,n):
        if n%_i == 0:
            return False
    return True
prime_num1=int(input("请输入一个正整数")) 
print("是素数" if prime_num(prime_num1) else "不是素数") 
