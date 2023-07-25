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
    parser.add_argument("--formats", help="To which formats the images will be converted", default='all', choices=['JPEG', 'PNG', 'all'])
    args = parser.parse_args()
    return args

def configure_paths_and_formats(args):
    if args.inputpath:
        inputdir = args.inputpath
    else:
        inputdir = "/"
    if args.outputpath:
        outputdir = args.outputpath
    else:
        outputdir = "/"
    if args.formats:
        if args.formats == 'all':
            formats = 'all'
        elif args.formats == 'JPEG':
            formats = 'JPEG'
        else:
            formats = 'PNG'    
    os.makedirs(outputdir, mode=0o777, exist_ok=True)
    return inputdir, outputdir, formats

def convert_images(inputdir, outputdir, formats):
    # Part of the pillow-heif package, needed to open the .heic/.heif as Pillow can't read them out of the box
    register_heif_opener()
    files = os.listdir(inputdir)
    for f in tqdm(files):
        if f.endswith(".HEIC"):
            inpath = os.path.join(inputdir, f)
            outpath = os.path.join(outputdir, f)
            print("Converting file: " + f)
            img = Image.open(inpath)
            if formats == 'all':
                img.save(outpath.replace(".HEIC", ".jpg"), format='JPEG')
                img.save(outpath.replace(".HEIC", ".png"), format='PNG')
            elif formats == 'JPEG':
                img.save(outpath.replace(".HEIC", ".jpg"), format=formats)
            else:
                img.save(outpath.replace(".HEIC", ".png"), format=formats)
            print("Succesfully converted")

args = create_argument_parser()
inputdir, outputdir, formats = configure_paths_and_formats(args)
convert_images(inputdir, outputdir, formats)