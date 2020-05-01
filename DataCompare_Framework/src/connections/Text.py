import os.path

class TextFileConnector():
    textfile = input("Enter the text File Path: ")

    if os.path.isfile(textfile):
        pass
    else:
        print("File Doesn't Exist")
        exit(0)
