#!/usr/bin/python3
'''
A python3 script to generate memory addresses based on hex input

author: Haoxi Tan
email: haoxi.tan@gmail.com
'''

import sys


def little_endian(addr):
    '''
    converts memory address into hex in reverse
    '''
    hex_list = []
    addr = addr.lstrip("0x")
    try:
        for i in range(0,len(addr),2):
            hex_list.append(addr[i]+addr[i+1])

    except IndexError:
        print("IndexError - your address is invalid (must be even in length)")

    hex_list.reverse()
    print ('\\x' + '\\x'.join(hex_list))

def big_endian(addr):
    '''
    converts memory address into hex in order
    '''
    hex_list = []
    addr = addr.lstrip("0x")
    try:
        for i in range(0,len(addr),2):
            hex_list.append(addr[i]+addr[i+1])

    except IndexError:
        print("IndexError - your address is invalid (must be even in length)")

    print ('\\x' + '\\x'.join(hex_list))


if __name__ == "__main__":

    usage = ("""
    Usage:
    {0} [options...] <address>
    options:
    -l  little endian
    -b  big endian

    default is little endian if no option specified

    example:
    {0} 0xdeadbeef
    {0} -l 0x12345678

    author: Haoxi Tan
    email: haoxi.tan@gmail.com
    """.format(sys.argv[0]))


    if len(sys.argv) <= 1 or sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print(usage)

    elif sys.argv[1] == "-l":
        little_endian(sys.argv[2])
    elif sys.argv[1] == "-b":
        big_endian(sys.argv[2])

    else:
        little_endian(sys.argv[1])