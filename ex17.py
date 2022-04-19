# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print(f"Copying from {from_file} to {to_file}")
#
# #we could do these two on one line, how?
# in_file = open(from_file) #indata = open(from_file).read()
# indata = in_file.read()
#
# print(f"The input file is {len(indata)} bytes long") #lenght - duzina, broj karaktera
#
# print(f"Does the output file exist? {exists(to_file)}") #f-ja exists izlazi kao "true" ili "false"
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()
#
# out_file = open(to_file, 'w') # da otvori text fajl u write mode
# out_file.write(indata)
#
# print("Alright, all done.")
#
#
# out_file.close()

# in_file.close()

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)