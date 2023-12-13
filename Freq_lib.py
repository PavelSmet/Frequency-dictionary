import string
import matplotlib.pyplot as plt

def spacedel():
  with open('Vocabularys/Vocabulary.txt', 'r') as file_read:
    Words = file_read.readlines() #построчное считывание файла в список
  while '\n' in Words:
      Words.remove('\n')
  with open('Vocabularys/Vocabulary.txt', 'w') as file:
    for word in Words:
      file.write(word)
  
def prepare():
  with open('Vocabularys/Vocabulary.txt', 'r') as file_read:
    lines = file_read.readlines()
  sort_list = list(lines)
  sort_list.sort()
  with open('Vocabularys/Vocabulary.txt', 'w') as file_write:
    for word in sort_list:
      file_write.write(word)
  return sort_list

def input_str(text):
  text = text.lower() #приведение строки к нижнему регистру
  Words = []
  tmp_word = ""
  for i in range(len(text)):
    if text[i] == " ":
      Words.append(tmp_word) #формируем слово и в случае достижения пробела добавлем его в список Words
      tmp_word = ""
    else:
      tmp_word += text[i]
    if i == len(text) - 1: #добавляем слово в список Words в случае достижения конца строки
      Words.append(tmp_word)
  with open('Vocabularys/Vocabulary.txt', 'a') as file:
    for word in Words:
      if len(word) >= 3:
        file.write(word + '\n')

def input_from_file():
  with open("Texts/text.txt", "r") as file_stream:
    lines = file_stream.readlines() #построчное чтение файла в список
  #for i in range(len(lines)):
    #lines[i] = lines[i].strip() #с помощью функции strip мы лечили что-то, но не помним что (разделение строки на слова)
  joined_string  = " ".join(lines) #объединение списка в строку
  clear_dict = joined_string.maketrans("", "", string.punctuation + "—" + "«" + "»" + "…") #первый параметр меняем на второй (пустые строки), 3 параметр удаляем
  line = joined_string.translate(clear_dict) #возвращает строку с заменами и удалением подстрок из 3го параметра
  return line
  
    #разобраться со структурой "словарь"
    #что такое функция! и что такое метод!

def vfreq(Vocabulary_name): #функция создания часточного словаря python
  with open ("Vocabularys/" + Vocabulary_name, 'r') as file_read:
    V = file_read.readlines()
  V = [line.rstrip() for line in V]
  V_key = []
  V_value = []
  count = 1
  V_key.append(V[0])
  for i in range(len(V) - 1):
    if V[i+1] == V[i]:
      count = count + 1
    else:
      V_value.append(count)
      V_key.append(V[i+1])
      count = 1
  V_value.append(count) # сформирован частотный словарь, состоящий из ключа(слово) и значения(частота)
  new_dict = dict(zip(V_key, V_value)) #создание питоновского словаря и помещение туда значений
  sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse = True)) #сортировка словаря по значению (в обратном порядке)
  #for k, v in sorted_dict.items():
    #print(f"{k} - {v}")
  return sorted_dict

def vfreq_show(sorted_dict):
  words = list(sorted_dict.keys())[0:20]
  freqs = list(sorted_dict.values())[0:20]

  fig, axs = plt.subplots(1, 1, figsize=(9, 3), sharey=True)
  axs.barh(words, freqs)
  axs.invert_yaxis()
  #axs[1].scatter(words, freqs)
  #axs[2].plot(words, freqs)
  fig.suptitle('Частотный словарь')
  plt.show()
