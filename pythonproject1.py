#project of Menu Bar for Select products in our budget


products={
    "apple":50,"banana":30,"orange":40,"grapes":40,"mangos":30,
    "pinapple":60,"pappaya":60,"watermelon":70,
}
p = int(input("Enter your total money: "))
print(f"You have ₹{p}")


cart=[]
while True:
    item=input("enter product to  add to cart(or type 'exit' to close): ").lower()
    if item == "exit":
        break


    if item in products:
        cart.append(item)
        print(f"{item} add to cart!")
    else:
        print(f"{item} is not available")



if not cart:
    print("Cart is empty!")
else:
    print("Your cart:", cart)


total=0
for item in cart:
    total += products[item]
print(f"\nTotal price: ₹{total}")


while total > p:
    print("\nYour products price is greater than your money!")
    print(f"Current total: ₹{total}, you have only ₹{p}")
    print("Your cart:", cart)
    b = input("Enter the product to remove: ").lower()

    if b in cart:
        cart.remove(b)
        total = sum(products[item] for item in cart)  # Recalculate total
        print(f"{b} removed! New total: ₹{total}")
    else:
        print(f"{b} is not in your cart.")

if total <= p:
    print("\nThank you for shopping!")
    print("Final cart:", cart)
    print(f"Total bill: ₹{total}")
