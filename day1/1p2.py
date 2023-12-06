import re 

file_path = './input1.txt'

def replace_word_with_digit(line):
    digit_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    for key in digit_dict:
        if key in line:
            line = line.replace(key, str(digit_dict[key]))

    return line


def count_sum(line):
    a = 0
    b = len(line) - 1
    
    total_sum = ''
    
    a_found_digit = False
    b_found_digit = False
    
    while a <= b  and (not a_found_digit or not b_found_digit):
        if line[a].isdigit():
            a_found_digit = True
            total_sum = line[a]
        else:
            a += 1
        
        if line[b].isdigit():
            b_found_digit = True
            total_sum = total_sum + line[b]
        else:
            b -= 1
    
    return total_sum


sum = 0

with open(file_path, 'r') as file:
    for line in file:
        new_line = replace_word_with_digit(line)
        print(new_line)
        print("Sum in line:", count_sum(new_line))
        sum += int(count_sum(new_line))

print("Total Sum:", sum)
