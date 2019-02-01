# DappDjangoProject
Trying to develope a distributed webapp to securely store user's documents on the decentralized system using Django and IPFS file system.

Modules:
1. User authentication
2. File upload
3. File download
4. User Creation

IPFS: Will be used to store file in decentralized manner. A user will be able to view and upload new files to IPFS.

Encryption: Somekind of encryption will be used to securly share the files. 

Blockchain: The article below states that blockchain can be used to store hashes of file stored on IPFS. But not sure how to make it or how it works. (Needs to read more)
https://medium.com/@mycoralhealth/learn-to-securely-share-files-on-the-blockchain-with-ipfs-219ee47df54c


Current Idea:

The user will signup/login to the his ethereum account with the help of his private key or traditional username/password combination. For every user his respective file hashes will be stored in his ethereum account. These file hashes will be used to access the users file on IPFS. If third party gets handson these hash of files then the files won't be secured so before uploading files to IPFS the files will be encrypted with users private key.

To read:

1. User session management on ethereum/ login mechanism for ethereum
2. how to interact between ethereum and IPFS
3. encryption of files, generating private keys,ect..
4. File size limitations (if any)
