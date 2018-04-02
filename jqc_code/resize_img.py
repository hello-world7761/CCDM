import os
import cv2
def resizeimg(filename, sourc):
	fopen = open(filename, 'r')
	s = filename.split('.')
	imgname = s[0]
	i = imgname.split('/')
	imgname2 = i[9]
	print(filename)
	img = cv2.imread(filename, -1)	
	size = (256, 256)
	result = cv2.resize(img, size)
	resultpath = os.path.join("/Users/jqc/Documents/study/CDMM/resize_trainingset/test_for_img", sourc)
	cv2.imwrite(resultpath, result)

def eachfile(filepath):
	pathdir = os.listdir(filepath)
	for s in pathdir:
		newdir = os.path.join(filepath, s)
		resizeimg(newdir, s)

eachfile("/Users/jqc/Documents/study/CDMM/第三届中国数据挖掘大赛数据集/第三届中国数据挖掘大赛-蝴蝶训练集/JPEGImages")