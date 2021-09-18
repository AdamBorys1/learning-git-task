shopping = {
    "piekarnia": ['chleb', 'bułka', 'pączek'],
    "warzywniak": ['cebula', 'buraki', 'seler']
}

for shop, product in shopping.items():
    product = [x.title() for x in product]
    print(f"Idę do {shop.capitalize()} i kupuję tam {product}")

number = int(len(shopping.get("piekarnia")) + int(len(shopping.get("warzywniak"))))
print(f"W sumie kupuję {number} produktów")

print("Tworzę drugi commit do wysłania")
print("Drugi commit został dodany, lecimy z trzecim :)")