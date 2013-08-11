import glob, time
from SimpleCV import Image, Color, Font

# put your images in the 'imgs' directory
files = glob.glob('./imgs/*')

for file in files:

    try:
        img = Image(file)

        area = img.area()
        
        # minimum and maximum areas for a cup relative to the image
        # proportions estimated and slightly expanded from real samples
        minsize = 0.0015 * area
        maxsize = 0.03 * area
    
        # super saturate pixels that most closely approximate red and invert image for blob detection
        im2 = img.hueDistance(color=Color.RED, minsaturation=200, minvalue=70).invert()
        # extract blobs within the specified size range
        blobs = im2.findBlobs(minsize=minsize, maxsize=maxsize)
    
    
        # if blob (i.e. cup) detected, draw blue rectangle according to its bounding box.
        if blobs:
            for blob in blobs:
                box = blob.mBoundingBox
                img.drawRectangle(box[0],box[1],box[2],box[3], color=Color.BLUE, width=5)
        else:
            # determine a reasonable location for text
            y = img.height / 2
            x = img.width / 2.5
            img.drawText('Nothing detected!', x=x, y=y, color=Color.WHITE, fontsize=45)
    
        display = img.show()
        time.sleep(5)
        display.quit()
        
    except Exception as e:
        print "File : %s, Error : %s" % (file, e)