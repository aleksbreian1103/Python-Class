from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import *
import mimetypes
import os

def emailmsg(addy, body, attachments):
    msg = MIMEMultipart()
    
    msg['To'] = addy
    text_msg = MIMEText(body, 'plain')
    msg.attach(text_msg)
    
    for fn in attachments:
        format, enc = mimetypes.guess_type(fn)
        mb = MIMEBase(*format.split('/'))
        mb.set_payload(open(fn, 'rb').read())
        mb.add_header('Content-Disposition', 'attachment', filename=os.path.basename(fn))
        msg.attach(mb)
    
    return msg
