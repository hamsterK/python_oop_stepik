def print_file_content(filename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print('Файл не найден')


print_file_content('Precepts_of_Zote2.txt')

