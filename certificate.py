import cv2 as cv

# Ambassador Program Certificate class
class CertificateAP:

    # Constructor
    def __init__(self, firstName, lastName, filePath):
        self.name = firstName + " " + lastName
        self.firstName = firstName
        self.lastName = lastName
        self.filePath = filePath
    
    # Generate certificate
    def generateCertificate(self):
        
        # get image from file path
        img = cv.imread('Ambassador Program Certificate.png')
        
        # set x and y coordinates for text
        x_cord = 15
        y_cord = 70

        # set font size, color, and type
        fontSize = 3
        fontColor = (0,0,0)
        font = cv.FONT_HERSHEY_SCRIPT_COMPLEX

        # get text size
        textSize = cv.getTextSize(self.name, font, fontSize, 5)[0]

        # set text x and y coordinates
        text_x = (img.shape[1] - textSize[0]) / 2 + x_cord 
        text_y = (img.shape[0] + textSize[1]) / 2 - y_cord
        text_x = int(text_x)
        text_y = int(text_y)

        # put text on image
        cv.putText(img, self.name,
                (text_x ,text_y ), 
                font,
                fontSize,
                fontColor, 5)
    
        # Output path along with the name of the
        # certificate generated
        certiPath = self.filePath + '/certificate-' + self.firstName.lower() + "-" + self.lastName.lower() + '.png'
        
        # Save the certificate                      
        cv.imwrite(certiPath,img)