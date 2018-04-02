import os
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom

def resize_location(filename, sourc):
	tree = ET.parse(filename)
	root = tree.getroot()
	old_width = int(root[4][0].text)
	old_height = int(root[4][1].text)
	old_xmin = int(root[6][4][0].text)
	old_ymin = int(root[6][4][1].text)
	old_xmax = int(root[6][4][2].text)
	old_ymax = int(root[6][4][3].text)
	try:
		new_xmin = 256* old_xmin/ old_width
		new_xmax = 256* old_xmax/ old_width
		new_ymin = 256* old_ymin/ old_width
		new_ymax = 256* old_ymax/ old_width
	except ZeroDivisionError:
		new_xmin = 0
		new_ymin = 0
		new_xmax = 0
		new_ymax = 0

	root[4][0].text = '256'
	root[4][1].text = '256'
	root[6][4][0].text = str(new_xmin)
	root[6][4][1].text = str(new_ymin)
	root[6][4][2].text = str(new_xmax)
	root[6][4][3].text = str(new_ymax)

	resultpath = os.path.join("/Users/jqc/Documents/study/CDMM/resize_trainingset/resize_annotation_result", sourc)
	out_xml(root, resultpath)
def out_xml(root, dest):
    """格式化root转换为xml文件"""
    rough_string = ET.tostring(root, 'utf-8')
    reared_content = minidom.parseString(rough_string)
    with open(dest, 'w+') as fs:
        reared_content.writexml(fs)
    return True
def eachfile(filepath):
	pathdir = os.listdir(filepath)
	for s in pathdir:
		newdir = os.path.join(filepath, s)
		resize_location(newdir, s)
eachfile("/Users/jqc/Documents/study/CDMM/第三届中国数据挖掘大赛数据集/第三届中国数据挖掘大赛-蝴蝶训练集/Annotations")














































