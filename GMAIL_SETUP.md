# Gmail MCP Setup Instructions

## Prerequisites
- Python 3.10+
- Gmail account
- Google Cloud Project

## Setup Steps

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Configure Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Gmail API:
   - Navigate to "APIs & Services" > "Library"
   - Search for "Gmail API"
   - Click "Enable"

### 3. Create OAuth Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. Configure OAuth consent screen:
   - User Type: External (for testing)
   - Add required information
   - Add test users if needed
4. Create OAuth client ID:
   - Application type: Desktop app
   - Name: Gmail MCP Server
5. Download the credentials JSON file
6. Save it as `credentials.json` in the project directory

### 4. Configure OAuth Scopes

Make sure your OAuth consent screen includes the scope:
- `https://www.googleapis.com/auth/gmail.send`

### 5. Set Up Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your values:
   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   MCP_GMAIL_CREDENTIALS_PATH=credentials.json
   MCP_GMAIL_TOKEN_PATH=token.json
   RECIPIENT_EMAIL=your_recipient@gmail.com
   ```

### 6. First Run Authentication

The first time you run the application, it will:
1. Open a browser window for OAuth authentication
2. Ask you to sign in to your Google account
3. Request permission to send emails
4. Save the authentication token to `token.json`

### 7. Run the Application

```bash
python talk2mcp_email.py
```

## Troubleshooting

### "Access blocked" error
- Make sure you've added yourself as a test user in the OAuth consent screen
- Verify the Gmail API is enabled

### "Invalid credentials" error
- Check that `credentials.json` is in the correct location
- Verify the file contains valid OAuth credentials

### Token expired
- Delete `token.json` and run the application again
- This will trigger a new authentication flow

## Files

- `email_mcp_server.py` - MCP server with calculator tools and Gmail sending
- `talk2mcp_email.py` - Client that uses the MCP server and sends results via email
- `credentials.json` - OAuth credentials (DO NOT commit to git)
- `token.json` - OAuth token (auto-generated, DO NOT commit to git)
- `.env` - Environment variables (DO NOT commit to git)
