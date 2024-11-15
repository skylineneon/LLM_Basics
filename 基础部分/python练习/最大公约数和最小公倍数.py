'''
最大公约数gcd：使用辗转相除法
最小公倍数lcm
最小公倍数=abs(a*b) // gcd(a, b)
'''
def gcd(a, b):
    while b!= 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a, b)

# 测试最大公约数和最小公倍数
a = 48
b = 60

print(f"{a}和{b}的最大公约数是: {gcd(a, b)}")
print(f"{a}和{b}的最小公倍数是: {lcm(a, b)}")
