frutas = ["maçã", "banana", "morango"]

for x in frutas:
    print(x)
    
    if x == "banana":
        continue

i = 1

while i < 6:
    print(i)
    i += 1

for x in range(2, 6):
    print(x)

# Saída:
    # 2
    # 3
    # 4
    # 5

print('#'*20)

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)
