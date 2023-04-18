## Getting ready documentation
Just follow these [instructions](https://www.cairo-lang.org/getting-started/).

Next at each launch of your terminal don't forget to use this specific venv:
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
---
## Getting ready from the cairo basecamp
(They shared this doc after the basecamp: https://docs.google.com/document/d/e/2PACX-1vQO7MSt_JINcGItO4-aIH-FQE9xN_Ssa6zQXC93f0e7W5g7ECny57w3E2M9-fdTdU5Ne1R-Kt9g8_EB/pub)
1. Install rust:
    ```
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    ```
2. Get cairo-lang (python cli) for creating account, declaring, deploying and invoking contracts (python tool seems to only support 0.x cairo):
    ```
    pip3 install cairo-lang
    ```
2. Compile Cairo compiler from source (rust lib which is able to compile cairo 1.x)
    ```
    git clone https://github.com/starkware-libs/cairo
    cd cairo
    git checkout tags/v1.0.0-alpha.6
    cargo build --all --release
    ```
    Now add the binaries to your path:
    ```
    echo 'export PATH="$HOME/.cairo/target/release:$PATH"' >> ~/.zshrc
    ```
    And test it:
    ```
    starknet-compile --version
    ```
    It should returns something like that:
    ```
    cairo-lang-starknet 1.0.0-alpha.6 
    ```
    Now if you want to compile a cairo contract:
    ```
    starknet-compile file.cairo file.json
    ```
    If you want the vscode extension, install nodejs and then go to the correct directory to compile it:
    ```
    cd $HOME/.cairo/vscode-cairo
    ```
    then install dependencies:
    ```
    npm i
    ```
    compile the package:
    ```
    vsce package
    ```
    Then go to vscode and go the settings of your new extension (Cairo 1.0) and put the right PATH for the compiler, here is mine:
    ```
    /Users/blabla/.cairo/target/release/cairo-language-server
    ```

___
## Create an account
You can get some doc [here](https://github.com/starknet-edu/deploy-cairo1-demo) too.
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
1. Keep in mind that your wallet is actually a contract that is already deployed, but not populated with your datas.  
2. In order to do so, let's pre-fund the address of the instancied version of the futur wallet contract address. **You need to pre-fund the wallet by sending `0.1 eth` to the `Account address`**.  

3. In order to do so, get some goerli en Ethereum Goerli testnet and bridge it to Starknet with the help of a web wallet like Argent that will help you to generate a seed and use it (so currently we haven't funded our futur wallet that we just generated thanks to commandline).  

4. Once you have `0.1 eth` into your web wallet you can now simply initiate the tx to transfer this `ether` to the `Account address` (and not to the public key).  

5. Monitor the tx, once it is `pending`, you can initiate the deployment of your wallet instance:
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
## Fun facts

There’s no way for sequencers to verify correctness of ABI submitted on deployment. Which means that you can fake it on the deployment and have a fake ABI verified on Starknet explorer.  
It’s actually pretty intuitive that you cannot possibly verify the correctness of ABI without access to contract source code. Thus the sequencer cannot possibly verify it.
___
## Dev tools

nile is a cli framework to simplify starknet dev, but it seems outdates and doesn't work anymore with cairo 1.0
https://github.com/OpenZeppelin/nile
---
## Videos
- Starknet session 1 (fundamental) :  
    https://www.youtube.com/watch?v=NdP2jTQ34hY  

    https://docs.google.com/presentation/d/e/2PACX-1vRpos6yyrEn1WHz1iHpCWe7Ha0F7DEtiwM3pHYlk2S3S6h5rV4dTwhQvbcWeiBfld_kBF51XibeTUFy/pub?start=false&loop=false&delayms=3000&slide=id.g22d0d34fde7_0_7

    What we learn here is:
    - that cairo permits you to generate a crypographic proof that can proove the execution validity of your code.

    - Starknet uses Cairo programs and it's not about privacy but scalability

    - Starknet uses STARKs which are quantum resistants (SNARKs aren't), have a proof size which is about `400kb` (SNARKS have a 288 bytes so they are better on that) and have verification complexity of log^2(n) instead of a constant one for SNARKs

    - It made sense to me because Ethereum will be quantum resistant in the future

    - Architecture:
        - Sequencer: Validates, executes and bundle txs into blocks (so you send your bytecode in Sierra (Sierra = Safe intermediate representation) which allow reverted tx to the sequencer that will compile it to CASM cairo assembly)
        - Prover: Creates STARK proofs for Starknet and StarkEx (SHARP) 
        - Verifier: Ll smart contract that verifies STARK proofs from SHARP 
        - Starknet Core: L1 smart contract that store changes to L2 global state (DA) 
        - Full Node: Provide data to L2 dapps 

    - Code:
        - You declare the attributes into a struct named "`Storage`"
        - You can read value frolm this storage with the function with _`attribute`_**`::read()`**
        - You can write on the storage with _*`attribute`_**`::write(`**_`new value`_**`)`**

    - Tools:
        - Protostar is a dev toolchain (I will test it further later)
        - scarb (super updated): install it with these instructions (https://docs.swmansion.com/scarb/download) from this repo https://github.com/software-mansion/scarb/releases and don't forget to add the bin folder to the path by adding this to your terminal profile `export PATH="$HOME/.scarb/bin:$PATH"`



