# email_draft
This app uses the Gmail API, accepts the email, subject, and content of the email, and creates a draft in your gmail account.

While working on this task, I delved deeply into the Gmail API documentation to understand best practices and required technical requirements. Modules used and their purpose:

google.auth and google.oauth2.credentials: these modules were used to authenticate the user via Google OAuth 2.0. This provides secure access to the user's Gmail account.

google_auth_oauthlib.flow: allows you to easily use the authorization flow to get the necessary permissions from the user.

googleapiclient.discovery: this module is used to create the Gmail API client, which in turn allows you to perform actions with email, such as creating drafts.

googleapiclient.errors.HttpError: provides HTTP Error Handling for requests to the Gmail API.

email.message.EmailMessage: a standard Python module for creating email objects.

base64: used to encode email content in a format compatible with the Gmail API.

Object-oriented approach:

I decided to use OOP to implement this task because it gives a clear structure to the code and improves its readability. The Gmail Email class was created using two methods: 'authenticate' for user authentication and 'create_draft' for creating a draft email. This makes it easy to extend the functionality and use the class in different contexts.

This approach also simplifies testing and subsequent code support, since all responsibilities are clearly separated between class methods.

To make the program work the same way:
- Go to the Google Developers Console.
- Create a new project or select an existing one.
- Enable the Gmail API for your project.
- Create OAuth 2.0 credentials for your application. Download the JSON file and save it as credentials.json.
