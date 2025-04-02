## variable declaration
input_symbols = 2
symbols = [0,1]
no_of_states = 5
initial_state = 0
final_state = 4
string = []

## Transition Table
rows, cols = no_of_states, input_symbols
matrix = [[0] * cols for i in range(rows)]

matrix[0][0] = 1
matrix[0][1] = 0
matrix[1][0] = 3
matrix[1][1] = 2
matrix[2][0] = 3
matrix[2][1] = 4 
matrix[3][0] = 3
matrix[3][1] = 3
matrix[4][0] = 1
matrix[4][1] = 4

## String Input and append them to list by casting their type to integer
input_string = input("Enter string: ")
for i in input_string:
    string.append(int(i))

## chaek the string valid or not
def check_acceptance():
    for i in string:
        if i not in symbols:
            return "Invalid String"
            break
    
    answer = check_string()
    return answer

def check_string():
    state = initial_state
    for i in range(len(string)):
        symbol = string[i]
        print(f'state = {state} , symbol = {symbol}')
        state = matrix[state][symbol]

    if state == 4:
        return ("Valid string")
    else:
        return ("Invalid String")
    
print(check_acceptance())
