shopping_list = {
    "piekarnia": ["chleb", "bułki", "paczek"],
    "warzywniak": ["marchew", "seler", "rukola"]  
}
for shop, items in shopping_list.items():
    print(f"Idę do {shop.capitalize()} i kupuje tam {items}")
x=0
for shop, items in shopping_list.items():
    x=x + len(items)

print(f"W sumie kupuje {x} produktów")    