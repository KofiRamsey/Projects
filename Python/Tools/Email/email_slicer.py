def email_slicer(email):
    username, domain = email.split("@")
    return username, domain


email = input('Email Address: ')
username, domain = email_slicer(email)
print("Username:", username)
print("Domain:", domain)


