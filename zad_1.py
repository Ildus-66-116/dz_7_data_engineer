"""Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:

a. Принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. Принимать параметр количество цифр в порядковом номере.
c. Принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. Принимать параметр расширение конечного файла.
e. Принимать диапазон сохраняемого оригинального имени. Например, для диапазона [3, 6] берутся буквы с 3 по 6
    из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано.
    Далее счётчик файлов и расширение.
f. Папка test_folder доступна из текущей директории"""

import os


def rename_files(desired_name, num_digits, source_ext, target_ext, name_range=(3, 5)):
    files = os.listdir('test_folder')
    filtered_files = [file for file in files if file.endswith(source_ext)]
    filtered_files.sort()
    num = 1
    for file in filtered_files:
        name = os.path.splitext(file)[0]
        if name_range:
            name = name[name_range[0] - 1:name_range[1]]
            new_name = name + desired_name + str(num).zfill(num_digits) + '.' + target_ext
        else:
            new_name = desired_name + str(num).zfill(num_digits) + '.' + target_ext
        path_old = os.path.join(os.getcwd(), 'test_folder', file)
        path_new = os.path.join(os.getcwd(), 'test_folder', new_name)
        os.rename(path_old, path_new)
        num += 1


if __name__ == '__main__':
    rename_files(desired_name="new_file_", num_digits=2, source_ext="txt", target_ext="doc")
