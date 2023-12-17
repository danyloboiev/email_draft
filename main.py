import os.path
import base64
from email.message import EmailMessage
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class GmailEmail:
    SCOPES = ["https://www.googleapis.com/auth/gmail.compose"]

    def __init__(self):
        self.creds = None
        self.service = None

    def authenticate(self):
        if os.path.exists("token.json"):
            self.creds = Credentials.from_authorized_user_file("token.json", self.SCOPES)
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", self.SCOPES)
                self.creds = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())
        self.service = build("gmail", "v1", credentials=self.creds)

    def create_draft(self, to_email, from_email, subject, message_text):
        try:
            message = EmailMessage()
            message.set_content(message_text)
            message["To"] = to_email
            message["From"] = from_email
            message["Subject"] = subject
            encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
            create_message = {"message": {"raw": encoded_message}}
            draft = (
                self.service.users()
                .drafts()
                .create(userId="me", body=create_message)
                .execute()
            )
            print(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
        except HttpError as error:
            print(f"An error occurred: {error}")
            draft = None
        return draft

if __name__ == "__main__":
    gmail = GmailEmail()
    gmail.authenticate()
    gmail.create_draft("danyloboiev@gmail.com", "danilboev1226000@gmail.com", "Draft with Gmail API", "Text for email")
