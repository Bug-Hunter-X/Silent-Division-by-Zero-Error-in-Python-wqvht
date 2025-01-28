def function_with_uncommon_error(a, b):
    if a == 0:
        return b  # Incorrect return, should handle division by zero
    elif b == 0:
        return a #Incorrect return, should handle division by zero
    else:
        return a / b

result = function_with_uncommon_error(10,0)
print(result)