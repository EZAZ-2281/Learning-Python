try:
    num = [12, 0, 6]
    result = num[0] / num[2]
    print(result)
    print("Successful")

except ZeroDivisionError:
    print("Division is not possible")

except IndexError:
    print("Out of index")

finally: 
    print("Golam Kibria")