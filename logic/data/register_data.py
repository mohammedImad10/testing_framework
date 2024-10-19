import random
import string
import logging as logger


def generate_random_email(domain=None, email_prefix=None) -> str:
    if not domain:
        domain = 'test.com'
    if not email_prefix:
        email_prefix = 'test_user'

    random_str = ''.join(random.choices(string.ascii_lowercase, k=10))
    logger.info(f"Generated random string is {random_str}")

    email = f"{email_prefix}_{random_str}@{domain}"
    logger.info(f"Generated random email: {email}")
    return email


def get_email_and_password_to_register(domain=None, email_prefix=None) -> dict:
    return {
        "email": generate_random_email(domain, email_prefix),
        "password": 'Test@moham'
    }
