import os
import csv


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {"series_1" : [], "series_2" : [], "series_3" : []}
        for row in reader:
            for key in row.keys():
                if key not in data:
                    data[key] = [int(row[key])]
                else:
                    data[key].append(int(row[key]))

        return data

# print(read_data("numbers.csv"))

# my_list = [1, 2, 3, 4]
# my_list[1], my_list[3] = my_list[3], my_list[1]
# print(my_list)
"""
def selection_sort(list):
    output = []
    i = 0
    for number in range(len(list)):
        if number[i] < list[i]:
            output.append(number)
        else:
            i += 1

    return output
"""
# print(selection_sort(read_data("numbers.csv")))

def selection_sort(list, direction="ascending"):
    for i in range(len(list)):
        min_idx = i
        for num_idx in range(i + 1, len(list)):
            if direction == "ascending":
                if list[min_idx] > list[num_idx]:
                    min_idx = num_idx
            elif direction == "descending":
                if list[min_idx] < list[num_idx]:
                    min_idx = num_idx

        list[i], list[min_idx] = list[min_idx], list[i]
        # list = list.pop(min_idx)
        # list.insert(i, list)

    return list

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

    return list

def insertion


def main():
    numbers = read_data("numbers.csv")
    sorted_series = selection_sort(numbers["series_1"])
    bubble = bubble_sort(numbers["series_1"])
    print(bubble)


if __name__ == '__main__':
    main()
