# OpenCode Instructions

## Running the app
```bash
python main.py
```

## Setup
1. Create `config/accounts.yaml` from `config/accounts.example.yaml`
2. Populate with VK group IDs, tokens
3. Create `photos/{account_id}/` directories with photos (one photo per group)

## Architecture
- **main.py**: Async entrypoint. Uploads photos to VK walls with message buttons
- **config/**: YAML parser loads `accounts.yaml` → `Account` objects
- Each account uploads photos from `photos/{account_id}/` to its groups

## Gotchas
- Photo count must match account's group count
- Uses `vkbottle` async API
