x = 31
print (x, bin(x), hex(x)) #converting to binary and hex numbers

#x = 1.825 #won't print because it's a "float" object which is not a whole integer
#print (x, bin(x), hex(x))
#changed to comment to not interfere with rest of program

#giving binary and hex values to variables to easily print
y = 0b1011
z = 0xA3
print(y, z)

#adding variable integers
w = x + y + z
print("the sum is ", w)

#setting variables
original_size = 300
dictionary_size = 35
compressed_size = 164
#used round function in equation to round within 2 digits
percent_compression = round(100 * (1 - ((compressed_size + dictionary_size) / original_size)), 2)

#f strings to embed the variables in strings
print(f"Compressed text size: {compressed_size} characters")
print(f"     Dictionary size: {dictionary_size} characters")
print(f"               Total: {int(dictionary_size + compressed_size)} characters")
print(f"  Original text size: {original_size} characters")
print(f"         Compression: {percent_compression}%")