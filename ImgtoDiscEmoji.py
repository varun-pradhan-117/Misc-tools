import sys
import os
from PIL import Image
import cv2

try:
    #grab source and destination folders
    source=sys.argv[1]
    dest=sys.argv[2]
    print(source)
    print(dest)
    #check if source exists
    if not os.path.exists(source):
        print("Enter a valid Source.")
    #check if destination exists, else create it
    if not os.path.exists(dest):
        os.makedirs(dest)
    
    for fname in os.listdir(source):
        #get name without filetype
        clean_name=os.path.splitext(fname)[0]
        print(clean_name)
        img=Image.open(f'{source}{fname}')
        img.thumbnail((128,128))
        img.save(f'{dest}{clean_name}.png','png')
        print("Job's done")

except IndexError:
    print("Enter 2 folders as argument")
except:
    e = sys.exc_info()[1]
    print( "Error: %s" % e )
    
