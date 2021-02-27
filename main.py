import os

filePath = input('Where would you like to save the file? \n')
fileName = input('What would you like to name the file? ')


userName = input('What is your name? ')
userAddress = input('What is your address? ')
userPhone = input('What is your phone number ')

completePath = filePath+fileName
if os.path.isfile(fileName): #check if file exists
  print('File Exists')
if os.path.isdir(filePath): #check if file path exists
  print('Directory Exists')
if os.path.exists(completePath): #check if complete path exists
  print('Complete path exists')
  print('Complete Path',completePath)
with open(completePath, 'w') as fileHandle: #open file for writing
  fileHandle.write("Data Written to file.") #write data to file
with open(completePath, 'r') as fileHandle: #open same file for Pythonreading
  data = fileHandle.read() #read data from the file
print(data)
with open(fileName, 'w') as file_object:
  file_object.write(userName)
  file_object.write(',''\n')
  file_object.write(userAddress)
  file_object.write(',''\n')
  file_object.write(userPhone)

with open(fileName, 'r') as file_object:
  contents = file_object.read()
print(contents)
