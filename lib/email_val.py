import re

def validar_email(email):
    regex = "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"
    if re.findall(regex, email):
        return True
    else:
        return False



# main
if __name__ == '__main__':
    is_valid = validar_email("soporte@hack4u.io")
    print(is_valid)