/* Refrence: https://medium.com/coinmonks/build-a-dapp-using-ethereum-and-angular-6-a404fbf3c08d
			 https://truffleframework.com/docs/ganache/quickstart
 */

pragma solidity ^0.4.25;

/**
 * The Payments contract does this and that...
 */
contract Payments {
	address transferFrom;
	address transferTo;
	uint paymentAmout;
	constructor() public {
		transferFrom=msg.sender;
	}

	event TransferFund(address _transferTo, address _transferFrom, uint amount);

	function transferFund (address _transferTo) public payable returns (bool) {
		transferTo = _transferTo;
		transferTo.transfer(msg.value);

		emit TransferFund(transferTo, transferFrom,msg.value);
		return true;		
	}

	function getBalanceOfCurrentAccount () public payable returns (uint) {
		return transferFrom.balance;
	}
	
	
	

	}