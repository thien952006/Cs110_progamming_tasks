# Author   : Xuan Thien Bui
# Email    : xuanthienbui@umass.edu
# Spire ID : 34750117


order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')
def get_protein(tuple):
    sum=0
    if(tuple[3]=="chicken" or tuple[3]=="veggies"):
        sum+=2.5
    elif(tuple[3]=="steak" or tuple[3]=="barbacoa"):
        sum+=3.5
    elif(tuple[3]=="carnitas"):
        sum+=3.0
    else:
        sum=0
    return sum
def get_rice(tuple):
    sum=0
    if(tuple[4]=="white"):
        sum+=2.5
    elif(tuple[4]=="brown"):
        sum+=3.5
    else:
        sum=0
    return sum
def get_beans(tuple):
    sum=0
    if(tuple[5]=="black" or tuple[5]=="pinto"):
        sum+=2.5
    else:
        sum=0
    return sum
def get_burrito(tuple):
    sum=0
    if(tuple[6]==True):
        sum+=2
    else:
        sum==0
    return sum
def get_toppings(a):
    sum=0
    for i in range(7,len(a)):
       if(a[i]=="guacamole"):
        sum+=2.75
        if(a[3]=="veggies"):
            sum-=2.75
       elif(a[i]=="tomato salsa"):
        sum+=2.5
       elif(a[i]=="chili corn salsa"):
        sum+=1.75
       elif(a[i]=="tomatillo green chili salsa"):
        sum+=2.0
       elif(a[i]=="sour cream"):
        sum+=2.5
       elif(a[i]=="fajita veggies"):
        sum+=2.5
        if(a[3]=="veggies"):
            sum-=2.5
       elif(a[i]=="cheese"):
        sum+=2.0
       elif(a[i]=="queso blanco"):
        sum+=2.75
       else:
        sum+=0
    return sum
def apply_discount(a:tuple, x:float):
    if(a[2]=="MAGIC"):
        x=x*0.95
    elif(a[2]=="SUNDAYFUNDAY"):
        x=x*0.9
    elif(a[2]=="FLAT3"):
        x-=3
    return x
def approximate_time(a):
    if(a[1]=="amherst" or a[1]=="north amherst" or a[1]=="south amherst" or a[1]=="hadley"):
        return 15
    elif(a[1]=="northampton" or a[1]=="south hadley" or a[1]=="belchertown" or a[1]=="sunderland"):
        return 30
    elif(a[1]=="holyoke" or a[1]=="greenfield" or a[1]=="deerfield" or a[1]=="springfield"):
        return 45
def change(a):
    if(a[6]==True):
        return "Yes"
    elif(a[6]==False):
        return "No"
def print_toppings(a):
    for i in range(7,len(a)+1):
        print(a[i])
def generate_invoice(a):
   print(f"Welcome to Chipotle Mexican Grill Hadley, {a[0]}.")
   print(f"Your invoice is displayed below:")
   print(f"Protein: {a[3]} - ${get_protein(a)}")
   print(f"Rice: {a[4]} rice - ${get_rice(a)}")
   print(f"Beans: {a[5]} beans - ${get_beans(a)}") 
   print(f"Burrito: {change(a)} - ${get_burrito(a)}")
   print(f"Toppings: {', '.join(map(str, a[7:len(a)+1]))} - ${get_toppings(a)}")
   print(f"Subtotal: ${get_protein(a)+get_rice(a)+get_beans(a)+get_burrito(a)+get_toppings(a)}")
   print(f"Discount Code: {a[2]}") 
   print(f"Total: ${apply_discount(a,get_protein(a)+get_rice(a)+get_beans(a)+get_burrito(a)+get_toppings(a))}") 
   print(f"You Save: ${get_protein(a)+get_rice(a)+get_beans(a)+get_burrito(a)+get_toppings(a)-(apply_discount(a,get_protein(a)+get_rice(a)+get_beans(a)+get_burrito(a)+get_toppings(a)))}") 
   print(f"Your order will be ready in {approximate_time(a)} minutes.")
   print(f"Enjoy your meal and have a good day!")

        
        



    
    