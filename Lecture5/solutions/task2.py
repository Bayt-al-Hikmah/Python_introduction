from sys import argv
input_file = argv[1]
output_file = argv[2]
with open(input_file,"r") as inputFile:
    data = inputFile.read()
with open(output_file,"w") as outputFile:
    outputFile.write(data)