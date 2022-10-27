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