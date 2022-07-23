try: 
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter a number: "))
    result = num1 / num2 
    print(result) 
except (ValueError, ZeroDivisionError): 
    print("Division is not possible")
finally: 
    print("Kibria") 