file_path = './input1.txt'

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
        print("Sum in line:", count_sum(line))
        sum += int(count_sum(line))

print("Total Sum:", sum)
