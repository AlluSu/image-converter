# Image converter prototype (WIP)  

## Background  
As an iOS user I had noticed that when sending photos taken with my iPhone to my personal laptop, the transferred images have an extension called *.HEIC*. However, this *.HEIC* format is not supported by some services or platforms, like for example *Nettiauto* and *Tori.fi*, when listing some items for sale. In the internet there is a variety of converters for this purpose, but I felt like trying to do my own and at the same time not use some random sketchy web-pages, which might collect or track some data related to the uploaded images or my device.  

## Functioning
- Clone the repository
- run *pip install -r requirements.txt*
- The *.HEIC* images should be in the same directory as the code
- After running the script, the converted image files are then transferred to a folder called *converted-images*
- The script converts every *.HEIC* image file to *.png* and *.jpg* images

## TODO:
- Use *argparse* library for the user to determine the location of the input images, determine the location for the output folder for the converted images and what extensions the user wants to convert  
- Study more about the *.HEIC* format, what does it contain and how it is formed  
- Check more throughly does the conversion have any side effects in, e.g., file size, image quality, metadata etc.  

