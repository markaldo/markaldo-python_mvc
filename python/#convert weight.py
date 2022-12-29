#convert_weight
weight=int(input('Weight: '))
units=str(input('(K)g or (L)bs: '))

def g_to_bs(w):
 x=w*2.2
 return x

def bs_to_g(w):
    y=w/2.2
    return y

if units.upper() == "K": 
 m=g_to_bs(weight)
 print("Weight in pounds")
 print(str(m))
elif units.upper() == "L":
 n=bs_to_g(weight)
 print("Weight in kilograms")
 print(str(n))
else:print("Invalid option")