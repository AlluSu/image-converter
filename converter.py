from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm
import os

register_heif_opener()
files = os.listdir('./')
for f in tqdm(files):
    if f.endswith(".HEIC"):
        print("Converting file: " + f)
        img = Image.open(f)
        img.save("./converted-images/" + str(f).replace(".HEIC", ".jpg"), format="JPEG")
        img.save("./converted-images/" + str(f).replace(".HEIC", ".png"), format="PNG")
        print("Succesfully converted")
