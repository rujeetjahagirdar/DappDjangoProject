from django.shortcuts import render
from web3 import Web3, HTTPProvider

web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
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
	accountData={}
	for i in web3.eth.accounts:
		accountData[i]=web3.fromWei(web3.eth.getBalance(i),'ether')
	return render(request,"resultallAccounts.html",{'ans':accountData})

def transfer(request):
	return render(request,"transfer.html")

def resultTransfer(request):
	transaction = {
	#'to':str(request.POST.get('toAccount')),
	'from':str(request.POST.get('fromAccount')),
	'value':int(web3.toWei(request.POST.get('amount'),'ether')),
	'gas':6721975,
	'gasPrice': 2000000000,
	'nonce':web3.eth.getTransactionCount(request.POST.get('fromAccount'))
	}
	key='a2046be017aa64a718e8c7295e218c33b4d2b1828e903dcba5e9298b68993696'
	signed_trans = web3.eth.account.signTransaction(transaction,key)
	transaction_id=web3.eth.sendRawTransaction(signed_trans.rawTransaction)
	#transaction_id=web3.eth.sendTransaction(transaction)
	return render(request,'resultTransfer.html',{'Id':transaction_id})