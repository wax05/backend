import re

email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email):
    """Check Email address

    Args:
        email (String): Email address

    Returns:
        Bool : True is email not vaild, False otherwise
    """    
    return re.match(email_regex, email) is not None
