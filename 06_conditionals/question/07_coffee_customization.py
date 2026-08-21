coffee_size = input("\nEnter coffee size small/medium/large : ").strip().lower()
extra_shot = input("Extra shot? (yes/no): ").strip().lower()

# Validation
if coffee_size not in ["small", "medium", "large"]:
    print("Invalid coffee size")
    exit()

if extra_shot not in ["yes", "no"]:
    print("Please enter yes or no")
    exit()

print("\n===== ORDER DETAIL =====")
print(f"Coffee Size : {coffee_size}")
print(f"Extra Shot : {extra_shot}")

if extra_shot == "yes":
    print(f"Your Order : {coffee_size} coffee with an extra shot.")
else:
    print(f"Your Order : {coffee_size} coffee with no extra shot.")




'''
Isko aur todte hain

Ye

if coffee_size not in ["small", "medium", "large"]:

lagbhag yehi hai:

if (
    coffee_size != "small"
    and coffee_size != "medium"
    and coffee_size != "large"
):

Ye dono same kaam karte hain.

Lekin pehla wala

not in

bahut chhota aur readable hai.





in

Check karta hai ki koi value kisi list (ya collection) ke andar hai ya nahi.

Syntax:

value in collection



not in

Check karta hai ki koi value kisi list (ya collection) ke andar nahi hai.

Syntax:

value not in collection

'''