def remove_signs(text):
    signs = [',', '.', '!', '?', ':', ';']
    for letter in text:
        if letter in signs:
            letter.remove()
    return text 

my_text = input('Enter your text: ')
print(remove_signs(my_text))