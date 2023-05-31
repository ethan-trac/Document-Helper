import customtkinter
import os
from tkinter import filedialog
from letter import LetterAP
from certificate import CertificateAP
from PIL import Image
from myemail import EmailAP

# set default appearance 
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# create global savepath variables
savePath = '' # path to save files
saveDataPath = 'save.txt' # path to text file that stores save path

# tab view class to switch between document generation types
class TabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        self.add("Ambassador Program")
        # create more tabs here as needed
        #
        #
        #
        ##################################

        # Set GUI for tabs

        # create recipient information frame AP (Ambassador Program)
        self.recipientInfoFrameAP = customtkinter.CTkFrame(self.tab('Ambassador Program'), fg_color="transparent")
        self.recipientInfoFrameAP.grid(row=2, column=1, padx=(20, 0), pady=(20, 0), sticky="nwes")
        self.recipientInfoFrameAP.grid_columnconfigure(0, weight=1)
        self.recipientInfoFrameAP.grid_rowconfigure(0, weight=1)
        
        self.titleLabel = customtkinter.CTkLabel(self.recipientInfoFrameAP, text="Recipient Information", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.titleLabel.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.firstNameEntryAP = customtkinter.CTkEntry(self.recipientInfoFrameAP, placeholder_text='First Name')
        self.firstNameEntryAP.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

        self.lastNameEntryAP = customtkinter.CTkEntry(self.recipientInfoFrameAP, placeholder_text='Last Name')
        self.lastNameEntryAP.grid(row=2, column=0, padx=(0, 10), pady=(0, 10))

        self.emailEntryAP = customtkinter.CTkEntry(self.recipientInfoFrameAP, placeholder_text='Recipient Email')
        self.emailEntryAP.grid(row=3, column=0, padx=(0, 10), pady=(0, 10))

        self.ambassadorLevelLabelAP = customtkinter.CTkLabel(self.recipientInfoFrameAP, text="Ambassador Level:", anchor="w")
        self.ambassadorLevelLabelAP.grid(row=4, column=0, padx=20, pady=(10, 0))

        self.ambassadorLevelEntryAP = customtkinter.CTkOptionMenu(self.recipientInfoFrameAP, values=["Regular", "Associate", "Executive"])
        self.ambassadorLevelEntryAP.grid(row=5, column=0, padx=20, pady=(10, 10))

        # create volunteer info info frame (Ambassador Program)
        self.volInfoFrameAP = customtkinter.CTkFrame(self.tab('Ambassador Program'), fg_color="transparent")
        self.volInfoFrameAP.grid(row=3, column=1, padx=(20, 0), pady=(20, 0), sticky="nwes")
        self.volInfoFrameAP.grid_columnconfigure(0, weight=1)
        self.volInfoFrameAP.grid_rowconfigure(4, weight=1)

        self.credentialsLabelAP = customtkinter.CTkLabel(self.volInfoFrameAP, text="Volunteer Information", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.credentialsLabelAP.grid(row=0, column=0, padx=(0, 10), pady=(0, 10))

        self.hoursEntryAP = customtkinter.CTkEntry(self.volInfoFrameAP, placeholder_text='Volunteer Hours')
        self.hoursEntryAP.grid(row=1, column=0, padx=(0, 10), pady=(0, 10))

        self.credentialsLabelAP = customtkinter.CTkLabel(self.volInfoFrameAP, text="Provide volunteer positions in list form.", anchor="w")
        self.credentialsLabelAP.grid(row=2, column=0, padx=(0, 10), pady=(0, 10))

        self.credentialsEntryAP = customtkinter.CTkTextbox(self.volInfoFrameAP, width=400)
        self.credentialsEntryAP.grid(row=3, column=0, padx=(0, 10), pady=(0, 10))

        # set default values (Ambassador Program)
        self.ambassadorLevelEntryAP.set("Regular")

        # set GUI for additional tabs here
        #
        #
        #
        ##################################

        # create popup window variables (initialized to None)
        self.toplevel_window = None
        self.confirmationWindow = None

    # generates certificate and letter
    def generateDocuments(self):
        # get global variables
        global saveDataPath
        global savePath

        # generate documents for Ambassador Program tab
        if(self.get() == 'Ambassador Program'):
            # get user input from GUI
            firstName = self.firstNameEntryAP.get()
            lastName = self.lastNameEntryAP.get()
            credentials = self.credentialsEntryAP.get('1.0', 'end-1c')
            volunteerHours = self.hoursEntryAP.get()
            level = self.ambassadorLevelEntryAP.get()

            # show error window if user input is invalid
            if firstName == '' or lastName == '' or credentials == '':
                errorMessage = "Please fill out all fields before generating documents."
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(self, message=errorMessage)  # create window if its None or destroyed
                else:
                    self.toplevel_window.focus()  # if window exists focus it

                return -1

            # create certificate and letter objects
            certificate = CertificateAP(firstName, lastName, savePath)
            letter = LetterAP(firstName, lastName, credentials, volunteerHours, level, savePath)

            # generate letter and certificate from objects
            letterResult = letter.generateLetter()
            certificate.generateCertificate()

            # -1 is returned if volunteer hours is not a number
            # throw error if volunteer hours is not a number
            if letterResult == -1:
                errorMessage = "Please provide volunteer hours as a number only."
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(self, message=errorMessage)  # create window if its None or destroyed
                else:
                    self.toplevel_window.focus()  # if window exists focus it

            # show success window if documents are generated successfully
            errorMessage = "Documents generated successfully!"
            if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                self.toplevel_window = ToplevelWindow(self, message=errorMessage)  # create window if its None or destroyed
            else:
                self.toplevel_window.focus()  # if window exists focus it
        
        # additional tabs will need if statements (alternatively switch cases)


    # generate template email
    def generateEmail(self):
        # get global variables
        global saveDataPath
        global savePath

        # generate email for Ambassador Program tab
        if self.get() == 'Ambassador Program':
            # get user input from GUI
            firstName = self.firstNameEntryAP.get()
            lastName = self.lastNameEntryAP.get()
            email = self.emailEntryAP.get()
            
            # create email object
            email = EmailAP(firstName, lastName, email, savePath)

            # generate template email from object
            generateEmailResult = email.generateEmail()

            # -1 is returned if documents are not generated before email template
            # throw error if documents are not generated before email template
            if generateEmailResult == -1:
                errorMessage = "Please generate documents before making an email template.\n\n\nMake sure you are in the same directory as your\n\ndocuments before creating an email template.\n\n\nMake sure the name of the documents matches the\n\nname provided."
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(self, message=errorMessage)  # create window if its None or destroyed
                else:
                    self.toplevel_window.focus()  # if window exists focus it

            # -2 is returned if recipient information is not provided before email template
            # throw error if recipient information is not provided before email template
            elif generateEmailResult == -2:
                errorMessage = "Please provide recipient information before generating an email template."
                if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
                    self.toplevel_window = ToplevelWindow(self, message=errorMessage)  # create window if its None or destroyed
                else:
                    self.toplevel_window.focus()  # if window exists focus it
        
        # additional tabs will need if statements (alternatively switch cases)
        return 0
    
    # clears fields in GUI
    def clear(self):
        # clear fields for Ambassador Program tab
        if self.get() == 'Ambassador Program':
            self.credentialsEntryAP.delete('1.0', 'end')
            self.firstNameEntryAP.delete('0', 'end')
            self.lastNameEntryAP.delete('0', 'end')
            self.emailEntryAP.delete('0', 'end')
            self.hoursEntryAP.delete('0', 'end')
            self.ambassadorLevelEntryAP.set("Regular")

# class for application itself
class App(customtkinter.CTk):
    def __init__(self):
        # call super constructor
        super().__init__()

        # get global variables
        global saveDataPath
        global savePath

        # get save path from save.txt
        self.getSaveData()

        # configure window
        self.title("Rupertsland Document Helper")
        self.resizable(False, False)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create tabview
        self.tab_view = TabView(master=self)
        self.tab_view.grid(row=0, column=1, padx=20, pady=20)

        # create sidebar frame with widgets
        self.sidebarFrame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebarFrame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebarFrame.grid_rowconfigure(4, weight=1)

        self.rliLogoImage = customtkinter.CTkImage(light_image=Image.open("RLI-TL_RGB_LIGHT.png"),
                                  dark_image=Image.open("RLI-TL_RGB_DARK.png"),
                                  size=(150, 74.72))


        self.logoLabel = customtkinter.CTkLabel(self.sidebarFrame, image=self.rliLogoImage, text='')
        self.logoLabel.grid(row=0, column=0, padx=20, pady=(20, 0))

        self.titleLabel = customtkinter.CTkLabel(self.sidebarFrame, text="Document Helper", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.titleLabel.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.generateDocumentsButton = customtkinter.CTkButton(self.sidebarFrame, text='Generate Documents', command=self.tab_view.generateDocuments)
        self.generateDocumentsButton.grid(row=2, column=0, padx=20, pady=10)
        
        self.generateEmailButton = customtkinter.CTkButton(self.sidebarFrame, text='Generate Email Template', command=self.tab_view.generateEmail)
        self.generateEmailButton.grid(row=3, column=0, padx=20, pady=10)

        self.resetImage = customtkinter.CTkImage(light_image=Image.open("reset.png"),
                                  dark_image=Image.open("reset.png"),
                                  size=(30, 30))

        self.resetButton = customtkinter.CTkButton(self.sidebarFrame, text='', image=self.resetImage, command=self.clearWindow, bg_color="transparent", fg_color="transparent", hover_color="")
        self.resetButton.grid(row=4, column=0, padx=(20, 20), pady=(20, 20))

        self.saveDirectoryLabel = customtkinter.CTkLabel(self.sidebarFrame, text="Save Directory", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.saveDirectoryLabel.grid(row=5, column=0, padx=(0, 10), pady=(0, 10))

        self.savePathString = savePath
        if len(self.savePathString) > 30: # shorten path if too long
            self.savePathString = self.savePathString[:30] + "..."

        self.filePathLabel = customtkinter.CTkLabel(self.sidebarFrame, text=self.savePathString)
        self.filePathLabel.grid(row=6, column=0, padx=(0, 10), pady=(0, 10))

        self.filePathButton = customtkinter.CTkButton(self.sidebarFrame, width = 10, text='Browse...', command=lambda: self.changeSavePath())
        self.filePathButton.grid(row=7, column=0, padx=(0, 10), pady=(0, 10))

        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebarFrame, text="Appearance Mode", anchor="w")
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebarFrame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 10))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")

        # create popup window variables (initialized to None)
        self.toplevel_window = None
        self.confirmationWindow = None

    # changes appearance mode
    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # gets save data from save.txt
    def getSaveData(self):
        global saveDataPath
        global savePath
        # check if save data file exists
        if os.path.exists(saveDataPath):
            with open(saveDataPath, 'r') as file:
                data = file.read().splitlines()

                # if there is a previous savepath, use it
                if len(data) > 0:
                    savePath = data[0]
                    # otherwise set to default
                else:
                    savePath = 'C:\''
        
        else:
            savePath = 'C:\''

    # changes save path and writes to save.txt
    def changeSavePath(self):
        global saveDataPath
        global savePath
        savePathTemp = filedialog.askdirectory()

        # catch if user cancels
        if savePathTemp != '':
            savePath = savePathTemp
        
        # save path to file
        with open(saveDataPath, 'w') as file:
            file.write(savePath)

        savePathString = savePath
        if len(savePathString) > 30:
            savePathString = savePathString[:30] + '...'
        # update label
        self.filePathLabel.configure(text=savePathString)

    def clearWindow(self):
        if self.confirmationWindow is None or not self.confirmationWindow.winfo_exists():
                self.confirmationWindow = ConfirmationWindow(self, app = self)  # create window if its None or destroyed
        else:
            self.confirmationWindow.focus()  # if window exists focus it

# popup window class for error messages
class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, message: str, **kwargs):
        super().__init__(*args, **kwargs)
        # set title of window
        self.title('Error')

        # make window not resizable
        self.resizable(False, False)

        # create label with message
        self.label = customtkinter.CTkLabel(self, text=message, anchor="center")
        self.label.pack(padx=20, pady=20)

        self.attributes('-topmost', 'true')  # make window topmost

# popup window class for confirmation messages
class ConfirmationWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, app: App, **kwargs):
        super().__init__(*args, **kwargs)
        # set title of window
        self.title('Notice')

        # get main app object (important for calling functions in main app)
        self.app = app

        # make window not resizable
        self.resizable(False, False)

        # create label with message
        self.label = customtkinter.CTkLabel(self, text='Are you sure you want to clear all fields?', anchor="center")
        self.label.pack(padx=20, pady=20)

        # create yes and no buttons
        self.yesButton = customtkinter.CTkButton(self, text='Yes', command=self.yes)
        self.yesButton.pack(padx=20, pady=20, side="left")

        self.noButton = customtkinter.CTkButton(self, text='No', command=self.destroy)
        self.noButton.pack(padx=20, pady=20, side="right")

        self.attributes('-topmost', 'true')  # make window topmost

    # clears all fields and closes window
    def yes(self):
        self.app.tab_view.clear()
        self.destroy()

# main
if __name__ == "__main__":
    # create app
    app = App()
    # run app
    app.mainloop()
