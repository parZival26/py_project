from jwt import encode, decode

def create_token(data: dict):
    token = str(encode(payload = data, key = "JUANjose2006", algorithm = "HS256"))
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key="JUANjose2006", algorithms = ['HS256'])
    return data