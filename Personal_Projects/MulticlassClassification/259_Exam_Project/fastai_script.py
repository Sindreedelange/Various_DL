#!/usr/bin/env python
import sys
import os
import time

sys.path.append("../../../FastAi")
sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')

from fastai.imports import *
from fastai.transforms import *
from fastai.conv_learner import *
from fastai.model import *
from fastai.dataset import *
from fastai.sgdr import *
from fastai.plots import *

#  "/home/ros/catkin_ws/src/Various_DL/Personal_Projects/BinaryClassification/data/# models/Resnet34_multiclass"
path_to_model = "/home/ros/catkin_ws/src/Various_DL/Personal_Projects/MulticlassClassification/259_Exam_Project/Models/ResNext50_multiclass"
path_to_image = "/home/ros/catkin_ws/src/reading_images/images/"

arch = resnext50
sz = 299 # One of two standards for ImageNet (224)
bs = 32
PATH = "../data"

tfms = tfms_from_model(arch, sz, aug_tfms=transforms_side_on, max_zoom=1.1)
data = ImageClassifierData.from_paths(PATH, tfms=tfms, bs=bs, num_workers=4)
learn = ConvLearner.pretrained(arch, data, ps=0.3, precompute=False)

# Loader modellen som vi har trent opp fra før
learn.load(path_to_model)

trn_tfms, val_tfms = tfms_from_model(arch, sz)

def predict_image(full_image_path, learn, data, val_tfms):
	
	try:
		new_image_path = from_np_arr_to_jpg(full_image_path, data)
		predict_single_picture_jpg(new_image_path, data, learn, val_tfms)
	except:
		pass

def from_np_arr_to_jpg(image, data):

	image_load = np.load(image)
	arr2im = Image.fromarray(image_load)
	new_img_path = image[:-4] + ".jpg"
	arr2im.save(new_img_path)
	return new_img_path

def predict_single_picture_jpg(image, data, learn, val_tfms):
	image_load = open_image(image)
	im = val_tfms(image_load)
	learn.precompute=False
	preds_log = learn.predict_array(im[None])
	preds = np.exp(preds_log)
	predict = np.argmax(preds_log)
	classes = data.classes
	os.system("clear")
	print(classes[predict])
	
	os.remove(image)

	
while(True):
	if(len(os.listdir(path_to_image)) > 0): # Det er et bilde i mappen
		image_name = os.listdir(path_to_image)[0]
		full_image_path = path_to_image + image_name
		predict_image(full_image_path, learn, data, val_tfms)
	else: # Mappen er tom
		print("No image")
	time.sleep(0.1) 


