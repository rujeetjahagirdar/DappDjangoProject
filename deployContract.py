from web3 import Web3, HTTPProvider
from solc import compile_files
import time
web3 = Web3(HTTPProvider('http://127.0.0.1:7545'))
compile_sol = compile_files(['/home/rujeet/Desktop/payment1.sol']);
contract_interface = compile_sol['/home/rujeet/Desktop/payment1.sol:payThem'];
MyContractClass=web3.eth.contract(abi=contract_interface['abi'],bytecode=contract_interface['bin']);
tx_hash = MyContractClass.deploy(transaction = {'from':web3.eth.accounts[1]});
time.sleep(3)
tx_receipt = web3.eth.getTransactionReceipt(tx_hash);
time.sleep(3)
print(tx_receipt['contractAddress'])
con = web3.eth.contract(address=tx_receipt.contractAddress,abi=contract_interface['abi'])
