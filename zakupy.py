shopping = {
    "piekarnia": ['chleb', 'bułka', 'pączek'],
    "warzywniak": ['cebula', 'buraki', 'seler']
}

for shop, product in shopping.items():
    product = [x.title() for x in product]
    print(f"Idę do {shop.capitalize()} i kupuję tam {product}")
