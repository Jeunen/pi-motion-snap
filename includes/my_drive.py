from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class MyDrive:

    def __init__(self):
        self.gauth = GoogleAuth()
        self.drive = GoogleDrive(self.gauth)

    def upload(self, filename):
        driveFile = self.drive.CreateFile()
        driveFile.SetContentFile(filename)
        driveFile.Upload()
