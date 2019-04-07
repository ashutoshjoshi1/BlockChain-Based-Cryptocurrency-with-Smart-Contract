# Void-Hacks----Hack-O-Holics
Project of my team (Hack O' Holics) for VoidHacks() 2019.

# Pre-requisites :-
1. Postman desktop application.
2. Python 3 with required libraries.
3. Xampp (Apache web server)
4. Truffle Ganache (to show transactions)
5. Remix soledity of browser.

# Procedure :-
1. $git clone https://github.com/rahulgangwal/Void-Hacks----Hack-O-Holics
2. cd VoidHacks()
3. python SamriddhiCoin.py
4. Open PostMan application and set the url on http://127.0.0.1:5000/get_chain for creaate blocks in chain and http://127.0.0.1:5000/mine_blocks to mine the formed blocks in our blockchain.
5. To see the transaction of cryptocurrency on web portal :-
  5(A). Open Xampp and start Apache Web Server.
  5(B). Copy and paste the UI folder of repo to "htdocs" of Xampp folder.
  5(C). Go to localhost/UI/index.html
  5(D). Login with credentials : Username : "ashutosh" ; Password : None.
  5(E). The further pages will explain the functions of Cryptocurrency -- Samriddhi Coin.
6. Initial Coin Offering :-
  6(A). Open GoogleChrome and open https://remix.ethereum.org/
  6(B). Copy the code of Samriddhi_Coin_ICO.sol from repo and paste it there.
  6(C). Clone the latest version of myetherwallet from https://github.com/kvhnuke/etherwallet/releases/download/v3.36.0/etherwallet-v3.36.0.zip and Download Truffle Ganache from https://truffleframework.com/ganache/ .
  6(D). Open MyEtherWallet folder and open index.html.
  6(E). In the Upper Right Corner, you have to Add your own soledity and name it with URL from Ganache example : http://127.0.0.1 and port "7545".
  6(F). Now go to Contracts to Deploy and interact with our Smart Contract.
  6(G). Deploy Contract: In ByteCode tab we have to paste the Object String of Byte Code of our Soledity file from details in remixsoledity. For Private Key we can use Ganache.
  6(H). Now we perform interaction in the transaction click on Interact With Contract, Paste the Senders Address in HashCode and ABI code from remixsoledity.
  6(I). It will show all the task and function of an ICO.
  
7. This the transaction shown on web portal with a crptocurrent and Samrt Contract simulation.  
