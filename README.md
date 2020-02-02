# RGBEncode
A method to change text into RGB based video/image files that can later be uploaded onto a video sharing website. An end user can download this file and decode it with the program on their side.

## Analysis
### The Problem
In an attempt to store my homework on a file storage site called MediaFire I was prompted with a message which announced that, 'No more storage remaining. Please upgrade your plan here: '. To save a file that was only 137 MB online the website was asking me to pay a monthly sum of £7. Sending this file via email would not be suitable as I needed to share it with a large group of people and the great aspect of storing it online in the cloud is you can send the end users a link and they can access it that way. 

Not being able to allocate money towards this purchase I decided to see if there was any way that I could share large amounts of data, ranging from a few megabytes to tens of gigabytes. The hope was to find an easy to use, portable, free way to share data with friends and family without any hassle or subscriptions. After watching a few YouTube videos I began to wonder how large each YouTube video much be and if there was a cost to uploading a video. In the end it turned out that uploading videos to platforms such as YouTube, Vimeo and Daily Motion was not only free but anyone could do it and there was no restriction to file sizes. You could essentially upload infinite amounts of data to the website. 

Creating videos of your work is tedious and can allow other people to read your data. The previous day I had been watching a video on the differences between OLED and LEDs and from that I explored the concept of how RGB colours worked. I came to the conclusion that I could turn text files in to video files by turning text into RGB pixels and then placing then on frames and finally into a video. This would mean at the end you could upload the video that is created to a place like YouTube or another free video uploading site, send the link to anyone you want to share the data with and they can decide it on their end.

### Stakeholders
The target audience for this project would range from school students to business men.

Having the ability to share large chunks of data is useful and a necessity for everyone. In universities students write lengthy essays and dissertations and this would allow them to send gigabytes of data to teachers and group members without facing restrictions due to email size limits and file sharing websites or even having to physically meet and hand over a USB file. Law firms have case files that are tens of thousands of pages long. Currently they print the data and transport it or they have send and receive this data via fax which requires a secretary to be present to handle the process (which can take several hours). Instead they would be able to convert it all into a  RGB video format and the data would be received in a matter of minutes.
### Existing Solutions
The only other existing solution that exists is a program called BitGlitter. It is a program created by a full stack developer called Mark. Not only does it change the text into RGB but it allows for the data to be encrypted to make it more secure and ensure only certain people would be able to see it. It has been created in Python and makes use of libraries such as PIL to edit images and FFMPEG to create videos from the RGB frames.

An example of the frames that are created look like the following:
 

The users of BitGlitter have a choice to use any of: 1, 2, 3, 4, 6 and 24 bits per colour. Although this allows users to have a greater range of choice when it comes to converting their text to pixels but only 24 bit will allow for the size of the RGB video/image to be the same size as the text file. Other options such as 1bit means that you have to use 8 pixels per letter and hence the size of the encoded video/image will be 8 times or more the size of the original file.

Users who aren’t technologically savvy will find it hard to operate the program. Command line program can function incorrectly/break if a single argument is entered incorrectly. For example when running Mark’s BitGlitter, the command you would run is, ‘python3 -m bitglitter write -file C://Users/Rohan/Desktop/doc.txt -mode video -o C://Users/Rohan/Desktop/Encrypted’. You can see that the command is quite tedious to write. Not only that but you can easily make a mistake and for many people this is very hard to use. My goal would be to make the program much more user friendly with an extensive GUI and folder/file selection GUI.

Some of BitGlitter key features include the ability to customise the amount of frames per second in the generated video. The reason for this feature is to cater to the different free video upload websites. For example YouTube has a cap of 60 frames per second and Vimeo has a cap of 120 frames per second. Another feature that the developers of BitGlitter have implemented is the ability to allow the user to choose the size of the frame. Once again there is a difference between many of the platforms. Some of them have a maximum size of 1920x1080 and others have a limit of 4096x2160. The final unique feature they have implemented is the ability to choose between creating a video of multiple frames or having all data put onto a single frame.

### Limitations
