# imports
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from starlette.requests import Request
from google.oauth2 import service_account
from google_auth_oauthlib.flow import Flow
from app import event
from app import models
from app import schema
from app import processtext
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from sqlalchemy.orm import Session

import os 


# create an app object
app = FastAPI(title="Email API", openapi_url="/openapi.json")

# location of frontend framework
origins = [
    "http://localhost:3001", 
]

# CORS middleware to allow for seamless frontend to backend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# adding a starlette middleware for session management
app.add_middleware(SessionMiddleware, secret_key="mycousinthrockmorton", https_only=True)

# global variables for authorize and callback, creds is the client secret file and scopes is the level of access
CREDS = "app/credentials.json"
SCOPES = ["https://www.googleapis.com/auth/gmail.compose",
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.labels",
        "https://www.googleapis.com/auth/gmail.settings.basic",
        "https://www.googleapis.com/auth/gmail.settings.sharing",
        "https://mail.google.com/"]
# redirect uri after authorization flow is complete
REDIRECT_URI = "http://localhost:8000/callback"
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# initiating an impersonation based login for the service account
@app.get("/login")
async def login():
    # Create a flow instance to manage the OAuth 2.0 Authorization Grant Flow steps
    flow = Flow.from_client_secrets_file(
        CREDS,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )

    authorization_url, _ = flow.authorization_url(
        access_type='offline',
        prompt='consent'
    )

    return RedirectResponse(authorization_url)

@app.get("/callback")
async def callback():
    return RedirectResponse(url='http://localhost:3001/create-draft')

# function to initialize database
def get_db():
    db = models.session.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# endpoint for model to process user text, and display it for verification
@app.post("/process_text")
def process_text(data: schema.TextData):
    text = processtext.process_text(data.text)
    return {"user_text": text}
        
# endpoint to create a draft using google mail API
@app.post("/create_draft/")
def create_draft(maildetails: schema.MailDetails, db: Session = Depends(get_db)):
    id = processtext.get_id()
    db_mail = models.mail.MailDetails(id=id, mailto=maildetails.mailto, subject=maildetails.subject, text=maildetails.text)
    db.add(db_mail)
    db.commit()
    db.refresh(db_mail)
    event.create_event(maildetails.text, maildetails.mailto, maildetails.subject)
    return {"message": "Draft Created"}
    

# import uvicorn and define an address for the site
if __name__ == "__main__":
    # for debugging 
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8000, log_level="debug")

