from collections import deque

bank = deque(["rahim", "karim", "abdul"])
print(bank)
bank.popleft()
print(bank)

bank.popleft()
bank.popleft()
print(bank) 

if not bank:
    print("No item left")