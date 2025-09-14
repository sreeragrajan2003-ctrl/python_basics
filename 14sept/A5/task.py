favourites = ["pizza", "chocolate", "sushi", "ice cream", "pasta"]
print("My favourite food:\n")
for i in range(0, len(favourites)):
    print(f"{i+1}. {favourites[i]}")


length = int(input("Enter the length of the list: "))
items = []
for i in range(length):
    element = input(f"Enter element {i+1}: ")
    items.append(element)

items.reverse()
print(",".join(items))

list_my = []
print(" Shopping List Manager\n1. Add item\n2. Remove item\n3. Show_list\n4. Check item\n5. Exit")
loop = True
while loop == True:
    key = int(input("Enter a option: "))
    if key == 1:
        item = input("Enter the name of the item: ")
        list_my.append(item)
        print(f"Added '{item}' to the list.")
    elif key == 2:
        remove_item = input("Enter the name of the item to be removed: ")
        if remove_item in list_my:
            list_my.remove(remove_item)
        else:
            print("No such item")
    elif key == 3:
        print("Shopping list manager:\n")
        for item in range(len(list_my)):
            print(f"{item+1}. {list_my[item]}")
    elif key == 4:
        check_item = input("Enter the name of the item to be checked: ")
        if check_item in list_my:
            print(f"Item is in position {int(list_my.index(check_item))+1} ")
        else:
            print("item not present")
    elif key == 5:
        loop = False
        print("exiting list")
        break
    else:
        print("Invalid input")


print("Enter your top 5 movies: ")
movies = []
rating = []
for i in range(0, 5):
    movie = input(f"Enter No.{i+1} movie: ")
    movies.append(movie)
    rate = float(input("rating of movie(1-10): "))
    rating.append(rate)

for j in range(0, 5):
    for k in range(j+1, 5):
        if rating[j] < rating[k]:
            rating[j], rating[k] = rating[k], rating[j]
            movies[j], movies[k] = movies[k], movies[j]
    print(f"{j+1}. {movies[j]}- {rating[j]}")

print(
    f"Highest rated movie= {movies[0]}-{rating[0]}\nLowest rated movie= {movies[-1]}-{rating[-1]}")
