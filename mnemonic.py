# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from mnemonic import Mnemonic
from bip44 import Wallet
from web3 import Account

# Load the value of the MNEMONIC variable from the .env file
mnemonic = os.getenv("MNEMONIC")

# Evaluate the contents of the mnemonic variable
# Create a new mnemonic seed phrase if the value of mnemonic equals None
if mnemonic is None:
  mnemo = Mnemonic("english")
  mnemonic = mnemo.generate(strength=128)

# Display the value of the mnemonic variable
mnemonic


wallet = Wallet(mnemonic)

# Create the public and private keys associated with a new Ethereum account
private, public = wallet.derive_account('eth')

