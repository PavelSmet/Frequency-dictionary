import lib_write
import os
"""
text = lib_write.input_from_file() #чтение файла text.txt и чистим от лишней пунктуации. Функция возвращает строку слов, разделенных пробелом 
lib_write.input_str(text) #принимает в качестве параметра строку, приводим к нижнему регистру, разбиваем на слова и записываем в словарь vocabulary.txt. Сделано ограничение по длине слова (от 3 символов)
lib_write.prepare() #сортировка словаря в алфавитном порядке
lib_write.spacedel() #удаление из словаря "переносы строки" (\n)
"""
# Указываем путь к директории
directory = "Vocabularys/"

# Получаем список файлов
files = os.listdir(directory)

# Выводим список файлов
print(*files, sep='\n')

Vocabulary_name = input("\nВведите имя словаря: ")
sorted_dict = lib_write.vfreq(Vocabulary_name) #создание питоновского частотного словаря
lib_write.vfreq_show(sorted_dict) #визуализация, вывод наиболее часто встречающихся слов


#прикрутить индексы к словарям
