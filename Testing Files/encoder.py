import cv2
from PIL import Image


def file_to_text(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')

    return data


class Encoder:
    def __init__(self, text: str):
        self.text = text
        self.frames = []

    def text_to_ascii(self):
        RGB = []
        currentSequence = []

        for letter in self.text:
            if len(currentSequence) is 3:
                RGB.append(currentSequence)
                currentSequence = []

            try:
                if ord(letter) <= 255:
                    currentSequence.append(ord(letter))
                else:
                    print(f'Not a valid ascii character: {letter}')
            except Exception as e:
                pass

        if currentSequence is not []:
            RGB.append(currentSequence)

        while len(RGB[-1]) is not 3:
            RGB[-1].append(0)

        return RGB

    def ascii_to_rgb(self, size: int, ascii_list: list):
        a = 0
        b = 0
        count = 0
        print(ascii_list)

        frame = Image.new('RGB', (size, size), "black")
        pixels = frame.load()

        for letter in ascii_list:
            if a is size-1 and b is size:
                frame.save(f'frame{count}.png')
                self.frames.append(f'frame{count}.png')
                count += 1
                frame = Image.new('RGB', (size, size), "black")
                pixels = frame.load()
                a = 0
                b = 0

            if b >= size:
                a += 1
                b = 0

            pixels[a, b] = tuple(letter)
            b += 1

        frame.save(f'frame{count}.png')
        frame.show()
        self.frames.append(f'frame{count}.png')

    def rgbframes_to_video(self):
        image_array = []

        for frame in self.frames:
            with open(frame, 'r') as f:
                img = cv2.imread(frame)
                height, width, layers = img.shape
                size = (width, height)
                image_array.append(img)

        # output = cv2.VideoWriter('encoded.avi',cv2.VideoWriter_fourcc(*'DIVX'), 10, size)
        # output = cv2.VideoWriter('encoded.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 10, size)
        output = cv2.VideoWriter('encoded.mp4', 0x7634706d, 1, size)

        for i in range(len(image_array)):
            output.write(image_array[i])

        output.release()



#a = Encoder(file_to_text('Latin-Lipsum.txt')*100)
a = Encoder("I'm known as Mr Rohan Radia")
ascii_holder = a.text_to_ascii()

a.ascii_to_rgb(9, ascii_holder)

#a.rgbframes_to_video()
