from pydantic import BaseModel, EmailStr

class SignupRequest(BaseModel):
    email : EmailStr
    password: str
    phnNumber: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = 'bearer'
