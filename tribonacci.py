def tribonacci(signature, n):
    result = []
    if n == 0:
        return result
    elif n <= 3:
        return signature[:n]
    for i in range(1, n-2):
        if i == 1:
            result = signature.copy()
        current_result = result[len(result)-1] + result[len(result)-2] + result[len(result)-3]
        result.append(current_result)
    return result
