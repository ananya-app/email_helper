# imports
from google.oauth2 import service_account
from googleapiclient.discovery import build
import base64
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# scope of access for calendar API
SCOPES = ["https://www.googleapis.com/auth/gmail.compose",
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.labels",
        "https://www.googleapis.com/auth/gmail.settings.basic",
        "https://www.googleapis.com/auth/gmail.settings.sharing",
        "https://mail.google.com/"]
SERVICE_ACCOUNT_FILE = 'app/service.json'

# creates a meeting event in user's calender based on service account
def create_event(text, mailto, subject):
    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES, subject="ananya@businessfactory.live")
    service = build('gmail', 'v1', credentials=credentials)
    message = EmailMessage()
    message.set_content(text)

    message["To"] = mailto
    message["From"] = "ananya@businessfactory.live"
    message["Subject"] = subject

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"message": {"raw": encoded_message}}
    # pylint: disable=E1101
    draft = (
        service.users()
        .drafts()
        .create(userId="me", body=create_message)
        .execute()
    )

    print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')

    return draft