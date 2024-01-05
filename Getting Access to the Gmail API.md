Since I found the process of getting access to the Gmail API so frustrating, I am documenting all the steps I took here so it isn't as frustrating for anyone else:
- Register for a Google Workspace Enterprise Account, and log in with a domain owned by you
- Follow the steps here- https://developers.google.com/gmail/api/quickstart/python to get the API up and running
- Navigate into the Google Cloud Console > APIs and Services > Credentials and click on 'Create Credentials'
- Create a Oauth client ID with the Application Type being "Web Application"
- Download the client secrets json file. This is the "credentials.json" used in the oauth setup I had before
- Now create another set of credentials, this time make a service account
- Download the corresponding json, this is the "service.json" used in the current setup I have
- Now navigate to admin.google.com, and sign in with the same domain owned by you
- Go to Security > Access and data controls > API controls and click on "Manage Domain Wide Delegation"
- Click on "Add New", and add the client ID (in the google cloud console under credentials) for both the web client and the service account
- Grant access to the following scopes for the client ids- "https://www.googleapis.com/auth/gmail.compose",
        "https://www.googleapis.com/auth/gmail.send",
        "https://www.googleapis.com/auth/gmail.labels",
        "https://www.googleapis.com/auth/gmail.settings.basic",
        "https://www.googleapis.com/auth/gmail.settings.sharing",
        "https://mail.google.com/"
- When using the service account to create events, add the "subject" parameter in credentials which is your login id for admin.google.com 
- This would enable you to access all functionalities of the gmail API without being blocked
