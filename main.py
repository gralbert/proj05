'''
Latin-rus decoder
'''

file_name = input('Enter the name of file:')

while True:
    try:
        with open(file_name, encoding='utf-8') as f_in:
            text = f_in.read()
            break
    except:
        file_name = input('Enter a valid filename:')
        continue

message = ''

while True:
    key = input('Enter the key symbol:')
    for num in range(0, len(text)):
        if text[num] == key:
            message += text[num + 1]
    if message != '':
        print(message)
        break
    else:
        print('The key symbol is wrong!')
