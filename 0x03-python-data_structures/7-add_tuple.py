#!/usr/bin/python3

def add_tuple(a=(), b=()):
    return (sum(a[:1] + b[:1]), sum(a[1:2] + b[1:2]))
