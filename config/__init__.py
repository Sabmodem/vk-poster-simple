from .yml_parser import read_config, Token, Account
accounts = read_config('./config/accounts.yaml')

__all__ = [
    'accounts',
    'Token',
    'Account'
]