def function_with_uncommon_error(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    elif a == 0:
        return 0
    else:
        return a / b

try:
    result = function_with_uncommon_error(10, 0)
    print(result)
except ZeroDivisionError as e:
    print("Error:", e) 

result1 = function_with_uncommon_error(10,2)
print(result1) 