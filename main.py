# The Image Brightness Detection.
#
# References:
# http://alienryderflex.com/hsp.html
# https://www.whydomath.org/node/wavlets/imagebasics.html
#
# We say the above formula for y is a convex combination of r', g',
# and b' since the multipliers .299, .587, and .114 are non-negative and sum to one. Actually, this is exactly the
# formula suggested by the National Television System Committee (NTSC) for converting color feeds to black and white
# televisions sets.
#
# Notes:
# Develop a generalized algorithm to detect the brightness of any image. Your algorithm should take an image
# as input and give a score between (0-10) as output (zero being low bright and 10 being high bright).
#
#
# See the README file for information on usage.

import math
import sys
from pathlib import Path
import argparse

import numpy as np
from PIL import Image, ImageStat


def create_arg_parser():
    """"
    Creates and returns the ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description='Calculates image brightness on scale of 1 to 10.')
    parser.add_argument("--input_path", type=Path, help="Input image path")
    return parser


class ImageBrightnessDetect(object):
    """
    Input: Input RGB image file path
    Output: Level of brightness 1 to 10 (0 being low and 10 being the brightest)
    """

    def __init__(self, image_path):
        self.__image_path = image_path

    def classify(self):
        # File existence check
        my_file = Path(self.__image_path)
        if my_file.is_file():
            image = Image.open(self.__image_path)
            image.resize((1280, 720), Image.ANTIALIAS)
            return self.__calculate_level(image)
        else:
            return "File does not exist"

    @staticmethod
    def __calculate_level(image):
        # Creating bins for 10 levels between 0 to 255
        levels = np.linspace(0, 255, num=10)

        # Get average pixel level for each layer
        image_stats = ImageStat.Stat(image)
        red_channel_mean, green_channel_mean, blue_channel_mean = image_stats.mean

        # The three constants (.299, .587, and .114) represent the different degrees to which each of the primary (RGB)
        # colors affects human perception of the overall brightness of a color.  Notice that they sum to 1.

        image_bright_value = math.sqrt(0.299 * (red_channel_mean ** 2)
                                       + 0.587 * (green_channel_mean ** 2)
                                       + 0.114 * (blue_channel_mean ** 2))

        image_bright_level = np.digitize(image_bright_value, levels, right=True)

        return image_bright_level


if __name__ == "__main__":
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(sys.argv[1:])
    test = ImageBrightnessDetect(parsed_args.input_path).classify()
    print(test)
