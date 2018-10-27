from django.shortcuts import render
import time
from web3 import Web3, HTTPProvider
from solc import compile_files

web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
con = web3.eth.contract(address='0xA50c68aeE104dCB57467144C0BA78d2Abf5931E8',abi=[{'constant': False, 'inputs': [], 'name': 'toContract', 'outputs': [], 'payable': True, 'stateMutability': 'payable', 'type': 'function'}, {'constant': False, 'inputs': [{'name': 'toAddress', 'type': 'address'}], 'name': 'toAccount', 'outputs': [], 'payable': False, 'stateMutability': 'nonpayable', 'type': 'function'}, {'constant': True, 'inputs': [{'name': 'accountAddress', 'type': 'address'}], 'name': 'getBalance', 'outputs': [{'name': '', 'type': 'uint256'}], 'payable': False, 'stateMutability': 'view', 'type': 'function'}])
# Create your views here.
def main_view(request):
	return render(request,"main_view.html",{})

#def result(request):
def allAccounts(request):
	# accountData={}
	# #i=int(request.POST.get('accountIndex'))
	# for i in web3.eth.accounts:
	# 	accountData[i]=web3.fromWei(web3.eth.getBalance(i),'ether')
	# #amount=int(web3.fromWei(web3.eth.getBalance(web3.eth.accounts[i-1]),'ether'))
	return render(request,"allAccounts.html")

def resultallAccounts(request):
	time.sleep(5)
	accountData={}
	for i in web3.eth.accounts:
		accountData[i]=web3.fromWei(web3.eth.getBalance(i),'ether')
	return render(request,"resultallAccounts.html",{'ans':accountData})

def transfer(request):
	return render(request,"transfer.html")

def resultTransfer(request):
	# transaction = {
	# #'to':str(request.POST.get('toAccount')),
	# 'from':str(request.POST.get('fromAccount')),
	# 'value':int(web3.toWei(request.POST.get('amount'),'ether')),
	# 'gas':6721975,
	# 'gasPrice': 2000000000,
	# 'nonce':web3.eth.getTransactionCount(request.POST.get('fromAccount'))
	# }
	# key='a2046be017aa64a718e8c7295e218c33b4d2b1828e903dcba5e9298b68993696'
	# signed_trans = web3.eth.account.signTransaction(transaction,key)
	# transaction_id=web3.eth.sendRawTransaction(signed_trans.rawTransaction)
	# #transaction_id=web3.eth.sendTransaction(transaction)
	transaction = {
	'from':str(request.POST.get('fromAccount')),
	'value':int(request.POST.get('amount'))#int(web3.toWei(request.POST.get('amount'),'ether')),
	}
	transaction_id = con.functions.toContract().transact(transaction)
	con.functions.toAccount(str(request.POST.get('toAddress'))).transact({'from':str(request.POST.get('fromAccount'))})
	#return render(request,'resultallAccounts.html',{})
	return resultallAccounts(request)