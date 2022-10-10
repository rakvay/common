# You can also read a file using the readlines method. This method
# reads the file and splits its contents on newline characters. It returns a
# list of strings. Each string is one line of the original text:
file_path = 'lyrics.txt'
open_file = open(file_path, 'r')
text = open_file.readlines()
len(text)
open_file.close()
