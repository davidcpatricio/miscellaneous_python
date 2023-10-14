line_1 = input("Line 1: ")
line_2 = input("Line 2: ")
line_3 = input("Line 3: ")
line_4 = input("Line 4: ")
line_5 = input("Line 5: ")
line_6 = input("Line 6: ")
line_7 = input("Line 7: ")
line_8 = input("Line 8: ")
line_9 = input("Line 9: ")

lines = [
    line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9
]

columns = ['', '', '', '', '', '', '', '', '']

for line in lines:
    line = line.strip()
    if len(line) != 9:
        print('All lines must contain only digits.')
        exit()
    elif not line.isdigit():
        print('Each line must contain exactly 9 digits.')
        exit()
    elif '0' in line:
        print('All digits must be in range (1-9).')
        exit()
    else:
        for i in range(len(line)):
            columns[i] += line[i]

tile_1 = line_1[:3] + line_2[:3] + line_3[:3]
tile_2 = line_1[3:6] + line_2[3:6] + line_3[3:6]
tile_3 = line_1[6:] + line_2[6:] + line_3[6:]
tile_4 = line_4[:3] + line_5[:3] + line_6[:3]
tile_5 = line_4[3:6] + line_5[3:6] + line_6[3:6]
tile_6 = line_4[6:] + line_5[6:] + line_6[6:]
tile_7 = line_7[:3] + line_8[:3] + line_9[:3]
tile_8 = line_7[3:6] + line_8[3:6] + line_9[3:6]
tile_9 = line_7[6:] + line_8[6:] + line_9[6:]

tiles = [
    tile_1, tile_2, tile_3, tile_4, tile_5, tile_6, tile_7, tile_8, tile_9
]


def not_sudoku():
    print('No')
    exit()


def checking(sequence):
    for section in sequence:
        checklist = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for digit in section:
            if digit in checklist:
                checklist.remove(digit)
            else:
                not_sudoku()


checking(lines)
checking(columns)
checking(tiles)


# for line in lines:
#     check_line = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for digit in line:
#         if digit in check_line:
#             check_line.remove(digit)
#         else:
#             not_sudoku()

# for column in columns:
#     check_column = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for digit in column:
#         if digit in check_column:
#             check_column.remove(digit)
#         else:
#             not_sudoku()

# for tile in tiles:
#     check_tile = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for digit in tile:
#         if digit in check_tile:
#             check_tile.remove(digit)
#         else:
#             not_sudoku()

print('Yes')
