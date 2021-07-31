#Python program to get extension from a filename

filename = input("Input the filename with extension: ")
f_extns = filename.split(".")
print ("The extension of the file is : " + repr(f_extns[-1]))
