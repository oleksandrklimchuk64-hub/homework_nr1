import re
def normalize_phone(phone_number):
    phone = re.sub(r"[^\d+]", "", phone_number)
    if phone.startswith("380"):
        phone = "+" + phone
    elif not phone.startswith("+38"):
        phone = "+38" + phone
    return phone
raw_numbers = [
    "067\\123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "    0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print(sanitized_numbers)
