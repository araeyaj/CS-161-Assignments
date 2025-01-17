x = int((input("Enter a whole positive integer: "))) #if input is not a positive whole number there will be a ValueError because, by definition, integers do not include decimal or fractional numbers

print(f"Decimal: {x}") #print x in decimal form
print(f"Binary: {bin(x)}") #print x in binary form
print (f"Hexadecimal: {hex(x)}") #print x in hexadecimal form

y = int(bin(x), 2)  #convert binary back to decimal integer
z = int(hex(x), 16) #convert hexadecimal back to decimal integer

w = x + y + z #add all 3 together in decimal form
print(f"The sum is {w}.")

print("" #add some space between the two
      "")

#COMPRESSION
original_size = 260 #set original text size variable
dictionary_size = 15 #set dictionary size variable
compressed_size = 200 #set compressed text size variable

compression_percent = (1 - ((compressed_size + dictionary_size)/original_size)) * 100 #use percent of compression formula to set compression percentage variable

#print each variable (including added total of compressed and dictionary)
print(f"Compressed text size: {compressed_size} characters")
print(f"     Dictionary size: {dictionary_size} characters")
print(f"               Total: {compressed_size+dictionary_size} characters")
print(f"  Original text size: {original_size} characters")
print(f"         Compression: {compression_percent}%")