const Web3 = require("web3")
const web3 = new  Web3(new Web3.providers.HttpProvider("https://rinkeby.infura.io/v3/95fc29f445c94dbaadd33f4b20dd5d97"))


web3.eth.getBalance("0x5408142593bA953843811B24570397708599558C", function(err, result) {
    if (err) {
      console.log(err)
    } else {
      console.log("Your balance in account "+ web3.utils.fromWei(result, "ether") + " ETH")
    }
  })
  
const address  = "0x61b7886EF3A08Ef2432d20D5DD62eB4A9941DC60"
const abi = JSON.parse('[{"constant":false,"inputs":[{"name":"_customer","type":"address"},{"name":"_cost","type":"uint256"}],"name":"setprice","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"transaction","outputs":[{"name":"customer","type":"address"},{"name":"ownerE","type":"address"},{"name":"value","type":"uint256"},{"name":"status_payment","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"status","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"yourcost","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"BuyToken","outputs":[{"name":"success","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"initialSupply","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
const contract = new web3.eth.Contract(abi, address)
  

contract.methods.status("0xd17455A243D297462bb609CBAAeE83d9BEA3947E").call()
.then(console.log,function(result){});


//const transaction = contract.methods.transaction("0xd17455A243D297462bb609CBAAeE83d9BEA3947E").call().then(console.log,function(result){})

 
 function transac(id){
  return contract.methods.transaction(id).call()
 }


 data = transac("0xd17455A243D297462bb609CBAAeE83d9BEA3947E").then(function(result) {
  console.log( JSON.stringify(result.status_payment))
  if (JSON.stringify(result.status_payment == true)){
    console.log("Relay on")
  } else{
    console.log("Relay off")
  }
})

 
