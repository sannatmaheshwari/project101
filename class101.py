import dropbox

class TransferData:
    def __init__(self,token):
        self.token = token

    def uploadFiles(self,source,destination):
        dbx = dropbox.Dropbox(self.token)

        f = open(source, 'rb')
        dbx.files_upload(f.read(), destination)

def main():
    token = "sl.BAyPwRTP2dFgB5ihW1ajKUNPB19AB-PaPOtB6GH_hmuryaJR7-S69gRSfEXfBTGxtbHLN1fWbxszaq-fdFyC_-JiLumHUNcGVFrARnkSK-Z0h74B333IKsl9QgryNs01RfGWPe_21FEq"
    transfer = TransferData(token)

    source = input("enter the file path to transfer = ")
    destination = input("enter the full path to upload to dropbox:") 

    transfer.uploadFiles(source,destination)
    print("your file has been moved")
main()