import win32com.client as win32

# Email class
class Email:
    # Constructor
    def __init__(self, firstName, lastName, email, filePath):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.filePath = filePath
        self.subject = ''
    # Generate email
    def generateEmail(self):
        
        # create outlook object
        outlook = win32.Dispatch('outlook.application') # or any other mailing application
        message = outlook.CreateItem(0)
        # set template details
        message.To = self.email
        message.Subject = self.subject

        # hard coded :(
        # create body text
        # see wind32com documentation for more information

        # open template in outlook
        message.Display()

        return 0