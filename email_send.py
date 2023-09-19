import smtplib
from random import randint


# creates SMTP
def sendResetOTPonEmail(email) -> int:
    random_otp = randint(100000, 999999)
    s = smtplib.SMTP("smtp.gmail.com", 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login("changednishant@gmail.com", "")

    # message to be sent
    message = f"Your OTP to reset password is {random_otp}"

    # sending the mail
    s.sendmail("changednishant@gmail.com", "changednishant@gmail.com", message)

    # terminating the session
    s.quit()
    return random_otp
