import popupMessage as pop
import least_square_plane as lsp
import image_stitching as ist
import cv2 as cv

msg = "CPS843 Assignment 2\n\nAuthors:\nMark Volfson - 500740834\nMichael Teitelbaum - 500747561\n\nThank you for your time!\n\nPress okay to continue..."
pop.popupmsg(msg)

msg = "In this assignment there are only 2 outputs:\n 1. A textbox asnwering question 1.3\n 2. The final panoramic image\n\nPress okay to continue..."
pop.popupmsg(msg)

a, b = lsp.lsp()

msg = "Answer for question 1.3\n\nThe ground  truth values:\n3, 4, 6\n\nThe estimated plane values:\n"+str(b[0])[1:8]+", "+str(b[1])[1:8]+", "+str(b[2])[1:8]+"\n\nThe absolute difference between the above mentioned values:\n"+str(a[0])[1:8]+", "+str(a[0])[1:8]+", "+str(a[0])[1:8]+"\n\nPress okay to continue..."
pop.popupmsg(msg)

msg = "The next output will be the final stitched panoramic image. The resized image will appear on your screen and the final full-sized image will be saved in this directory as the file \"output.jpg\"\n\nIn order to proceed after seeing the image, please press the space bar.\n\nPress okay to continue..."
pop.popupmsg(msg)

img = ist.stitch()
cv.imshow("Window", img)
cv.waitKey(0)
cv.destroyAllWindows()

msg = "This is the end of our assignment 2.\n\nYou can find the final stitched image under the same directory you found this executable.\n\nThank you for your time!\n\nPress Okay to exit..."
pop.popupmsg(msg)


