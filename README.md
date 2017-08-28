# Watermark
This script adds watermark(s) to the images stored within a folder on your system or on your google drive depending on what you select.
I have created 3 separate functions:

1.DriveDownload() - To download images from the folder specified by the folder id given as a parameter in ListFolder(). The downloaded images gets saved in a folder 'downloaded' in the default path.(The path where the script is saved).

2.WaterMark(directory) - It applies watermark to the images in the directory specified as a parameter and saves them in a folder 'saved' in the default path.

3.DriveUpload(dir1) - It uploads processed images from the 'saved' folder which is given as a parameter and uploads them to a new folder 'test' on your drive.
