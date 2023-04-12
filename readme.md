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
