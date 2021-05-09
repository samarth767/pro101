  
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token =  access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files: 
                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)
                    
                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = "sl.AqcZBnlzqtFwn4GrAPxG8kn7LEkQy49zKEnXPYX-Z0OlM4PnUxMpToSm7yBP5foRL90B1StXveNa_jFVS9k4E_GPMDZnjFnaHTG3UfpUc9xBFO6-nOhILAfj2e5_d01yinAE62hY"
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : "))
    file_to = input("Enter the full path to upload to Dropbox: ")

    transferData.upload_file(file_from,file_to)
    print("File has been uploaded")

main()