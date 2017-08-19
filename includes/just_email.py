from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from settings import email
from settings import picture


class JustEmail:

    def __init__(self):
        self.server = email['SERVER']
        self.port = email['PORT']
        self.username = email['USERNAME']
        self.password = email['PASSWORD']
        self.sender = email['SENDER']
        self.receiver = email['RECEIVER']
        self.subject = email['SUBJECT']
        self.textmsg = email['MESSAGE']
        self.uploadfolder = picture['FOLDER']
        self.msgobj = MIMEMultipart()

    def make_message(self):
        try:
            self.msgobj['From'] = self.username
            self.msgobj['To'] = self.receiver
            self.msgobj['Subject'] = self.subject
            self.msgobj.attach(MIMEText(self.textmsg))

        except Exception as e:
            print("makemsg " + str(e))

    def add_images(self, images):
        if isinstance(images, list):
            try:
                for image in images:
                    fp = open(self.uploadfolder + "/" + image, 'rb')
                    img = MIMEImage(fp.read())
                    fp.close()
                    self.msgobj.attach(img)

            except Exception as e:
                print("addimg " + str(e))

        else:
            print("passed parameter is not a list")

    def send_mail(self):
        try:
            server = SMTP(self.server, self.port)
            server.ehlo()
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, self.receiver, self.msgobj.as_string())
            server.close()

        except Exception as e:
            print("sendmail " + str(e))
