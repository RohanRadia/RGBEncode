import cv2  # import video generating/encoding library
import os
from PIL import Image  # import image generating library

from Misc import to_ascii, to_three, encrypt  # import all miscellaneous functions from utils


class Encode:  # generate class
    def __init__(self, raw_data: str, encryption_key: str):  # constructor setup - runs basic code when class is
        # instantiated
        self.raw_data = raw_data  # class variable defined and assigned
        self.key = encryption_key  # class variable defined and assigned

        self.data = None  # class variable defined
        self.ascii_list = None  # class variable defined
        self.frames = []  # class variable defined

    def to_frames(self, size: int = 30):  # define required arguments
        a = 0  # define variable; counts current layer
        b = 0  # define variable; counts current row position
        count = 0  # define variable; counts amount of frames

        frame = Image.new('RGB', (size, size), "black")  # generate first frame
        pixels = frame.load()  # load the frame for editing

        for letter in self.ascii_list:  # for each letter in ascii_list class variable...
            if a is size-1 and b is size:  # if row is one less than size and position is at the end of the row...
                frame.save(f'frame{count}.png')  # save the frame
                self.frames.append(f'frame{count}.png')  # append the frame to the array
                count += 1  # increase the frame count by 1
                frame = Image.new('RGB', (size, size), "black")  # generate new frame
                pixels = frame.load()  # load the frame for editing
                a = 0  # reset the layer position
                b = 0  # reset the row position

            if b >= size:  # if row position is greater than the size
                a += 1  # increase layer position (move onto next layer)
                b = 0  # reset the row position (move to the front of the row)

            pixels[a, b] = tuple(letter)  # set the pixel at the current position to the ascii tuple
            b += 1  # increase the row position by one

        frame.save(f'frame{count}.png')  # save the frame
        self.frames.append(f'frame{count}.png')  # append the name of the frame to the frames list

    def to_video(self, file_name: str = "encoded"):  # define required arguments
        image_array = []  # define image_array variable

        for frame in self.frames:  # for each frame in class variable frames
            with open(frame, 'r') as f:  # open each frame and read, store in variable f
                img = cv2.imread(frame)  # define img variable and set value as cv2 imread() output of frame variable
                height, width, layers = img.shape  # make height, width and layers variables equal to output of img
                # shape attribute
                size = (width, height)  # size is equal to the width and height that were extracted from the frame
                image_array.append(img)  # append the image stored in the img variable to imgage_array
        print('above')
        if os.path.exists(f'{file_name}.mp4') is True:
            print('hit')
            file_increment = 1

            while os.path.exists(f"{file_name}{file_increment}.mp4"):
                print('hit')
                file_increment += 1

        else:
            file_increment = None
            file_increment = ''

        output = cv2.VideoWriter(f'{file_name}{file_increment}.mp4', 0x7634706d, 1, size)  # encode the base video as mp4

        for i in range(len(image_array)):  # for each value in the length of image_array, assign the value to i
            output.write(image_array[i])  # write to output the image in position i of image_array

        output.release()  # release software and hardware resources

        print(f'{file_name}{file_increment}.mp4')

    def run(self):  # define required arguments
        """Encrypt"""
        if len(self.key) is not 0:  # if the key provided is not empty then...
            self.data = encrypt(self.key, self.raw_data)  # encrypt the data and store it in the self.data variable
        else:  # else...
            self.data = self.raw_data  # make self.data equal to self.raw_data as not encryption needs to be applied

        """Ascii Triplets"""
        self.ascii_list = to_three(to_ascii(self.data))  # convert all the data to ascii, then split the ascii
        # values into smaller lists of 3, finally store the values in self.ascii_list

        """Generate Frames"""
        self.to_frames(30)  # generate frames

        """Generate Video"""
        self.to_video()  # generate video from frames

        """Delete Generated Frames"""
        for frame in self.frames:
            os.remove(frame)
