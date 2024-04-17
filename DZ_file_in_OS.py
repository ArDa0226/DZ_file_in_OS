
import time, os

directory = 'C:\\Users\\Артур\\PycharmProjects\\probe\\Work_of_files\\DZ_work_of_files\\'

for root, dirs, files in os.walk(directory):
    print(root, dirs, files)
    for file in files:
        full_path = os.path.join(root, file)
        times = os.path.getmtime(full_path)
        f_t = time.strftime("%d.%m.%Y%H:%M", time.localtime(times))
        file_size = os.path.getsize(file)
        pat_dir = os.path.dirname(__file__)
        print(f'Обнаружен файл: {file} , Путь: {full_path} , Размер: {file_size} байт, Время изменения: {f_t}, Родительская директория: {pat_dir}')