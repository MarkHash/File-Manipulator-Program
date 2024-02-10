# File-Manipulator-Program
File-Manipulator-Program

This project is simple app that has various operation with files. The file operations include the following:

  - Reverse the file contents.
  - Copy the file contents.
  - Repeat the file contents.
  - Replace a word to new one.

### Repositories
* Create a directory for the project and initialize git with command `git clone https://github.com/MarkHash/File-Manipulator-Program.git`

### Environment Set up
* Download and install python if you don’t have it already.

### Deployment
* Run a folloing command for each file operations.
  - Reverse: `python3 file_manipulator.py reverse input_file_path output_file_path`
  - Copy: `python3 file_manipulator.py copy input_file_path output_file_path`
  - Repeat: `python3 file_manipulator.py duplicate-contents input_file_path n`, where n is the number to repeat.
  - Replace: `python3 file_manipulator.py replace-string input_file_path word new_word`, where `word` replaces to `new_word`.