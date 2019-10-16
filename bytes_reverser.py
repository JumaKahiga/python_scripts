my_file = open('sample.bin', 'rb')
inside_file = my_file.read()
print(inside_file)

file_data = bytearray(inside_file)
file_data.reverse()

print(file_data)


