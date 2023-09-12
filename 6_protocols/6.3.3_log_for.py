def log_for(logfile, date_str):
    with open(logfile, 'r', encoding='utf-8') as input_file, open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as output_file:
        for line in input_file:
            date, info = line.split(' ', maxsplit=1)
            if date == date_str:
                output_file.write(info)


with open('log.txt', 'w', encoding='utf-8') as file:
    print('2022-01-01 INFO: User logged in', file=file)
    print('2022-01-01 ERROR: Invalid input data', file=file)
    print('2022-01-02 INFO: User logged out', file=file)
    print('2022-01-03 INFO: User registered', file=file)

log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())
    