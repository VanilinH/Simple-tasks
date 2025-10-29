ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
eng = ['f', ',', 'd', 'u', 'l', 't', '`', ';', 'p', 'b', 'q', 'r', 'k', 'v', 'y', 'j', 'g', 'h', 'c', 'n', 'e', 'a', '[', 'w', 'x', 'i', 'o', ']', 's', 'm', "'", '.', 'z']

a = input("Введите текст: ")

translated_text = ""
for char in a:
    if char in ru:
        index = ru.index(char)
        translated_text += eng[index]
    elif char in eng:
        index = eng.index(char)
        translated_text += ru[index]
    else:
        translated_text += char

print(translated_text)
