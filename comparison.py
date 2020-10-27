#! /usr/bin/env python3

i = int(1)
f = float(1)
s = str("1")

if (i == f):
    print("int equals float")

if (i == s):
    print("int equals string")

if (f == s):
    print("float equals string")

if (f == float(s)):
    print("float equals float(string)")


if (i):
    print("int is TRUE")

if (f):
    print("float is TRUE")

if (s):
    print("string is TRUE")

if (u):
    print("undefined is TRUE")


