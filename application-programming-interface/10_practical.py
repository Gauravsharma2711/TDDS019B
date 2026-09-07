from fastapi import FastAPI , Depends , HTTPException
from fastapi.security import OAuth2AuthorizationCodeBearer , OAuth2PasswordRequestForm
from jose import jwt 

app = FastAPI()

SECRET_KEY =mysecret
ALGORITHM = HS256

USERNAME = "gaurav"
PASSWORD = "2113"

oauth2_scheme = OAuth2AuthorizationCodeBearer (
    tokenUrl= "login"
)

@app.get('/')
def home():
    return ("This is Home page")

@app.post('/login')
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    if (
        form_data.username == USERNAME
        and form_data.password == PASSWORD
    ):
        token = jwt.encode(
            {
                "username" : form_data.username
            },
            SECRET_KEY , 
            algorithm=ALGORITHM
        )

        return{
            "access_token" : token ,
            'token_type' : "bearer"
        }

    raise HTTPException (
        sta
    )