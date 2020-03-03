desired_list = input("Which File do you wish to update: Tried or Wishlist? Enter 'T' or 'W': ")

if desired_list not in ['T', 'W']:
    print("You entered an invalid response. Please enter only 'T' or 'W'")

if desired_list == 'T':
    str_var = 'tried'
else:
    str_var = 'wishlist'

whiskey_update = input(f"Type the whiskey you wish to update whiskey_{str_var}.txt: ")

print("Bourbon/American, Scotch, Irish or Other?")
category = input("Enter: 'B', 'S', 'I' or 'O': ")

if category not in ['B', 'S', 'I', 'O']:
    print("You entered an invalid response. Please enter only 'B', 'S', 'I', 'O'")

with open("whiskey_tried.txt", "r+") as search:
    lines = search.readlines()
    lines_strip = [line.strip('\n') for line in lines]
    if desired_list == 'T':
        if whiskey_update not in lines_strip:
            for i, line in enumerate(lines):
                line = line[0]  # remove '\n' at end of line
                if category == line:
                    print(line, i)
                    break

            search.seek(0)
            lines.insert(i + 2, f"{whiskey_update}\n")
            search.writelines(lines)
        else:
            print("This whiskey already exists in the whiskey_tried file")

    else:
        if whiskey_update in lines_strip:
            print("You have already tried it! - It has not been added to your wishlist.")

with open("whiskey_wishlist.txt", "r+") as search:
    lines = search.readlines()
    lines_strip = [line.strip('\n') for line in lines]

    if desired_list == 'T':
        if whiskey_update in lines_strip:
            line_num = lines_strip.index(whiskey_update)
            del lines[line_num]
            search.seek(0)
            search.writelines(lines)
            print(f"{whiskey_update} was present in your wishlist, it has now been removed")
    else:
        if whiskey_update not in lines_strip:
            for i, line in enumerate(lines):
                line = line[0]  # remove '\n' at end of line
                if category == line:
                    print(line, i)
                    break

            search.seek(0)
            lines.insert(i + 2, f"{whiskey_update}\n")
            search.writelines(lines)

        else:
            print("This whiskey already exists in the whiskey_wishlist file")