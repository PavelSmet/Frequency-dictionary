import Freq_lib
import os
"""
text = Freq_lib.input_from_file() #чтение файла text.txt и чистим от лишней пунктуации. Функция возвращает строку слов, разделенных пробелом 
Freq_lib.input_str(text) #принимает в качестве параметра строку, приводим к нижнему регистру, разбиваем на слова и записываем в словарь vocabulary.txt. Сделано ограничение по длине слова (от 3 символов)
Freq_lib.prepare() #сортировка словаря в алфавитном порядке
Freq_lib.spacedel() #удаление из словаря "переносы строки" (\n)
"""
# Указываем путь к директории
directory = "Dictionaries/"

# Получаем список файлов
files = os.listdir(directory)

# Выводим список файлов
print(*files, sep='\n')

Vocabulary_name = input("\nВведите имя словаря: ")
sorted_dict = Freq_lib.vfreq(Vocabulary_name) #создание питоновского частотного словаря
Freq_lib.vfreq_show(sorted_dict) #визуализация, вывод наиболее часто встречающихся слов


#прикрутить индексы к словарям
