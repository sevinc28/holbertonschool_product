#!/usr/bin/python3
product1 = "alma"
product2 = "corek"
product3 = "sud"
print(f"file {product1}, {product2}, {product3}")

my_product = []
my_product.append(product1)
my_product.append(product2)
my_product.append(product3)
print(my_product)
my_product.append("su")
print("add succesfull")
def add_product(list, product=None):
    if product is None:
        print("Məhsul adı daxil edilməyib")
    else:
        list.append(product)
        print("Məhsul əlavə olundu")

add_product(my_product, "su")
add_product(my_product, "cay")
print(f"my_product: {my_product}")
print(f"my_product: {my_product}")
def remove_product(list):
    list.pop()
    print("Siyahı boşdur, silmək mümkün deyil")

