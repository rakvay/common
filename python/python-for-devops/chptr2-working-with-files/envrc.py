# The tool direnv is used to automatically set up some development
# environments. You can define environment variables and application
# runtimes in a file named .envrc

text = '''export STAGE=PROD
export TABLE_ID=token-storage-1234'''
with open('.envrc', 'w') as opened_file:
	opened_file.write(text)
