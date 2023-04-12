from starknet_py.net.account.account import Account
from starknet_py.net.gateway_client import GatewayClient
from starknet_py.net.models.chains import StarknetChainId
from starknet_py.net.signer.stark_curve_signer import KeyPair
from starknet_py.net.signer.stark_curve_signer import StarkCurveSigner

testnet = "testnet"

# Creates an instance of account which is already deployed (testnet)

# Account using transaction version=1 (has __validate__ function)
client = GatewayClient(net=testnet)
account = Account(
    client=client,
    address="0x07fe31b844e43ef53a2c213105bb1acca68dba88d1445c2f93cce33c86d3c3af", #Trying to use this address to deploy the ledger part of the contract
    key_pair=KeyPair(private_key=654, public_key=321),
    chain=StarknetChainId.TESTNET,
)

# There is another way of creating key_pair
#key_pair = KeyPair.from_private_key(key=123)

# Instead of providing key_pair it is possible to specify a signer
#signer = StarkCurveSigner("0x07fe31b844e43ef53a2c213105bb1acca68dba88d1445c2f93cce33c86d3c3af", key_pair, StarknetChainId.TESTNET)

#account = Account(client=client, address="0x07fe31b844e43ef53a2c213105bb1acca68dba88d1445c2f93cce33c86d3c3af", signer=signer)