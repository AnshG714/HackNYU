#import camera
import scanner
import cv2
import os

pathname = ''
#camera.clickPic()
def readPicture():
    cam = cv2.VideoCapture(0)
    
    cv2.namedWindow("Click a picture!")
    
    img_counter = 0
    curr_img_name = ''
    while True:
        ret, frame = cam.read()
        cv2.imshow("test", frame)
        if not ret:
            break
        k = cv2.waitKey(1)
    
        if k%256 == 88 or k%256 == 120:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "opencv_frame_{}.png".format(img_counter)
            curr_img_name = img_name
            path = '/Users/sanja/Desktop/rec_pics'
            cv2.imwrite(os.path.join(path ,img_name), frame)
            print("{} written!".format(img_name))
            img_counter += 1
    
    cam.release()
    
    cv2.destroyAllWindows()
    # for file in os.listdir('/Users/anshgodha/Desktop/rec_pics'):
    #     os.remove('/Users/anshgodha/Desktop/rec_pics/'+file)
    filepath = '/Users/sanja/Desktop/rec_pics/' + curr_img_name
    pathname= filepath
    scanner.detect_text('/Users/sanja/Desktop/rec_pics/' + curr_img_name)
    
    
