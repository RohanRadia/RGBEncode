import cv2
from PIL import Image

from Utils.Misc import from_ascii, from_three, decrypt


class Decode:  # generate class
    def __init__(self, frame_name: str, encryption_key: str = " "):  # constructor setup - runs basic code when
        # class is instantiated
        self.frame_name = frame_name.rstrip()
        self.key = encryption_key  # class variable defined and assigned

        self.raw_data = None  # class variable defined and assigned
        self.three_list = []
        self.ascii_list = []
        self.encrypted_chars = ''
        self.decrypted_chars = ''

    """
    def from_video(self):  # define required arguments
        video = cv2.VideoCapture(f"{self.video_name}.mp4")

        success, image = video.read()

        count = 0
        while success:
            self.frames.append(f"frame{count}.png")
            cv2.imwrite(f"frame{count}.png", image)
            success, image = video.read()
            count += 1
    """

    def from_frame(self):  # define required arguments
        frame = Image.open(self.frame_name)
        pixels = frame.load()

        width, height = frame.size

        for x in range(height):
            for y in range(width):
                self.three_list.append(pixels[y, x])

    def run(self):
        """Deconstruct Video To Frames
        self.from_video()
        """

        """Deconstruct Frames To Ascii"""
        self.from_frame()
        self.ascii_list = from_three(self.three_list)

        """Remove All Null Values"""
        while self.ascii_list[-1] is 0:
            self.ascii_list.remove(0)

        """Ascii To Letters"""
        self.encrypted_chars = from_ascii(self.ascii_list)

        """Decrypt"""
        self.decrypted_chars = decrypt(self.encrypted_chars, self.key)

        """Save Text To Local .txt File"""
        with open("decoded.txt", 'w') as f:
            f.write(self.decrypted_chars)

        """Output Data"""
        return self.decrypted_chars
