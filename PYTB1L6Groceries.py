import time
GroceryList = ["apples","bread","pasta","Sauce","lemonade"]
print("GroceryList")
for x in GroceryList:
  print(x)
  time.sleep(1)
  if x == "lemonade":
      continue

ShoppingCart = ["apples","bread","pasta"]
print("ShoppingCart")
for x in ShoppingCart:
    print(x)
    time.sleep(1)
    if x == "lemonade":
        break
if x== "lemonade" in ShoppingCart and GroceryList:
    print("Done shopping")
elif x== "apples" or "bread" or "pasta" or "Sauce":
    print("continue shopping")

