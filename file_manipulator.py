import sys
from pathlib import Path

def reverse(argv):
    with open(argv[2], 'r') as input_file:
        contents = input_file.read()

    with open(argv[3], 'w') as output_file:
        output_file.write(contents[::-1])

def copy(argv):
    print("copy")
    with open(argv[2], 'r') as input_file:
        contents = input_file.read()

    file_name = Path(argv[3])
    file_name.touch(exist_ok=True)
    with open(file_name, 'w+') as output_file:
        output_file.write(contents)

def duplicate_contents(argv):
    with open(argv[2], 'r') as input_file:
        contents = input_file.read()

    with open(argv[2], 'a+') as input_file: 
        for i in range(int(argv[3])):
            input_file.write(contents)

def replace_string(argv):
    with open(argv[2], 'r') as input_file:
        contents = input_file.read()

    with open(argv[2], 'w+') as input_file:
        replaced_contents = contents.replace(argv[3], argv[4])
        input_file.write(replaced_contents)

command = sys.argv[1]
if command == "reverse":
    reverse(sys.argv)
elif command == "copy":
    print("copy")
    copy(sys.argv)
elif command == "duplicate-contents":
    duplicate_contents(sys.argv)
elif command == "replace-string":
    replace_string(sys.argv)

