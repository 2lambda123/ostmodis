ostmodis
========

A quick, naive implementation of @celoyd's cloud-removal algorithm for satellite images. 

It was December of 2012 and I wanted some cloud-free satellite images. I thought 
"Hey, didn't @celoyd [do something like this](https://www.flickr.com/photos/vruba/8017203149/in/set-72157631622037685)? 
I should try implementing his approach!"
I hacked up what I could from the photo caption, then showed it to Charlie and he was kind enough to share his 
(more efficient, actually working) code -- buff-cube.py and pxpack.py are both straight from him and he released better public versions of them shortly thereafter.

If you want to remove clouds from your own images, you almost certainly want to use Charlie's [wheather](https://github.com/celoyd/wheather) instead of this 
-- it's more complete, more efficient, and infinitely better documented.




