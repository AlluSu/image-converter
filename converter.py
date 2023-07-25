from PIL import Image
from pillow_heif import register_heif_opener
from tqdm import tqdm
import os
import argparse

def create_argument_parser():
    # Add arguments for the command line
    parser = argparse.ArgumentParser(description="Convert .HEIC images to .png and .jpg formats")
    parser.add_argument("--inputpath", help="Relative path to the folder of the images", default="/")
    parser.add_argument("--outputpath", help="Relative path to where the results will be stored", default="/converted-images")
    parser.add_argument("--formats", help="To which formats the images will be converted", default=['JPEG', 'PNG'], choices=['JPEG', 'PNG'])
    args = parser.parse_args()
    return args

def convert_images(args):
    # Part of the pillow-heif package, needed to open the .heic/.heif as Pillow can't read them
    register_heif_opener()

    formats = args.formats
    if args.outputpath:
        outputdir = args.outputpath
    else:
        outputdir = "/"
    if args.inputpath:
        inputdir = args.inputpath
    else:
        inputdir = "/"
    os.makedirs(outputdir, mode=0o777, exist_ok=True)
    files = os.listdir(inputdir)
    for f in tqdm(files):
        if f.endswith(".HEIC"):
            outpath = os.path.join(outputdir, f)
            inpath = os.path.join(inputdir, f)
            print("Converting file: " + f)
            img = Image.open(inpath)
            if not args.formats or len(formats) == 2:
                img.save(outpath.replace(".HEIC", ".jpg"), format=formats[0])
                img.save(outpath.replace(".HEIC", ".png"), format=formats[1])
            elif formats == 'JPEG':
                img.save(outpath.replace(".HEIC", ".jpg"), format=formats[0])
            else:
                img.save(outpath.replace(".HEIC", ".png"), format=formats[1])
            print("Succesfully converted")

args = create_argument_parser()
convert_images(args)