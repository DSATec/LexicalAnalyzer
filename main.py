# input = 'input.txt'

def read_file_line_by_line(file_path: str) -> None:
    file = open(file_path, 'r')
    # read file line by line
    for line in file:
        for char in line:
            print(char, end='')
    file.close()

read_file_line_by_line('input.txt')
