import numpy as np
import os
from PIL import Image
import argparse

HISTGR_TR = 0.33

parser = argparse.ArgumentParser(description='First test task on images similarity.')    
    
parser.add_argument('--path', action="store", dest="path", help="folder with images", required=True)
    
dataset = parser.parse_args()                      #read dataset from arguments

def read_photo(image_dir: str) -> dict:         #Read images from directory 
                                                    #aggregate images in dict
    image_names = os.listdir(image_dir)
    
    images = [Image.open(os.path.join(image_dir, image_name)) for image_name in image_names]  
    
    return {q: i for q, i in zip(image_names, images)}


def photo_duplicate(img_1: Image, img_2: Image) -> bool:   #Check if RGB arrays are equal 
    
    if not np.array_equal(img_1.size, img_2.size):    # If images have different size they are not duplicates
        return False

    return np.array_equal(np.asarray(img_1), np.asarray(img_2))

if __name__ == '__main__':
   
    image_dict = read_photo(dataset.path)

    search_pair = []

    for img_name_1 in image_dict.keys():

        duplicate = []
        

        for img_name_2 in image_dict.keys():           
           
            if [img_name_2, img_name_1] in search_pair:      # Don't check images if they had been checked 
                continue
                
            if img_name_1 == img_name_2:                    # Don't check the same images
                continue

            if photo_duplicate(image_dict[img_name_1], image_dict[img_name_2]):  
                duplicate.append(img_name_2)
                search_pair.append([img_name_1, img_name_2])
                continue
            
            
        if len(duplicate) > 0:
            
            print('{}, {}'.format(img_name_1, (', ').join(duplicate)))

       
    