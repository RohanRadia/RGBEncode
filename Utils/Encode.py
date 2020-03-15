import cv2  # import video generating/encoding library
import math
import os  # import operating system interaction library
from PIL import Image  # import image generating library

from Misc import to_ascii, to_three, encrypt  # import all miscellaneous functions from utils


class Encode:  # generate class
    def __init__(self, raw_data: str, encryption_key: str):  # constructor setup - runs basic code when class is
        # instantiated
        self.raw_data = raw_data  # class variable defined and assigned
        self.key = encryption_key  # class variable defined and assigned

        self.data = None  # class variable defined
        self.ascii_list = None  # class variable defined

    def to_frame(self):  # define required arguments
        row = 0
        row_max = math.ceil(math.sqrt(len(self.raw_data)))

        column = 0
        column_max = math.ceil(math.sqrt(len(self.raw_data)))

        if row_max < 1:
            row_max = 1

        if column_max < 1:
            column_max = 1

        frame = Image.new('RGB',
                          (column_max, row_max),
                          'black')
        pixels = frame.load()

        for letter in self.ascii_list:
            pixels[column, row] = tuple(letter)

            column += 1

            if column is column_max-1:
                row += 1
                column = 0

        frame.save("frame.png")

    def run(self):  # define required arguments
        """Encrypt"""
        if len(self.key) is not 0:  # if the key provided is not empty then...
            self.data = encrypt(self.raw_data, self.key)  # encrypt the data and store it in the self.data variable
        else:  # else...
            self.data = self.raw_data  # make self.data equal to self.raw_data as not encryption needs to be applied

        """Ascii Triplets"""
        self.ascii_list = to_three(to_ascii(self.data))  # convert all the data to ascii, then split the ascii
        # values into smaller lists of 3, finally store the values in self.ascii_list

        """Generate Frame"""
        self.to_frame()  # generate frames
