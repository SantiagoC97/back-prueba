from jwt import encode, decode

def create_token(data: dict, secret: str= "1850") -> str:
    token = encode(payload=data, key=secret, algorithm="HS256")
    return token

def validate_token(token: str):
    data = decode(token, "1850", algorithms=["HS256"])
    return data