document.getElementById("process").onclick=function(){
    const path = document.getElementById("input_text").value;
    fetch(path)
        .then((response) => response.json())
        .then(res =>{
            console.log(res.data);
            document.getElementById("data").innerHTML = FormatSting(res.data);
        })
        .catch((error)=>{
            document.getElementById("data").innerHTML = "Сервер не вернул значений";
            console.error(error)
        });
    }
    function FormatSting(data) {

        let formatedStr = [];
        
        for(let element in data){
            formatedStr.push(data[element]);            
        }
        formatedStr.reverse();
        
        formatedStr = formatedStr.join(' ');

        console.log(formatedStr);

        return formatedStr;
    };
    