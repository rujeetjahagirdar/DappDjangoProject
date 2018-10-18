from django.shortcuts import render
from web3 import Web3, HTTPProvider

# Create your views here.
def main_view(request):
	return render(request,"main_view.html",{})

def result(request):
	i=int(request.POST.get('accountIndex'))
	web3=Web3(HTTPProvider('http://127.0.0.1:7545'))
	amount=int(web3.fromWei(web3.eth.getBalance(web3.eth.accounts[i-1]),'ether'))
	return render(request,"result.html",{'ans':amount})