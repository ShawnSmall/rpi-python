#! /usr/bin/env python3

a = "hello\n" # \n is a newline character
b = "world"
a = a.strip() # this removes white space from both ends
print(f'{a} to the whole {b}.')
file = open("output.txt","a",buffering=1)
file.write(f'{a} to the whole {b}.')
file.close()




