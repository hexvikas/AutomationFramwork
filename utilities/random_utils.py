import random
import string

def generate_random_email(domain="gmail.com"):
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"user_{random_str}@{domain}"