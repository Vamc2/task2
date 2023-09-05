import random
import smtplib

# Step 1: Generate a 6-digit random OTP
otp = str(random.randint(100000, 999999))

# Step 2: Store the OTP in a variable (You can also store it in a database)
otp_storage = otp

# Step 3: Write a function to send emails
def send_email(email, message):
    # Replace these with your SMTP server details
    smtp_server = 'smtp-relay.gmail.com'
    smtp_port = 587
    smtp_username = 'sandu.vamsi@gmail.com'
    smtp_password = 'Kesu@kesu1'

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(smtp_username, email, message)
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Email could not be sent:", str(e))

# Step 4: Send the OTP via email
user_email = input("Enter your email address: ")
email_message = f"Your OTP is: {otp}"
send_email(user_email, email_message)

# Step 5: Request user input for OTP verification
user_input_otp = input("Enter the OTP sent to your email: ")

# Step 6: Verify the user's input
if user_input_otp == otp_storage:
    print("OTP Verified successfully!")
else:
    print("OTP Verification failed. Please try again.")
