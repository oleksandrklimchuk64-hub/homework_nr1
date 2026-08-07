import re
def normalize_phone(phone_number):
    has_plus = phone_number.strip().startswith("+")
    phone = re.sub(r"\D+", "", phone_number)
    if has_plus:
        return "+" + phone
    if phone.startswith("380"):
        return "+" + phone
    if phone.startswith("0"):
        return "+38" + phone
    return "+38" + phone
raw_numbers = [
    "067\\123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "    0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11",
    "+44 123 456 789"
]
sanitized_numbers = [normalize_phone(number) for number in raw_numbers]
print(sanitized_numbers)