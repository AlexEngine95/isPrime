import os

prime = False
end = int(input("Enter the last number you want to be checked if it is prime."))
a = open("./output.txt", "w")
for x in range(2,end+1):
    for i in range(2,x+1):
        if x % i == 0 and x != i:
            prime = False
            break
        else:
            prime = True
    if prime:
        a.write(str(x) + " is prime. \n")
    else:
        a.write(str(x) + " isn't prime. \n")
    if x % 10000 == 0:
        print(x)
    if x % 50000 == 0:
        os.system("cls")
a.close()
