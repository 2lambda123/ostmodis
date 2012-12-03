from sys import argv, exit, path
path.append('/Library/Python') # or, y'know, fix your PYTHONPATH.
from PIL import Image
from numpy import *

def gridwalk((width,height)):
	for y in range(height):
		for x in range(width):
			yield(x,y)

if len(argv) < 3:
    exit('Usage: <input image>* <output image>. Output is a PNG.')

stacktype = float64
channel_max_val = 255
n = float(len(argv)-2) # -1 for our filename, -1 for the ouput file

imgnum = 0
for imgfile in argv[1:-1]:
	try: img = Image.open(imgfile)
	except: exit('Could not read "%s"!' % (imgfile))
	if imgnum == 0:
		stack = asarray(img).copy()
		stack.resize((n,) + stack.shape)
		stack = stack.astype(stacktype)
	
	else:
		if img.size != (stack.shape[2], stack.shape[1]): # img.size: (y,x). stack.shape: (z,x,y,rgb)
			exit('"%s" is not the same shape as the earlier images!' % (imgfile))
		
	stack[imgnum] = asarray(img)
	imgnum = imgnum + 1

for i,j in gridwalk(stack[0].shape[:-1]):
	px = stack[:,i,j]
	saturation = px.max(axis=1) - px.min(axis=1)
	darkness = 3*channel_max_val - px.sum(axis=1)
	quality = saturation + darkness/3
	stack[:,i,j] = px[quality.argsort()]

# Eventually, pick the sorted z-axis we want to export and call it 'bestz'.
bestz = 0 # FOR TESTING ONLY, FOOL

#outimg = Image.fromarray(stack[bestz].astype(uint8))
#outimg.save(argv[-1])
	
for i in range(stack.shape[0]):
	outimg = Image.fromarray(stack[i].astype(uint8))
	outimg.save(str(i)+argv[-1])
	
	