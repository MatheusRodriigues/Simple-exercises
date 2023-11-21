import os

messages = []

name = input("name: ")

while True:
    
    # cleaning terminal
    os.system('cls')

    if len(messages) > 0:
        for m in messages:
            print(m['name'], '-', m['text'])
    
    print("-------------------------")

    # getting the texts
    text = input('message: ')
    if text == 'stop':
        break

    # adding message to list
    messages.append({
        'name': name,
        'text': text
    })
