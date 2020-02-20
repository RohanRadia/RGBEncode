import cv2

from Misc import from_ascii, from_three, decrypt


class Decode:  # generate class
    def __init__(self, video_name: str, encryption_key: str = " "):  # constructor setup - runs basic code when
        # class is instantiated
        self.video_name = video_name
        self.key = encryption_key  # class variable defined and assigned

        self.raw_data = None  # class variable defined and assigned
        self.frames = []  # class variable defined and assigned

    def from_video(self):  # define required arguments
        video = cv2.VideoCapture(f"{self.video_name}.mp4")

        success, image = video.read()

        count = 0
        while success:
            self.frames.append(f"frame{count}.jpg")
            cv2.imwrite(f"frame{count}.jpg", image)
            success, image = video.read()
            count += 1

    def from_frames(self):  # define required arguments
        pass

    def run(self):
        """Deconstruct Video To Frames"""

        """Deconstruct Frames To Ascii"""

        """Ascii To Letters"""

        """Save Text To Local .txt File"""

        """Delete Frames"""


a = Decode("encoded", "noting")
a.from_video()
print(a.frames)
