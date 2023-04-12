## Getting ready documentation
In order to use correctly starknet, use this specific venv:
```
python3.9 -m venv ~/cairo_venv && source ~/cairo_venv/bin/activate
```
then, define the starknet network to goerli testnet:
```
export STARKNET_NETWORK=alpha-goerli
```
then, define the deployed starknet wallet contract that we are gonna use (and potentially instantiate)
```
export STARKNET_WALLET=starkware.starknet.wallets.open_zeppelin.OpenZeppelinAccount
```
___
## Create an account
First, generate a wallet in local:
```
starknet new_account --account wallet_name
```
You should have a return like this:
```
Account address: 0x0511b37d642d29322f60d18b694391531a7ba5a462952c6f671944bd835cdcc4
Public key: 0x0361edee52ab6f30afa7dfff689a26805af421bc546740285317961672af8a88
Move the appropriate amount of funds to the account, and then deploy the account
by invoking the 'starknet deploy_account' command.

NOTE: This is a modified version of the OpenZeppelin account contract. The signature is computed
differently.
```
Keep in mind that your wallet is actually a contract that is already deployed, but not populated with your datas.  
In order to do so, let's pre-fund the address of the instancied version of the futur wallet contract address. **You need to pre-fund the wallet by sending `0.1 eth` to the `Account address`**.  

In order to do so, get some goerli en Ethereum Goerli testnet and bridge it to Starknet with the help of a web wallet like Argent that will help you to generate a seed and use it (so currently we haven't funded our futur wallet that we just generated thanks to commandline).  

Once you have `0.1 eth` into your web wallet you can now simply initiate the tx to transfer this `ether` to the `Account address` (and not to the public key).  

Monitor the tx, once it is `pending`, you can initiate the deployment of your wallet instance:
```
starknet deploy_account --account wallet_name
```
the return should be:
```
Sending the transaction with max_fee: 0.000768 ETH (767716294629699 WEI).
Sent deploy account contract transaction.

Contract address: 0x0511b37d642d29322f60d18b694391531a7ba5a462952c6f671944bd835cdcc4
Transaction hash: 0x609b9a66b79c6720282b48ed21c7bf708237ea638f8ff9056beb9b4f8f327be
```
And your wallet should be created successfully.
___
