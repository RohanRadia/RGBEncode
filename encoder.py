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

        frame.show()
        frame.save(f'frame{count}.png')
        self.frames.append(f'frame{count}.png')


a = Encoder(file_to_text('Latin-Lipsum.txt'))
ascii_holder = a.text_to_ascii()

a.ascii_to_rgb(30, ascii_holder)