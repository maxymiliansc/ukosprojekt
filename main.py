import sys


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.readlines()


def save_to_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)

def contains(file_path, data):
    contain_file = read_file(file_path)
    if data in contain_file:
        print("zawiera")
    else:
        print("Nie zawiera")

def add(file_path, add_text):
    file_contents = read_file(file_path)
    file_contents.append(add_text)
    save_to_file(file_path, "\n".join(file_contents))


def run_program(name, params):
    print(params)
    if params[0] == 'contains':
        contains("file.txt", params[1])
    if params[0] == 'add':
        add("file.txt", params[1])


if __name__ == '__main__':
    args = sys.argv
    run_program('PyCharm', sys.argv[1:])