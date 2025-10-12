def calculate_sum(a, b):
    result = a + b
    print("The sum of", a, "and", b, "is", result)
    return result


def calculate_product(x, y):
    product = x * y
    print("The product of", x, "and", y, "is", product)
    return product


# 这是一个符合PEP8规范的行长度限制的注释
if __name__ == "__main__":
    num1 = 10
    num2 = 20
    calculate_sum(num1, num2)
    calculate_product(num1, num2)
