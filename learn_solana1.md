
## 安装solana-cli

文档
https://docs.solanalabs.com/cli/install

https://blog.logrocket.com/building-token-solana/?ref=defiplot.com
```bash
sh -c "$(curl -sSfL https://release.solana.com/v1.18.4/install)"
```
返回
```commandline

downloading v1.18.4 installer
attempting to upgrade legacy config file
config upgrade succeeded!
  ✨ 1.18.4 initialized
Adding 
export PATH="/home/gbx/.local/share/solana/install/active_release/bin:$PATH" to /home/gbx/.profile

Close and reopen your terminal to apply the PATH changes or run the following in your existing shell:
  
export PATH="/home/gbx/.local/share/solana/install/active_release/bin:$PATH"


```

手动添加到~/.bashrc中
```commandline
sudo gedit ~/.bashrc
```
添加这一行
```commandline
export PATH="/home/gbx/.local/share/solana/install/active_release/bin:$PATH"
```
更新，即可显示版本
```commandline
gbx@gbx:~/Downloads$ source ~/.bashrc
gbx@gbx:~/Downloads$ solana --version
solana-cli 1.18.4 (src:356c6a38; feat:3352961542, client:SolanaLabs)

```

## 安装SPL-token-cli
安装cargo
```commandline
sudo apt install cargo
```
安装spl-token-cli
```commandline
cargo install spl-token-cli
```
报错
```commandline
。。。。
  Compiling displaydoc v0.2.4
   Compiling time v0.3.36
   Compiling hashbrown v0.12.3
error: failed to run custom build command for `hidapi v2.6.1`

```
和
```commandline

```commandline
error: failed to compile `spl-token-cli v3.4.0`, intermediate artifacts can be found at `/tmp/cargo-installnLaxub`.
To reuse those artifacts with a future compilation, set the environment variable `CARGO_TARGET_DIR` to that path.

```
试这个
```

```commandline
sudo apt-get install libudev-dev
```
没用。
试试这个
```commandline
sudo apt install build-essential cmake pkg-config libudev-dev
```
ok改完重新安装成功了，返回
```commandline
 Compiling spl-token-client v0.9.2
    Finished release [optimized] target(s) in 2m 09s
  Installing /home/gbx/.cargo/bin/spl-token
   Installed package `spl-token-cli v3.4.0` (executable `spl-token`)
warning: be sure to add `/home/gbx/.cargo/bin` to your PATH to be able to run the installed binaries

```
同样修改~/.bashrc，添加之后再source
```commandline
export PATH="/home/gbx/.cargo/bin:$PATH"
```
如果一切正常，则
```commandline
gbx@gbx:~/Downloads$ spl-token
spl-token-cli 3.4.0
SPL-Token Command-line Utility

USAGE:
    spl-token [FLAGS] [OPTIONS] <SUBCOMMAND>

FLAGS:
    -h, --help       Prints help information
    -V, --version    Prints version information
    -v, --verbose    Show additional information


```
## 主网及开发环境
Solana 在两个环境中运行：主网环境和开发环境。 作为开发人员，你可能熟悉这些术语。 主网络是用于生产的主要 Solana 网络所在的位置。

出于开发和测试目的，使用的是开发环境。 在本教程中，我们将使用开发环境。

默认情况下，你的环境设置为 Main。 在继续之前，我们应该将环境设置为 Development：
```commandline
solana config set --url https://api.devnet.solana.com
```
结果
```commandline
Config File: /home/gbx/.config/solana/cli/config.yml
RPC URL: https://api.devnet.solana.com 
WebSocket URL: wss://api.devnet.solana.com/ (computed)
Keypair Path: /home/gbx/.config/solana/id.json 
Commitment: confirmed
```
检查solana集群环境
```commandline
solana config get
```

```
gbx@gbx:~/Downloads$ solana config get
Config File: /home/gbx/.config/solana/cli/config.yml
RPC URL: https://api.devnet.solana.com 
WebSocket URL: wss://api.devnet.solana.com/ (computed)
Keypair Path: /home/gbx/.config/solana/id.json 
Commitment: confirmed
```
## get solana

