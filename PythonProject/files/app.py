# To open a file and store it in a variable
my_file=open('data.txt','r')
file_content=my_file.read()
# Close file after use
my_file.close()
 
print(file_content)
# or
# import fil_operations
# print(fil_operations.read_file('data.txt'))


name=input("Enter your name")
my_file_writing=open('data.txt','w')
# Content override because 'w' override always
my_file_writing.write(name)


my_file_writing.close()

