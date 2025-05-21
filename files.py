# import os
# os.path.exists(file_path)
# os.path.isfile(file_path)

###


import csv
import json

file_path = "test.csv"
data_txt = "data :)"
data_json = {
    "data1": " data 1",
    "data2": " data 2",
    "data3": " data 3",
    "data4": " data 4",
}
data_csv = [["data1", 1, "1"], ["data2", 2, "2"], ["data3", 3, "3"], ["data4", 4, "4"]]

# w : write a file
# x : write if the file doesnt exist
# a : append data to a file
# r : read file


with open(file_path, "w") as file:
    file.write(data_txt)
    print(f"txt file '{file_path}' is created")

with open(file_path, "w") as file:
    json.dump(data_json, file, indent=4)
    print(f"json file '{file_path}' is created")

with open(file_path, "w", newline="") as file:
    writer = csv.writer(file)
    for row in data_csv:
        writer.writerow(row)
    print(f"csv file '{file_path}' is created")


# Reading files ###
# general read
try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Cant acces the file")
# json read
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content["data"])
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Cant acces the file")
# csv read
try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[2])
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("Cant acces the file")
