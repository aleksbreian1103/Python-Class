from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import mimetypes
import os

PATHSTEM = "v:\\workspace\\Python2_Homework11\\src\\"

def emailmsg(addy, body, attachments):
    msg = MIMEMultipart()
    
    msg['To'] = addy
    text_msg = MIMEText(body, 'plain')
    msg.attach(text_msg)

    if attachments:
        for fn in attachments:
            format, enc = mimetypes.guess_type(fn)
            type, subtype = format.split('/')
            
            if type == "text":
                fp = open(fn)
                mime = MIMEText(fp.read(), _subtype=subtype)
            elif type == "image":
                fp = open(fn, 'rb')
                mime = MIMEImage(fp.read(), _subtype=subtype)
            elif type == 'audio':
                fp = open(fn, 'rb')
                mime = MIMEAudio(fp.read(), _subtype=subtype)
            else:
                fp = open(fn, 'rb')
                mime = MIMEBase(type, subtype)
                mime.set_payload(fp.read())
            
            mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
            msg.attach(mime)
            fp.close()
    
    return msg

if __name__ == "__main__":
    attach1 = PATHSTEM + "python_logo.png"
    attach2 = PATHSTEM + "lorem.txt"
    attachments = [attach1, attach2]
    print(emailmsg("ying82@gmail.com", "Email body.", attachments))
