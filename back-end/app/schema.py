from pydantic import BaseModel, EmailStr
from datetime import datetime

# pydantic model for input text
class TextData(BaseModel):
    text: str

# pydantic model for meeting data
class MailDetails(BaseModel):
    mailto: EmailStr
    subject: str
    text: str