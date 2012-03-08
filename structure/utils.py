#coding: utf-8

from random import choice

def get_random_string(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
	"Generates a random password with the given length and given allowed_chars"
	# Note that default value of allowed_chars does not have "I" or letters
	# that look like it -- just to avoid confusion.
	return ''.join([choice(allowed_chars) for i in range(length)])