function myAlarm(m)
{
    console.log("WakeUp");
    console.log("Hey, kobe, it's " + m);
    console.log ("WAKE UP, WAKE UP, WAKE UP!!")
}


myAlarm("6:30am");
myAlarm("6:67am");
myAlarm("6:55am");


let result = prompt("enter your name");
// myAlarm()
familyalarm(result, "6:00am");

function familyalarm(name,time)
{
    console.log("hey"+ name + "Wake up. It's " + time);
}