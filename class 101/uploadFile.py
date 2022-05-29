import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
    
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BGeMSclPBZy35cpf9JLMSlLaUsz4MeS2SeM_mM-8kPO66DcaBeEd0fFqreUVVmK_v2Qwbj7JIO2kYZfFrJkuwgHN9RZwBfXcfvO_QoeWyZfXuerXwIcfvT-KsBEOt9z8g83CoFa_ytaD'
    transferData = TransferData(access_token)

    file_from = input('Enter the file path to transfer')
    file_to = input('Enter the full path to upload to dropbox')  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Uploaded")

main()