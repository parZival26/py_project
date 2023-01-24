from jwt import encode

def create_token(data: dict):
    token = str(encode(payload = data, key = "JUANjose2006", algorithm = "HS256"))
    return token
