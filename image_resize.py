import argparse
import os
from PIL import Image



def check_positive_int(argument):
    value = int(argument)
    if value <= 0:
         raise argparse.ArgumentTypeError("{} is invalid. Must be positive number".format(argument))
    return value

def check_positive_float(argument):
    value = float(argument)
    if value <= 0:
         raise argparse.ArgumentTypeError("{} is invalid. Must be positive number".format(argument))
    return value


def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input_file_path', help='Enter a path of img file')
    parser.add_argument('-o', '--output_file_path', help='Enter a path to save output image')
    parser.add_argument('-w', '--width', type=check_positive_int, help='Enter a width of the output image')
    parser.add_argument('--height', type=check_positive_int, help='Enter a height of the output image')
    parser.add_argument('-s', '--scale', type=check_positive_float, help='Enter a scale ratio to resize an image')

    args = parser.parse_args()
    return args

def get_new_image_size(img, required_width, required_height, scale_ratio):
    image_width = img.width
    image_height = img.height

    if required_height and not required_width:
        scale = required_height / image_height
        required_width = int(image_width * scale)
    if not required_height and required_width:
        scale = required_width / image_width
        required_height = int(image_height * scale)
    if scale_ratio:
        required_height = int(image_height * scale_ratio)
        required_width = int(image_width * scale_ratio)
    return required_width, required_height

def get_img(path):
    try:
        input_img = Image.open(path)
        return input_img
    except FileNotFoundError:
        print('{} file not found'.format(path))
        return None

def get_new_image_path(input_img_path, new_directory, img_width, img_height):
    if new_directory:
        dir_path = os.path.dirname(new_directory)
    if not new_directory:
        dir_path = os.path.dirname(input_img_path)
    if not dir_path:
        dir_path = os.getcwd()

    input_image_full_name = os.path.basename(input_img_path)

    image_name, image_extension = os.path.splitext(input_image_full_name)

    new_image_name = '{}__{}x{}{}'.format(image_name, img_width, img_height, image_extension) 
    new_image_path = os.path.join(dir_path, new_image_name)
    return new_image_path
   
def check_proportions(old_img, new_img):
    old_proportion = old_img.width / old_img.height
    new_proportion = new_img.width / new_img.height
    proportion_difference = old_proportion - new_proportion
    small_proportion = 0.01
    return proportion_difference < small_proportion


if __name__ == '__main__':
  arguments = get_arguments() 
  height = arguments.height
  input_file_path = arguments.input_file_path
  width = arguments.width
  output_dir = arguments.output_file_path
  scale = arguments.scale
  

  if not height and not width and not scale:
      exit('At least one argument must be entered')

  image = get_img(input_file_path)
  if not image:
      exit('Can not open the file')

  new_width, new_height = get_new_image_size(image, width, height, scale)
  new_image = image.resize((new_width, new_height))
  proportion = check_proportions(image, new_image)
  output_file_path = get_new_image_path(
      input_file_path, output_dir, new_width, new_height
  )
  print(output_file_path)
  new_image.save(output_file_path)