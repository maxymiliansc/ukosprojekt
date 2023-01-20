import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)


def add(file_path, add_text):
    file = read_file(file_path)
    file += add_text
    file += "\n"
    save_to_file(file_path, file)


def run_program(name, params):
    print(params)
    if params[0] == 'add':
        add("plik12.txt", params[1])


if __name__ == '__main__':
    args = sys.argv
    run_program('PyCharm', sys.argv[1:])

