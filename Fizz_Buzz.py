b_FB = False
b_F = False
b_B = False 

i = int(input("実行回数")) + 1
for num in range(1,i):
    if(num % 15 == 0):
        print("Fizz Buzz")
        b_FB = True
    
    if(num % 3 == 0 and not b_FB):
        print("Fizz")
        b_F = True

    if(num % 5 == 0 and not b_FB):
        print("Buzz")
        b_B = True

    if not(b_FB or b_F or b_B):print(num)

    b_FB = False
    b_F = False
    b_B = False 
    

