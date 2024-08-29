# Cookbook Manager

## English

### Description
This project is a part of a larger system that manages a cookbook. It provides functionality to read recipes from a file, create a shopping list based on selected dishes, and print the contents of the cookbook.

### Features
- read_cookbook(filename): Reads recipes from a file and returns a dictionary representing the cookbook.
- get_shop_list_by_dishes(dishes, person_count): Generates a shopping list based on the selected dishes and the number of servings.
- parse_ingredient_line(line): Parses a line representing an ingredient and returns a dictionary with the ingredient's name, quantity, and measure.

### Usage
1. Call read_cookbook('recipes.txt') to load the cookbook from the 'recipes.txt' file.
2. Use the get_shop_list_by_dishes(['Dish1', 'Dish2'], 2) function to generate a shopping list for the specified dishes and number of servings.

## Russian

### Описание
Этот проект является частью более крупной системы, управляющей кулинарной книгой. Он предоставляет функциональность для чтения рецептов из файла, создания списка покупок на основе выбранных блюд и печати содержимого кулинарной книги.

### Возможности
- read_cookbook(filename): Читает рецепты из файла и возвращает словарь, представляющий кулинарную книгу.
- get_shop_list_by_dishes(dishes, person_count): Формирует список покупок на основе выбранных блюд и количества порций.
- parse_ingredient_line(line): Анализирует строку, представляющую ингредиент, и возвращает словарь с именем ингредиента, количеством и мерой.

### Использование
1. Вызовите read_cookbook('recipes.txt'), чтобы загрузить кулинарную книгу из файла 'recipes.txt'.
2. Используйте функцию get_shop_list_by_dishes(['Блюдо1', 'Блюдо2'], 2), чтобы сгенерировать список покупок для указанных блюд и количества порций.