进行空投，但是报错 
```commandline
gbx@gbx:~$ solana airdrop 1
Error: Dynamic program error: No default signer found, run "solana-keygen new -o /home/gbx/.config/solana/id.json" to create a new one

```
按照提示创建id.json
```commandline
solana-keygen new -o /home/gbx/.config/solana/id.json
Generating a new keypair

For added security, enter a BIP39 passphrase

NOTE! This passphrase improves security of the recovery seed phrase NOT the
keypair file itself, which is stored as insecure plain text

BIP39 Passphrase (empty for none): 

```
我用空格跳过了
```commandline
Wrote new keypair to /home/gbx/.config/solana/id.json
===========================================================================
pubkey: 2MQZA4a5vSc6TK5hxszCtrrgJoJ9Zh4hRpYWqE8UXKbt
===========================================================================
Save this seed phrase and your BIP39 passphrase to recover your new keypair:
despair foil radio unfair swap guide degree lab critic prison hungry powder
===========================================================================

```
看了一下id.json里面是很多组数字
。。。
现在可以发空投了
```commandline
gbx@gbx:~$ solana airdrop 1
Requesting airdrop of 1 SOL

Signature: 61wM4KYnoAyry1mGYoPqpQXsSfc88kqEA9niXDgs9FzRDSU352AG1KNMzKJNkmm68evdLcsqZ7BZkHXGjisNZTxL

1 SOL

```

## creating token
Token 在加密货币和区块链领域中通常用来标识一个特定的数字资产或代币。
每个 Token 都有其独特的标识符，
用于在区块链网络上进行识别和跟踪
```commandline
spl-token create-token
```
```commandline
gbx@gbx:~$ spl-token create-token
Creating token Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP under program TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA

Address:  Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
Decimals:  9

Signature: 33d6zbkY8mTh5KRJsRRwsU6kDgNfPjexZfAkEoYV1zdjtoLvGLUmNmorrYmrENohA6eMTFieYmAegwFbaYHMv91c

```

可以看到地址
```commandline
Address:  Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
```
##  creating account

```commandline

gbx@gbx:~$ spl-token create-account Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP

```
```commandline

gbx@gbx:~$ spl-token create-account Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
Creating account AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7

Signature: Jp55LDfR4GSC72h9isDYmSuWoz8Wda7V7zXtHbwy4MmtqDa8o9r5LsFqSPzUF7AJtowNxC71YwYi7yC7kL1tR1B

```
## 铸币
```commandline
spl-token mint <token-identifier> <token-amount>
```
```commandline
gbx@gbx:~$ spl-token mint Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP 100

```
```commandline
gbx@gbx:~$ spl-token mint Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP 100
Minting 100 tokens
  Token: Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
  Recipient: AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7

Signature: 5m1ci7YxCXLvk5RTypjj1FSNPJPNZZnLozL8zPCFaKn3JUkCpVSHHFNcergWDihgua25cVghN6sBQm73Nrpszsbf

```
检查你的余额： spl-token balance <token-identifier>。

```commandline
gbx@gbx:~$ spl-token balance Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
100
```


#### 存在的一些疑问和尝试
当时mint的时候并没有指定存入哪个account，
虽然只有一个自动存入了
```commandline
gbx@gbx:~$ spl-token create-account
error: The following required arguments were not provided:
    <TOKEN_MINT_ADDRESS>
```
```commandline
gbx@gbx:~$ spl-token create-account Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
Creating account AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7
Error: "Error: Account already exists: AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7"
```
一种token只能创造一个account吗

## 限制与销毁

销毁的实质：
销毁加密货币意味着将一些代币从流通中永久删除。
这通常是通过将相关代币转移到销毁地址来完成的
——这是一个永远无法检索代币的钱包地址。 这
通常被描述为销毁（destroy）代币。


通过禁用我们的铸币权限来限制我们的总供应量
```commandline
 spl-token authorize  <token-identifier> mint --disable
```
```commandline
gbx@gbx:~$ spl-token authorize  Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP mint --disable
Updating Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
  Current mint: 2MQZA4a5vSc6TK5hxszCtrrgJoJ9Zh4hRpYWqE8UXKbt
  New mint: disabled

Signature: 4fxVGFJBHCB8amYBs22BAcUE9otPtcxfs3fnjGNHN5fXNzpjq8xZsLWX5DZw9WBb1JFgoJqLLw1CcsLouL1J3RVn


```

销毁
```commandline
spl-token burn <token-account-addresss><amount>
```

```commandline
gbx@gbx:~$ spl-token burn AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7 20
Burn 20 tokens
  Source: AgMgDvXM2nqyrRCmUbMHZJQXCfmgYQe2vnfJs3pRmLA7

Signature: 5A9FbdDuU2GPTb7huCUB1rgAkQCyMHA1A1LC4raAx7QAo6sNqu3poLdCgRFfZBzePMoEPzNNAduiaVip7XWhVwz2

gbx@gbx:~$ spl-token balance Gq2KsCoV2RgSLgAhPDV1bPbgnXtWc9rnM3V8PGckQsjP
80

```