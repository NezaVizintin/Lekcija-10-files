with open("file.csv", "r") as csv_file:
    rows = csv_file.read().splitlines()

    for row in rows:
        row_data = row.split(",")
        name = row_data[0]
        age = row_data[1]
        str1 = "is"
        str2 = "years old "
        str3 = "and"
        print(f"{name} {str1} {age} {str2} {str3} {row_data[2]}")
