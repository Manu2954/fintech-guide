from fastapi import APIRouter
from controller.auth_controller import signup_user, login_user
from schemas.auth import SignupRequest, LoginRequest, TokenResponse

router = APIRouter()

@router.post('/signup')
def signup(req:SignupRequest):
    return signup_user(req.email, req.password, req.phnNumber)

@router.post('/login', response_model=TokenResponse)
def login(req: LoginRequest):
    return login_user(req.email, req.password)