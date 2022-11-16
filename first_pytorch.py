from torch.utils.data import Dataset
from PIL import Image
import os
class MyData(Dataset):
    def __init__(self,root_dir,lable_dir):
        self.root_dir=root_dir
        self.lable_dir=lable_dir
        self.path=os.path.join(root_dir,lable_dir)
        self.image_path=os.listdir(self.path)

    def __getitem__(self, idx):
        image_name=self.image_path[idx]
        image_item_path=os.path.join(self.root_dir,self.lable_dir,image_name)
        img = Image.open(image_item_path)
        lable=self.lable_dir
        return img,lable
    def  __len__(self):
        return len(self.image_path)


root_dir='data/train'
target_dir='ants_image'
image_path=os.listdir(os.path.join(root_dir,target_dir))
label=target_dir.split('_')[0]
out_dir='ants_lable'
for i in image_path:
   file_name=i.split('.jpg')[0]
   with open(os.path.join(root_dir,target_dir,'{}.txt'.format(file_name))) as f:
       f.write(label)








