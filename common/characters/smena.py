import os
from tqdm import tqdm

def process_file(file_path):
    # Получаем название файла без расширения
    file_name, _ = os.path.splitext(os.path.basename(file_path))

    # Открываем файл для чтения и записи
    with open(file_path, 'r+') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            # Находим строку с нужным условием
            if line.strip() == "cost = 100":
                # Ищем ближайшую строку сверху с названием файла
                j = i - 1
                while j >= 0:
                    if file_name in lines[j]:
                        # Обрезаем два последних символа и создаем новую строку
                        idea_token = lines[j].rstrip()[:-2]  
                        # Удаляем пробелы и табуляции перед "idea_token = "
                        idea_token = idea_token.strip()
                        # Вставляем новую строку после строки с условием с нужным отступом
                        lines.insert(i + 1, f"\t\t\tidea_token = {idea_token}\n")
                        break
                    j -= 1
        # Перемещаем указатель файла в начало и перезаписываем его
        file.seek(0)
        file.writelines(lines)

# Получаем путь к папке, содержащей скрипт
script_dir = os.path.dirname(os.path.abspath(__file__))
# Получаем список файлов в этой папке
files = os.listdir(script_dir)
# Фильтруем список файлов, оставляя только файлы с расширением ".txt"
files = [f for f in files if f.endswith('.txt')]

# Проходимся по всем найденным файлам с прогресс-баром
for file_name in tqdm(files, desc='Processing files'):
    # Создаем полный путь к файлу
    file_path = os.path.join(script_dir, file_name)
    # Обрабатываем файл
    process_file(file_path)
