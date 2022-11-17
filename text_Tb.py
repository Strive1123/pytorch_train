from torch.utils.tensorboard import SummaryWriter
from PIL import Image
import numpy as np
writer = SummaryWriter('logs')
image_path='data/train/bees_image/16838648_415acd9e3f.jpg'
image_PIL=Image.open(image_path)
image_array=np.array(image_PIL)
writer.add_image('test',image_array,2,dataformats='HWC')
for i in range(100):
    writer.add_scalar('y=2x',3*i,i)

writer.close()