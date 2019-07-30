const GetNumber = (x) =>
{
    while(true){ 
        let response = Number(prompt('enter a number'))
        if(!isNaN(response) && response === Math.abs(response)){
            console.log()
        }
    }
    console.log ('num' - Math.abs(4));
}
