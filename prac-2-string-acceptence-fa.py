states_count = 4
symbol_count = 2
initial_state = 1
accepting_state_count = 1
accepting_state = 2

rows, cols = states_count, symbol_count
transition_table = [[0] * cols for i in range (rows)] 

for i in range(rows):
    for j in range(cols):
        if j == 0:
            value = int(input(f"state from state {i+1} using symbol a: "))
        else:
            value = int(input(f"state from state {i+1} using symbol b: "))
        transition_table[i][j] = value

print("\n")
print("Transition Table Metrix: ")
print(transition_table)
print("\n")

input_string = "abbabab"
counter = 1

for i in input_string:

    if i == 'a':
        if counter == 1:
            answer = transition_table[initial_state-1][0]
            if answer == -1:
                print("String is not accepted by Finite Automata.")
                break
            else:
                print(f"reaching to {answer} by doing {initial_state} => a")
        else:
            index = answer
            answer = transition_table[answer - 1][0]
            if answer == -1:
                print("String is not accepted by Finite Automata.")
                break
            else:
                print(f"reaching to {answer} by doing {index + 1} => a")

    elif i == 'b':
        if counter == 1:
            answer = transition_table[initial_state-1][1]
            if answer == -1:
                print("String is not accepted by Finite Automata.")
                break
            else:
                print(f"reaching to {answer} by doing {initial_state} => b")
        else:
            index = answer
            answer = transition_table[answer - 1][1]
            if answer == -1:
                print("String is not accepted by Finite Automata.")
                break
            else:
                print(f"reaching to {answer} by doing {index+1} => b")
    else:
        print("String is not accepted as you have used a character other than allowed symbols")
        break
    counter = counter + 1
    

if counter-1 == len(input_string):
    print("\nString is accepted by Finite Automata")


    

