# decimaltoascii

This python script is a tool to convert decimal numbers (specifically numbers between 32-126) into their corresponding ASCII characters. Made this to solve the Nice Netcat flag on PicoCTF. 

NOTE: Lmaoooo i just found out, that there's a built-in way in Python to do this. smh. still had fun making this tho.

#essentially, this is how it would be done.
number = 97
ascii = chr(number)

print(ascii)
