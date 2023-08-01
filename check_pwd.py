# Inserting the Basic Code for the check_pwd function

def check_pwd(pwd):
    symbols = "~`!@#$%^&*()_+-="

    if len(pwd) < 8 or len(pwd) > 20:
        return False
    if not any(character.islower() for character in pwd):
        return False
    if not any(character.isupper() for character in pwd):
        return False
    if not any(character.isdigit() for character in pwd):
        return False
    if not any(character in symbols for character in pwd):
        return False

    return True
