from docx import Document
from docx2pdf import convert

# Letter Class
class Letter:
    # Constructor
    def __init__(self, firstName: str, lastName: str, credentials: str, volunteerHours: str, level: str, filePath: str):
        self.firstName = firstName
        self.lastName = lastName
        self.credentials = credentials
        self.filePath = filePath
        self.volunteerHours = volunteerHours
        self.level = level
    # Generate letter
    def generateLetter(self):
        # return -1 if the volunteer hours are not a number
        if not self.volunteerHours.isdigit():
            return -1

        # create word document object
        doc = Document()

        # add text to document piece by piece
        # reference docx documentation for more information

        # save document to specified file path
        doc.save(self.filePath + '/letter-' + self.firstName.lower() + "-" + self.lastName.lower() + '.docx')

        # convert to pdf for emailing (dont want recipients to be able to edit the letter)
        convert(self.filePath + '/letter-' + self.firstName.lower() + "-" + self.lastName.lower() + '.docx', self.filePath + '/letter-' + self.firstName.lower() + "-" + self.lastName.lower() + '.pdf')

        return 0
