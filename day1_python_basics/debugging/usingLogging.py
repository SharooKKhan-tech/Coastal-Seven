import logging

logging.basicConfig(level=logging.INFO)

x = 10
y = 0

logging.info(f"x = {x}, y = {y}")

try:
    result = x / y
except ZeroDivisionError:
    logging.error("Cannot divide by zero")