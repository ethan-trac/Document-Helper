import win32com.client as win32

# Ambassador Program Email class
class EmailAP:
    # Constructor
    def __init__(self, firstName, lastName, email, filePath):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.filePath = filePath
        self.subject = 'Ambassador Program: Requested Documents'
    # Generate email
    def generateEmail(self):
        
        # create outlook object
        outlook = win32.Dispatch('outlook.application')
        message = outlook.CreateItem(0)
        # set template details
        message.To = self.email
        message.Subject = self.subject

        # hard coded :(
        # create body text
        text = 'Hello ' + self.firstName + ' ' + self.lastName + ',\n\n' + 'Thank you for participating in the Ambassador Program. Attached are the documents you requested.\n\n' + 'Best,\n\n'

        # return -1 if the files are not found
        try: # add attachments to email
            message.Attachments.Add(self.filePath + '/certificate-' + self.firstName.lower() + "-" + self.lastName.lower() + '.png')
            message.Attachments.Add(self.filePath + '/ambassador-letter-' + self.firstName.lower() + "-" + self.lastName.lower() + '.pdf')
        except:
            return -1
        
        # return -2 if the email, first name, or last name are empty
        if self.email == '' or self.firstName == '' or self.lastName == '':
            return -2

        # set body text to previously created variable
        message.Body = text

        # open template in outlook
        message.Display()

        return 0