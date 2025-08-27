import yaml
from dataclasses import dataclass
from typing import List

@dataclass
class Token:
    type: str
    value: str

@dataclass
class Account:
    id: str
    token: Token
    groups: list[int]

def read_file(filename: str) -> str:
    with open(filename, 'r') as infile:
        return infile.read()

def read_config(path) -> List[Account]:
    file = read_file(path)
    config = yaml.safe_load(file)
    accounts = []
    for account in config.get('accounts', []):
        accounts.append(Account(
            id=account.get('id'),
            token=Token(account.get('token').get('type'), account.get('token').get('value')),
            groups=account.get('groups')
        ))
    return accounts