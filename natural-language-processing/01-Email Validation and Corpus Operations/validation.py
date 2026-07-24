import re

def validate_emails(text):
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    tokens = text.split()

    print("--- Email Validation Results ---")
    for token in tokens:
        clean_token = token.strip(",.?!();:")

        if re.match(email_pattern, clean_token):
            print(f"VALID: {clean_token}")
        else:
            print(f"INVALID: {clean_token}")

data = input("Enter: ")
validate_emails(data)