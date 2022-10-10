# A handy way of opening files is to use with statements. You do not
# need to close a file explicitly in this case. Python closes it and
# releases the file resource at the end of the indented block:

file_path = 'lyrics.txt'
with open(file_path, 'r') as open_file:
	text = open_file.readlines()
