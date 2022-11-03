#平均分數計算
average = input("請輸入何種服務\n平均按1\n計算機按2")
if average=="1"
    
if average=="2"
else:
    print("暫不支援此功能") 
#建立計算機(加減乘除)
number1 = float(input("請輸入第一個數: "))    #input為提示之意思
operate = input("請輸入運算符號")             #即為字串，無須轉換成數字
number2 = float(input("請輸入第二個數: "))
                                             #字串經float轉換後，轉換成有小數點之數
#判斷加減乘除
if operate=="+":
    print(number1+number2)
elif operate=="-":
    print(number1-number2)
elif operate=="/":
    print(number1/number2)
elif operate=="*":
    print(number1*number2)
else:
    print("暫不支援此運算")

#平均分數計算
a=int(input("請輸入第一個數"))
b=int(input("請輸入第二個數"))
c=int(input("請輸入第三個數"))
total=a+b+c
print("得",total)
print("得",total/3)
                
                