# Блок под номером 1 в терминологии блокчейн называется генезиз блоком и не содержит хэш

import json
import os
import hashlib

blockchain_dir = os.curdir + '/blocks/'


def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()

    return hashlib.md5(file).hexdigest()


def get_files():
        files = os.listdir(blockchain_dir)

        # sorted(list(map(int, files)))  # Третий метод
        # sorted(files, key=len)  # Второй метод сортировки

        return sorted([int(i) for i in files])


def check_integrity():
    # 1. Считать хэш предыдущего блока
    # 2. Вычислить хэш предыдущего блока
    # 3. Сравнить полученные данные
    files = get_files()
    results = []

    for file in files[1:]:
        h = json.load(open(blockchain_dir + str(file)))['hash']
        last_file = str(file - 1)
        actual_hash = get_hash(last_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        # print('Block {} is: {}'.format(last_file, res))

        results.append({'block': last_file, 'result': res})

    return results


def write_block(name, amount, to_whom, _hash=''):
    files = get_files()
    last_file = files[-1]
    filename = str(last_file + 1)
    # filename = str(int(last_file) + 1)  # Так же для второго метода сортировки
    _hash = get_hash(str(last_file))

    data = {
        'name': name,
        'amount': amount,
        'to_whom': to_whom,
        'hash': _hash
    }

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    # write_block('Eugene', 100000, 'VK')
    for i in check_integrity():
        print(i)


if __name__ == '__main__':
    main()
