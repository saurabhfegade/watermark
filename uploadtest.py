import os
from os import listdir
import PIL.Image
import PIL.ImageEnhance
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#####################################################################################################################################

def DriveDownload():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() 

    drive = GoogleDrive(gauth)
    os.makedirs('downloaded', exist_ok=True)
    def ListFolder(parent):
      filelist=[]
      file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
      for f in file_list:
        if (f['mimeType']=='application/vnd.google-apps.folder'): # Check if folder
            filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
            print('title: %s, id: %s, mimeType: %s' % (f['title'], f['id'], f['mimeType']))        
        else:
            filelist.append({"title":f['title'],"title1":f['alternateLink']})
            print('title: %s, id: %s, mimeType: %s' % (f['title'], f['id'], f['mimeType']))
      #return filelist
            filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
            file6 = drive.CreateFile({'id': f['id']})
            file6.GetContentFile(os.path.join('downloaded',"%s" %f['title']))

    ListFolder('0B0DHX3t01_6YVXpLdW9SRlVpVWM') # Specify the parameters as your folder id from which you want to download images
    #-->Right click on the folder-->Click on 'Get Shareable Link'-->Extreme left part is the folder id

######################################################################################################################################

def DriveUpload(dir1):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    new_folder = drive.CreateFile({'title':'{}'.format('test'),'mimeType':'application/vnd.google-apps.folder'}) #Creates a 
                                                                                                        #new folder on drive
    new_folder.Upload()
    fnames = listdir(dir1)
    for fname in fnames:
        if (fname.endswith(".jpg") or fname.endswith(".png")):
            nfile = drive.CreateFile({'title':os.path.basename(fname),'parents':[{u'id': new_folder['id']}]})
            nfile.SetContentFile(fname)
            nfile.Upload()
#####################################################################################################################################

def WaterMark(directory):
    dirListing = listdir(directory)  #enter directory/folder of the photos you want to add logo to.
    
    editFiles = []                                   #creates list which will fill up with all images from specified directory above.
    
    for item in dirListing:                          #loops through directory and fills list with .jpg and .png (specify according to user) .   
        if (item.endswith(".png") or item.endswith(".jpg")):
            editFiles.append(item)
    print (editFiles)
    print (len(editFiles))
    y=100
    os.makedirs('saved', exist_ok=True)

    for i in range (0, len(editFiles)):              
        # images
        
        base_path = editFiles[i]                    
        
        watermark_path = r'C:/Users/Rohit/Desktop/ieeelogo.png'                  #sepecify the path of the 1st logo here. 
        
        watermark_path2 = r'C:/Users/Rohit/Desktop/vitlogo.png'             #specify the path of the 2nd logo here.
        base = PIL.Image.open(base_path)            
        width, height= base.size
        watermark = PIL.Image.open(watermark_path)  
        wat1width, wat1height= watermark.size
        
        watermark2 = PIL.Image.open(watermark_path2)  
        wat2width, wat2height= watermark2.size
    
        # optional lightness of watermark from 0.0 to 1.0
        brightness = 0.5
        watermark = PIL.ImageEnhance.Brightness(watermark).enhance(brightness)
        watermark2 = PIL.ImageEnhance.Brightness(watermark2).enhance(brightness)
    
        # apply the watermark
        
        some_xy_offset = (int(width/192), int(height/54))                      # x and y cood of 1st logo
        some_xy2_offset = (int(width-width/4)-15, 10)                          # x and y cood of 2nd logo
    
        
        watermark=watermark.resize((int(width/9.66), int(height/7)))  #resizes logo image 
                                                                      
        watermark2=watermark2.resize((int(width/4),int(height/9.81)))
        
        # the mask uses the transparency of the watermark (if it exists)
        
        base.paste(watermark, some_xy_offset, mask=watermark)        #applies the logo 
        base.paste(watermark2, some_xy2_offset, mask=watermark2)     #applies the logo 
        
        base.save(os.path.join('saved','ImageWithLogo'+ str(y)+ '.png'))                    #name+ someNumber of saved image
        #base.show()                                                   #display each image
        y=y+1

##################################################################################################################################
method = int(input("Press 1 for drive and 2 for folder on pc:"))

if (method == 1):
    DriveDownload()
    directory = r"C:/Users/Rohit/Desktop/PyWatermark -PyDrive/downloaded"
    WaterMark(directory)
    dir1 = r"C:/Users/Rohit/Desktop/PyWatermark -PyDrive/saved"
    DriveUpload(dir1)
    
elif(method == 2):
    directory = r"C:/Users/Rohit/Desktop/PyWatermark -PyDrive"
    WaterMark(directory)

