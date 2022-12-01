import math

def calc_sin(degree: float):
    x = convert_degree2radian(degree)
    sin = 0
    for n in range(100):
        temp1 = (-1) ** n
        temp2 = calc_fact(2 * n + 1)
        temp3 = x **(2 * n + 1)
        sin = sin + temp1 / temp2 * temp3
    return sin

def calc_fact (num: int): ## 3! = 1*2*3
    fact = 1
    for i in range(1, num = 1):
        fact = fact * i
        return fact
    
def convert_degree2radian(degree: float):
    radian = degree / 180 * math.pi
    return radian

degree = 90
result = calc_sin(degree)
print(result)
#rad = convert_degree2radian(degree)
#print("Degree 2 rad: ",rad)

#result = calc_fact(num = 3)
#print(result)
    






#不等式一樣希望能做出來