'''
Week 02 Tic-Tac-Toe Assignment
Author: Nelson Familia
'''
left_up = 1
middle_up = 2 
right_up = 3
left_center = 4
middle_center = 5
right_center = 6
left_down = 7
middle_down = 8
right_down = 9
end = False

def player():
    count_x = 0
    count_o = 0
    global cells
    global end
    cells = [left_up, middle_up, right_up, left_center, middle_center, right_center, left_down, middle_down, right_down]
    for i in cells:
        if i == "x":
            count_x += 1
        elif i == "o":
            count_o += 1
    if (count_x + count_o) == 9:
        end = True
        print("\nIt's a tie\n")
    if count_x > count_o:
        player = "o"
    else:
        player = "x"
    return player
    
def validation(choice):    
    if cells[choice - 1] == "x" or cells[choice - 1] == "o":
        print()
        print("This cell is already used\nTry again!!")
        print()
        return False
    else:
        return True

def check_winner():
    global end
    if cells[0] == cells[1] and cells[1] == cells[2]:
        end = True
        print(f"Congratulations Player '{cells[0]}', You won'")
    elif cells[3] == cells[4] and cells[4] == cells[5]:
        end = True
        print(f"Congratulations Player '{cells[3]}', You won'")
    elif cells[6] == cells[7] and cells[7] == cells[8]:
        end = True
        print(f"Congratulations Player '{cells[6]}', You won'")
    elif cells[0] == cells[3] and cells[3] == cells[6]:
        end = True
        print(f"Congratulations Player '{cells[0]}', You won'")
    elif cells[1] == cells[4] and cells[4] == cells[7]:
        end = True
        print(f"Congratulations Player '{cells[1]}', You won'")
    elif cells[2] == cells[5] and cells[5] == cells[8]:
        end = True
        print(f"Congratulations Player '{cells[2]}', You won'")
    elif cells[0] == cells[4] and cells[4] == cells[8]:
        end = True
        print(f"Congratulations Player '{cells[0]}', You won'")
    elif cells[6] == cells[4] and cells[4] == cells[2]:
        end = True
        print(f"Congratulations Player '{cells[6]}', You won'")
    
def chart_changer():
    print()
    choice = int(input(f"Add an {player()} "))
    match choice:
        case 1:
            if validation(choice) == True:
                global left_up
                left_up = player()
        case 2:
            if validation(choice) == True:
                global middle_up
                middle_up = player() 
        case 3:
            if validation(choice) == True:
                global right_up
                right_up = player()
        case 4:
            if validation(choice) == True:
                global left_center
                left_center = player()
        case 5:
            if validation(choice) == True:
                global middle_center
                middle_center = player()
        case 6:
            if validation(choice) == True:
                global right_center
                right_center = player()
        case 7:
            if validation(choice) == True:
                global left_down
                left_down = player()
        case 8:
            if validation(choice) == True:
                global middle_down
                middle_down = player()
        case 9:
            if validation(choice) == True:
                global right_down
                right_down = player()
def main():    
    while end == False:
        print(f"{left_up}|{middle_up}|{right_up}\n-----\n{left_center}|{middle_center}|{right_center}\n-----\n{left_down}|{middle_down}|{right_down}")
        player()
        check_winner()
        if end == False:
            chart_changer()

if __name__ == "__main__":
    main() 