console.log('1\n2\n3\n4\n5\n6\n7\n8\n9\n10');

let result = prompt("Enter your Name");
console.log("Hello,", result);

let num = prompt("enter a number");
num = Number(num)
if(isNaN(num))
{
    num = 20;
}
num = num + 10;
console.log(num);

let grade = prompt("enter grade number");
grade = Number (grade);

 if(grade>=70)
 {
     console.log("you pass")
} 
 else 
 {
 console.log("you Fail")
}