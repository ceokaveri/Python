def calculate(s: str) -> int:
    stack = []
    sign = 1
    result = 0
    num = 0
    
    for char in s:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char == '+':
            result += sign * num
            num = 0
            sign = 1
        elif char == '-':
            result += sign * num
            num = 0
            sign = -1
        elif char == '(':
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif char == ')':
            result += sign * num
            num = 0
            result *= stack.pop()  
            result += stack.pop()  
        else:
            
            pass
    
   
    result += sign * num
    
    return result


# expression = " 2-1 + (3 - (4 + 5) + 6) "
expression = input("please enter the expression\n")
result = calculate(expression)
print(f"Expression: {expression}")
print(f"Result: {result}")
