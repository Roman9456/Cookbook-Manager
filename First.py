def read_cookbook(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        cookbook = {}
        dish_name = ''
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.isnumeric():
                ingredients_count = int(line)
                cookbook[dish_name] = []
                for i in range(ingredients_count):
                    ingredient_line = f.readline().strip()
                    ingredient = parse_ingredient_line(ingredient_line)
                    cookbook[dish_name].append(ingredient)
            else:
                dish_name = line
    return cookbook
def get_shop_list_by_dishes(dishes, person_count):
    cookbook = read_cookbook('recipes.txt')
    shop_list = {}
    for dish in dishes:
        if dish in cookbook:
            ingredients = cookbook[dish]
            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if name not in shop_list:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}
                else:
                    shop_list[name]['quantity'] += quantity
        else:
            print(f"Блюдо '{dish}' не найдено в книге рецептов.")
    return shop_list

def parse_ingredient_line(line):
    parts = line.split(' | ')
    ingredient_name = parts[0]
    quantity = int(parts[1])
    measure = parts[2]
    return {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}

cookbook = read_cookbook('recipes.txt')
for dish, ingredients in cookbook.items():
    print(dish)
    for ingredient in ingredients:
        print(f"{ingredient['ingredient_name']}, {ingredient['quantity']}, {ingredient['measure']}")
    print()

shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for ingredient, data in shop_list.items():
    print(f"{ingredient}: {data['quantity']} {data['measure']}")