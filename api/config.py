"""
config provides general settings for the API
"""
from os import environ

ALERT_WALLET_ADDRESS = environ.get(
    "ALERT_WALLET_ADDRESS", "0x8ab2b989b6E4Fb453968C46cEE0CbCcB9839e1c2"
)
ALERT_WALLET_PK = environ.get(
    "ALERT_WALLET_PK",
    "0x98f5f0839c7645affacde7cc4de16049d386b3f81320dbd5835539ce18978f43",
)

BLOCK_USERNAME = environ.get("BLOCK_USERNAME", "equipe03")
BLOCK_PASSWORD = environ.get("BLOCK_PASSWORD", "kt693x")
