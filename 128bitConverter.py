print("CONVERT HEXA TO 128 BITS\n");
hex = input("HEXA Value:")
size=len(hex)
print("Given input length:",size)
if(size==128):
    print(hex)
elif(0<size<128):
    n =128-size
    z="0"
    while n>0: 
        hex="0"+hex
        n=n-1
    print(hex)
else:
    print("Invalid input")
