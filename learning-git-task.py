shopping_list = {
    "piekarnia": ["chleb", "bułki", "paczek"],
    "warzywniak": ["marchew", "seler", "rukola"]  
}
for shop, items in shopping_list.items():
    print(f"Idę do {shop.capitalize()} i kupuje tam {items}")