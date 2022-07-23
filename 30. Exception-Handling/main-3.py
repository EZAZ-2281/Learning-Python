def voter(n): 
    if(n >= 18): 
        print("You are allowed to vote")
    else: 
        raise ValueError("Invalid voter")
try: 
    voter(22) 
except ValueError as e:
    print(e)  