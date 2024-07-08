function UpdateUserCoin(){
    const username = document.getElementById("username").textContent;
    const value = document.getElementById("coin-counter-text").textContent;
    const url = "http://127.0.0.1:8000/tunnel/addcoin/"+username+"/"+value+"/";
    const params = {
        method:"POST"
    }
    fetch(url , params)
    .then(data=>{console.log(data)})
    .then(res=>{console.log(res)})
}

setInterval(UpdateUserCoin , 2000);