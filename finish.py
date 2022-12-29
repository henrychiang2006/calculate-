def int2(num) -> any:
    if(num-int(num)==0):
        return int(num)
    else:
        return num
    
def average():
    numL=[]
    while(True):
        temp=input(">>>")
        try:
            temp = int(temp)
            numL.append(temp)
        except:
            break     
    ave = 0
    for i in numL:
        ave += i
    print(ave/len(numL))

def calculator():
    num1 = float(input("請輸入第一個數: ")) #input為提示之意思
    operate = input("請輸入運算符號")       #即為字串，無須轉換成數字
    num2 = float(input("請輸入第二個數: ")) #字串經float轉換後，轉換成有小數點之數
    match operate:
        case "+":
            print(int2(num1+num2))
        case "-":
            print(int2(num1-num2))
        case "*":
            print(int2(num1*num2))
        case "/":
            print(int2(num1/num2))
        case _:
            pass

def circle():
    import math
    r = float(input("請輸入半徑: "))
    print(f"perimeter = {2*math.pi*r}")
    print(f"Area = {r**2*math.pi}")

def power0():
    num = float(input("請輸入數字: "))
    power = float(input("請輸入次方: "))
    print(num**power)

#開n次根號
def power1():
    num = float(input("請輸入數字: "))
    power = float(input("請輸入平方根數字: "))
    print(num**(1/power))

# FIX
def half():

    #三角函數希望能做出來
    import math
    Pi = math.pi
    #rad = float(input("單位為弳/n 請輸入幾弳: "))
    #angle = float(input("單位為度 請輸入角度: "))
    #print (math.degrees(Pi))
    #print (math.radians(rad))
    x = float(input("請輸入角度: "))
    print(math.sin(x))
    print(math.tan(180 * x/Pi ))
    print(math.cos(x))
    
def ellipse():
   aa = float(input("請輸入長軸:"))#longaxis
   bb = float(input("請輸入短軸:"))#shortaxis
   print(f"perimeter = {2*pi*bb*4*(a-b)}")
   print(f"area {aa*bb*pi}")

#不等式一樣希望能做出來
def main():
    Basic = input("\n \n請輸入何種服務\n平均按1\n計算機按2\n圓計算按3\n橢圓按4\n次方按5\n平方根按6\n三角函數按7(單位為弧度): ")

    #分流
    match Basic:
        case "1":
            average()
        case "2":
            # 計算機
            calculator()
            pass
        case "3":
            circle()
        case "4":
            ellipse()
        case "5":
            power0()
        case "6":
            power1()
        case "7":
            half()
        case _:
            pass
            print("不支援此種服務\n \n \n \n")
while(1):
    main()