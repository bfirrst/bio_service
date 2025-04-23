# Bio Service

This service provides a `/bio` endpoint for fetching Telegram user bios using Telethon and session files.

## Setup

1. Place your Telegram session file in the `sessions/` directory:
   ```
   sessions/12262333496.session
   ```

2. Ensure the corresponding JSON credentials file is also present:
   ```
   sessions/12262333496.json
   ```

3. Deploy on Railway — it will use `${PORT}` automatically.

## API

POST `/bio`
```json
{
  "session_file": "12262333496",
  "api_id": 2040,
  "api_hash": "b18441a1ff607e10a989891a5462e627",
  "username": "StevenHardesty"
}
```
