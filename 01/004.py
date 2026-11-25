n = int(input("Введіть висоту n: "))
w = int(input("Введіть ширину w: "))
for _ in range(n):
    print("*" * w)
    
print("----------------")
       
for _ in range(1, n + 1):
   print("*" * _)
   
print("----------------")
   
for _ in range(n, 0, -1):
    print("*" * _)
    
print("----------------")
   
if w >= 2:
    print("*" * w)
    for _ in range(n - 2):
        print("*" + " " * (w - 2) + "*")
    print("*" * w)