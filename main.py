def   calculate_sum  (  a,  b  ):
    result=a+b
    print("The sum of",a,"and",b,"is",result)
    return   result

def   calculate_product  (  x,  y  ):
    product=x*y
    print("The product of",x,"and",y,"is",product)
    return product

# 这是一个非常长的行，超过了PEP8推荐的79字符限制，这里故意写得很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长很长
if __name__=="__main__":
    num1=10
    num2=20
    calculate_sum(num1,num2)
    calculate_product(num1,num2)
