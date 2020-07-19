import smptlib
import os

EMAIL_ADDRESS =os.environ.get('EMAIL_USER')
EMAIL_PASSWORD =os.environ.get('EMAIL_PASS')

with smptlib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
