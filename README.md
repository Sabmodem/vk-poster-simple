# VK Poster Simple

Async tool for posting photos to VK group walls with interactive buttons.

## Setup

1. Create config file:
   ```bash
   cp config/accounts.example.yaml config/accounts.yaml
   ```

2. Edit `config/accounts.yaml` with:
   - Account IDs
   - Access tokens (group or personal with appropriate permissions)
   - Target group IDs for each account

3. Create photo directories:
   ```bash
   mkdir -p photos/{account_id}
   ```
   Place one photo per group in each account's folder. Filenames are matched to groups sequentially.

## Running

```bash
python main.py
```

## Configuration

`config/accounts.yaml` structure:
```yaml
accounts:
  - id: account_identifier
    token:
      type: null  # or "group"
      value: your_token_here
    groups:
      - 123456789
      - 987654321
```

## Requirements

```bash
pip install -r requirements.txt
```

## Architecture

- `main.py` - Async entrypoint that uploads all configured photos
- `config/yml_parser.py` - Parses account configuration
- `vkbottle` - Async VK API client with `PhotoWallUploader`
