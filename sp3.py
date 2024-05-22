Product = {}

def showfunction():
    print(Product.items())
    print("Name \t Product")
    for key in Product:
        print("{} \t {}".format(key,Product.get(key)))

while True:
    choice = int(input("1.  Add new product\n"
                       "2.  Search the product\n"
                       "3.  Display the product\n"
                       "4.  Edit the product\n"
                       "5.  Delete the product\n"
                       "6.  Exit\n"
                       "Please write number 1 - 6:"))
    if choice == 1:
        name = input("Product Name : ")
        price = input("Product Price : ")
        Product[name]= price

    elif choice ==2:
        product_name = input("Search the product :  ")
        if product_name in Product:
            print(product_name,"product price is ",Product[product_name])
        else:
            print("Not found the product")

    elif choice ==3:
        if not Product:
            print("Product is empty")
        else:
            showfunction()


    elif choice == 4:
        Editproduct = input("Edit your product :")
        if Editproduct in Product:
            price = input("Change your product price : ")
            Product[Editproduct] = price
            print("Product updated succesfully")
            showfunction()
        else:
            print("Name is not found")

    elif choice ==5:
        Del_product = input(" Which product do you want to Delete? : ")
        if Del_product in Product :
            Deletedconfirm = input("Do you want to delete this product y/n : ")
            if Deletedconfirm == "y" or Deletedconfirm == "Y":
                Product.pop(Del_product)
            showfunction()
        else:
            print("This name is not found in this product")

    else:
        break