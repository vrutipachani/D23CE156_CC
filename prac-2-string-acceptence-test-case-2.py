## variable declaration
no_of_symbols = 3
list_of_symbols = [0,1,2]  ## 0:a, 1:b, 2:c
no_of_states = 7
initial_state = 0
no_of_accepting_state = 4
accepting_states = [0,2,4,6]
string = []

## input string function
def take_input():
    input_string = input("Enter your string: ")
    for i in input_string:
        if(i == 'a'):
            string.append(0)
        elif(i == 'b'):
            string.append(1)
        elif(i == 'c'):
            string.append(2)
        else:
            print("Invalid input")
            return
    check_string()

## Transition table
rows, cols = no_of_states, no_of_symbols

transition_table = [[0] * cols for i in range(rows)]

transition_table [0][0] = 1
transition_table [0][1] = 3
transition_table [0][2] = 5
transition_table [1][0] = 2
transition_table [1][1] = 3
transition_table [1][2] = 5
transition_table [2][0] = 2
transition_table [2][1] = 3
transition_table [2][2] = 5
transition_table [3][0] = 3
transition_table [3][1] = 4
transition_table [3][2] = 3
transition_table [4][0] = 3
transition_table [4][1] = 4
transition_table [4][2] = 3
transition_table [5][0] = 5
transition_table [5][1] = 5 
transition_table [5][2] = 6
transition_table [6][0] = 5
transition_table [6][1] = 5
transition_table [6][2] = 6

##checking string

def check_string():
    state = initial_state
    for i in range(len(string)):
        symbol = string[i]
        print(f"state: {state}, symbol: {symbol}")
        state = transition_table[state][symbol]

    if state in accepting_states:
        print("String is accepted")
    else:
        print("String is not accepted")

take_input()