import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_files(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = 'mYb4DjJREr8AAAAAAAAAAeLkoenOiu2UpELvfplagMoUx-7qMJqUCp_S7s0tyYi6'
    transferdata = TransferData(access_token)

    file_from = 'test.txt'
    file_to = '/python/test.txt'
    transferdata.upload_files(file_from,file_to)
    print("Files uploaded successfully!")

if __name__ == '__main__':
    main()