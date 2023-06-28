#relative path 
# absolute path
#file = open("./demo.txt","w")
file = open("./demo.txt","a")
file.write("\nHello World")
file.writelines(["\nHello World","\nHello World","\nHello World"])
file.writelines(["100","200","300"])
file.close()