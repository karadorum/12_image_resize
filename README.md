# Image Resizer

[TODO. There will be project description]

This script resizes an image according to user wishes. Script gets an image and required image size and returns a new image having required features.

How To Install
Python v3.5 should be already installed. Afterwards use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependecies:

`bash
pip install -r requirements.txt `# alternatively try pip3
Remember that it is recommended to use virtualenv/venv for better isolation.

Quick Start
An image file path is the positional argument of the script. An output directory path is the optional argument. By default the output image is saved in the directory of input image.

Moreover, user should set at least one of these arguments:

new image height (pixels number),
new image width (pixels number),
scale rate to resize an image.
To run script on Linux:
`bash
$ python image_resize.py /home/image.jpg --output_directory /home/img width_height --width 500 --height 400
The path of edited image: /home/img/image__500x400.jpg
Windows usage is the same.`

Project Goals
The code is written for educational purposes. Training course for web-developers - DEVMAN.org
