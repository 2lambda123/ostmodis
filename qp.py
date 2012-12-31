#!/usr/bin/env python

#from pxpack import pack, unpack
#from numpy import array, float16, empty
#from quality import qp
#from random import uniform
from numpy import uint8

# def saturation(c):
# 	return (max(c) - min(c))
# 
# def darkness(c):
# 	return (3*255 - sum(c))/3

def qp(c):
	dark = (3*255 - sum(c))/3
	sat = (max(c) - min(c))
	#return uint8(uniform(0, 256))
	return 255 - (dark + sat)/2
	#return (saturation(c) + (darkness(c)/10))/2.0

# byte = 2**8
# 
# quality = empty((byte**3), dtype=float16)
# 
# #print pack((1, 2, 3))
# 
# for r in range(byte):
# 	for g in range(byte):
# 		for b in range(byte):
# 			color = (r, g, b)
# 			i = pack(color)
# 			quality[i] = qp(color)
# 			print qp(color)
