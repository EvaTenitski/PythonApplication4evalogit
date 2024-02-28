import random
import string

def kontrolli_kasutajanimi(nimi, kasutajate_nimekiri):
    return nimi in kasutajate_nimekiri

def loo_parool():
    tähed = string.ascii_letters + string.digits + string.punctuation
    parool = ''.join(random.choice(tähed) for _ in range(12))
    return parool

def kontrolli_parooli_tugevust(parool):
    return any(char.islower() for char in parool) and \
           any(char.isupper() for char in parool) and \
           any(char.isdigit() for char in parool) and \
           any(char in string.punctuation for char in parool)