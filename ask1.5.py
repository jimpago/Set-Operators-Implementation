#DIMITRIOS PAGONIS AM:4985
import csv
import sys
def read_file(file_path):
    
    with open(file_path, "r", encoding="utf-8") as file:
        data = [line.strip().split("\t") for line in file.readlines()]
    
    
    for row in data:
        row[1] = int(row[1])  
    return data

def write_back(file_path, data):
    
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(f"{row[0]}\t{row[1]}\n" for row in data)

def merge_sort_2d(arr):
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort_2d(arr[:mid])
    right_half = merge_sort_2d(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:  
            result.append(left[i])
            i += 1
        elif left[i][0] > right[j][0]:
            result.append(right[j])
            j += 1
        else:  
            combined_value = left[i][1] + right[j][1]
            result.append([left[i][0], combined_value])
            i += 1
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

def group_and_sort(matrix):
    
    sorted_matrix = merge_sort_2d(matrix)

    
    grouped_result = []
    for item in sorted_matrix:
        if grouped_result and grouped_result[-1][0] == item[0]:  
            grouped_result[-1][1] += item[1]
        else:
            grouped_result.append(item)

    return grouped_result


if len(sys.argv) != 3:
    print("Use the correct number of arguments!")
    sys.exit(1)


input_file = sys.argv[1]
output_file = sys.argv[2]


data = read_file(input_file)
sorted_grouped_data = group_and_sort(data)
write_back(output_file, sorted_grouped_data)

