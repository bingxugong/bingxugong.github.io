
# SOLANA开发环境搭建
文档
http://defiplot.com/blog/set-up-solana-dev-env/

https://docs.alchemy.com/docs/how-to-setup-your-solana-development-environment?ref=defiplot.com


## Alchemy
备注注册用的自己谷歌账户+手机
网址
https://dashboard.alchemy.com/

### create an app
API key 
```commandline
M5CUaTI_gFLBNAbpsdpuRJQhQOJVD0T7
```
HTTPs
```commandline
https://solana-mainnet.g.alchemy.com/v2/M5CUaTI_gFLBNAbpsdpuRJQhQOJVD0T7
```
Websockets
```commandline
wss://solana-mainnet.g.alchemy.com/v2/M5CUaTI_gFLBNAbpsdpuRJQhQOJVD0T7
```
### send first request
HTTPs example
```commandline
# Returns recent block production information
curl https://solana-mainnet.g.alchemy.com/v2/M5CUaTI_gFLBNAbpsdpuRJQhQOJVD0T7 -X POST -H "Content-Type: application/json" -d '{"id": 1, "jsonrpc": "2.0", "method": "getBlockProduction"}'
```
返回大致
```commandline
{"jsonrpc":"2.0","result":{"context":{"apiVersion":"1.17.28","slot":261797680},"value":{"byIdentity":{"12ashmTiFStQ8RGUpi1BTCinJakVyDKWjRL6SWhnbxbT":[4,4],"1KXvrkPXwkGF6NK1zyzVuJqbXfpenPVPP6hoiK9bsK3":[4,4],"22rU5yUmdVThrkoPieVNphqEyAtMQKmZxjwcD8v4bJDU":[52,52],"245B9WFHUGuWycSXHagHXwsXGcxDkNYfxWBaeh7vAHDU":[4,4],"2B5wMmBQkMHu9V5JbUyJuf2mJJUU286qKPsZzvQQjTNQ":[4,4],"2EiEMRvsBS43gbDCi5yb9GfRBghae41UFAbBt2iSvNYB":[4,4],"2GUnfxZavKoPfS9s3VSEjaWDzB3vNf5RojUhprCS1rSx":[36,36],"2P
```

Websocket example
```commandline
# Listen to all finalized blocks
wscat -c wss://solana-mainnet.g.alchemy.com/v2/M5CUaTI_gFLBNAbpsdpuRJQhQOJVD0T7

# Then call a subscription
> {"jsonrpc": "2.0", "id": 1, "method": "signatureSubscribe", "params": ["2EBVM6cB8vAAD93Ktr6Vd8p67XPbQzCJX47MpReuiCXJAtcjaxpvWpcg9Ege1Nr5Tk3a2GFrByT7WPBjdsTycY9b"]}
```
```commandline
找不到命令 “wscat”，但可以通过以下软件包安装它：
sudo apt install node-ws
2.0,：未找到命令
gbx@gbx:~$ sudo apt install node-ws

```
装了之后大概是可以正常运行了
```commandline
Connected (press CTRL+C to quit)
> 

```
### creating new app
选用的solana协议和devnet测试网
名称叫gbx-test
API key 
```commandline
Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P
```
HTTPs
```commandline
https://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P
```
Websockets
```commandline
wss://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P
```
Returns recent block production information
```commandline
curl https://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "jsonrpc": "2.0", "method": "getBlockProduction"}'
```
websocket example
```commandline
# Install wscat (https://github.com/websockets/wscat)
npm install -g wscat

# Listen to all new pending transactions
wscat -c wss://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P

# Then call a subscription
> {"jsonrpc":"2.0","id": 2, "method": "eth_subscribe", "params": ["alchemy_pendingTransactions", {"toAddress": ["0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48", "0xdAC17F958D2ee523a2206206994597C13D831ec7"], "hashesOnly": false}]}
```
## 创建phantom钱包
备注白12
## 安装Rust
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
我这里说已经装过了
但是我测试这几个
```commandline
rustup --version
rustc --version
cargo --version
```
rustup  是没有安装的。。。
算了我就多安装一个rustup吧，以后出了问题再说
。
```
sudo snap install rustup --classic

```
```commandline
 rustup 1.27.0 已从 Canonical✓ 安装
```
## JavaScripts
### 安装Node.js

这个好像是Ubuntu对应
https://nodejs.org/en/download/package-manager/all#debian-and-ubuntu-based-linux-distributions
Debian and Ubuntu based Linux distributions
Node.js binary distributions are available from NodeSource.
https://github.com/nodesource/distributions


Alternatives
Packages compatible with Debian and Ubuntu based Linux distributions are available via Node.js snaps.
https://nodejs.org/en/download/package-manager/all#snap
可通过snap安装。。。
https://github.com/nodejs/snap
那直接试试md中的这句
```commandline
sudo snap install node --classic --channel=14
```
```commandline
node (14/stable) 14.21.2 已从 OpenJS Foundation (iojs✓) 安装

```
```commandline
gbx@gbx:~$ node --version
v12.22.9

```
### 安装mocha 和yarn框架
```bash
sudo npm install --global mocha
sudo npm install --global yarn
```
#### 太慢了  试试npm换源
https://segmentfault.com/a/1190000023314583
找到配置文件
```bash
npm config ls -l
```
找到这一行 
```commandline
userconfig = "/home/gbx/.npmrc"

```
去修改这个文件
添加淘宝源
找到并打开配置文件：~/.npmrc
写入配置：
```
registry=https://registry.npm.taobao.org
```
验证成功换源

```commandline
gbx@gbx:~$ npm config get registry
https://registry.npm.taobao.org/

```
报错，原因是taobao旧域名更换了
换成这个
```commandline
https://registry.npmmirror.com
```
同样修改。

能用
```commandline
sudo npm install mocha
```
但是用
```commandline
mocha --version
```
找不到。。
算了，还是用
```commandline
sudo apt-get install mocha
```
吧
```commandline
gbx@gbx:~$ mocha --version
9.2.1

```
```commandline
gbx@gbx:~$ yarn --version
0.32+git

```

## 配置cli
通过alchemy连接到solana devnet网络
```commandline
gbx@gbx:~$ solana --version
solana-cli 1.18.4 (src:356c6a38; feat:3352961542, client:SolanaLabs)
gbx@gbx:~$ solana config set --url https://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P

```
```commandline
Config File: /home/gbx/.config/solana/cli/config.yml
RPC URL: https://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P 
WebSocket URL: wss://solana-devnet.g.alchemy.com/v2/Z3ZAjRxIxXox-u1Giamp0Kmr6B2E572P (computed)
Keypair Path: /home/gbx/.config/solana/id.json 
Commitment: confirmed
```

###  查看公钥
```commandline
gbx@gbx:~$ solana address
2MQZA4a5vSc6TK5hxszCtrrgJoJ9Zh4hRpYWqE8UXKbt

```

## Anchor

```commandline
cargo install --git https://github.com/coral-xyz/anchor anchor-cli --locked
```
成功结果
```commandline
  Installed package `anchor-cli v0.30.0 (https://github.com/coral-xyz/anchor#c96846fc)` (executable `anchor`)
gbx@gbx:~$ anchor --version
anchor-cli 0.30.0
```
