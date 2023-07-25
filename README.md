# Image converter prototype (WIP)  

## Background  
As an iOS user I had noticed that when sending photos taken with my iPhone to my personal laptop, the transferred images have an extension called *.HEIC*. However, this *.HEIC* format is not supported by some services or platforms, like for example *Nettiauto* and *Tori.fi*, when listing some items for sale. In the internet there is a variety of converters for this purpose, but I felt like trying to do my own and at the same time not use some random sketchy web-pages, which might collect or track some data related to the uploaded images or my device.  

## Functioning
- Clone the repository
- run `pip install -r requirements.txt` (assumes you have *pip* installed)
- usage: `converter.py [-h] [--inputpath INPUTPATH] [--outputpath OUTPUTPATH] [--formats {JPEG,PNG,all}]`
    - You can run `python3 converter.py --help` on the command line to get the documentation how to use the command line arguments
    - All arguments are optional
- The script converts every *.HEIC* image file from the folder relative to the path of the program to *.png* and *.jpg* images in the folder 

## TODO:
- Study more about the *.HEIC* format, what does it contain and how it is formed  
- Check more throughly does the conversion have any side effects in, e.g., file size, image quality, metadata etc.  
