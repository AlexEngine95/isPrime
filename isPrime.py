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
    percentage = 100 * float(x/end)
    if str(percentage) == str(int(percentage)) + ".0":  #Overly complicated way of checking that the percentage of numbers checked is, effectively, an integer. Not perfect.
        print(str(int(percentage)) + "% complete.")
a.close()
