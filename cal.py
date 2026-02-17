expr = input("Enter expression: ")
list_num = []
list_op = []
start = 0

for i in range(0, len(expr)):
    if expr[i] in ["+", "-", "*", "/"]:
        list_op.append(expr[i])
        list_num.append(expr[start:i])
        start = i + 1
list_num.append(expr[start:len(expr)])
print("Numbers:", list_num)
print("Operators:", list_op)
i = 0
while i < len(list_op):
    if list_op[i] == '*' or list_op[i] == '/':
        op = list_op.pop(i) 
        val1 = float(list_num[i])
        val2 = float(list_num[i + 1])
        
        if op == '*':
            ans = val1 * val2
        else:
            ans = val1 / val2
            
        list_num[i] = ans  
        list_num.pop(i + 1) 
    else:
        i += 1
i = 0
while i < len(list_op):
    if list_op[i] == '+' or list_op[i] == '-':
        op = list_op.pop(i)
        val1 = float(list_num[i])
        val2 = float(list_num[i + 1])
        if op == '+':
            ans = val1 + val2
        else:
            ans = val1 - val2
            
        list_num[i] = ans
        list_num.pop(i + 1)
    else:
        i += 1
print("Final Result:", list_num[0])
