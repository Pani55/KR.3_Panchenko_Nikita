import json


def open_file__extract_info():
    with open("operations.json", 'r') as file:
        temp = json.load(file)

        for line in temp:
            if "state" not in line:
                temp.remove(line)
            else:
                if line["state"] == "CANCELED":
                    temp.remove(line)
                else:
                    continue

    return temp
