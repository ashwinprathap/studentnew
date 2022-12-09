var nam=document.getElementById('name');
var email=document.getElementById('email');
var phno=document.getElementById('phno');
var pass1=document.getElementById('pass1');
var pass2=document.getElementById('pass2');

function validname(){
    var fn = nam.value;
    if (isNaN(fn)){
        nam.className = "success";
        document.getElementById("text").innerHTML = "";
    
    }else{
        nam.className ="error";
        document.getElementById("signup").disabled = true;
        document.getElementById("text").innerHTML ="please enter name";
    }

 }
function validmail(){
    var mail=email.value;
    var re=/^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;
    if (re.test(mail)){
        email.className="success";
        document.getElementById("text").innerHTML="";
    }
    else{
        email.className="error";
        document.getElementById("text").innerHTML="please enter a valid mail id"
    }
}
function validphn(){
    var num=phno.value;
    if (isNaN(num)){
        phno.className="error";
        document.getElementById("signup").disabled= true;
        document.getElementById("text").innerHTML="please enter a valid  phone no";

    }
    else{
        var numl=num.length;
        if (numl == 10){
            phno.className="success";
            document.getElementById("text").innerHTML=""
        }else{
            phno.className="error";
            document.getElementById("signup").disabled= true;
            document.getElementById("text").innerHTML="please enter a valid  phone no";
        }
       
    }
}

function validpass(){
    var passl = pass1.value.length;
    if(passl >= 8 & pass1 <= 16){
        pass1.className = "success";
        document.getElementById("text").innerHTML="";
    }
    else{
        pass1.className ="error";
        document.getElementById("signup").disabled= true;
        document.getElementById("text").innerHTML="password length must be greater than 8 charecters.and not excced 15";

    }
}
function validpassconform(){
    var pass = pass1.value;
    var passc = pass2.value;
    if(pass == passc){
        pass2.className = "success";
        document.getElementById("text").innerHTML="";
        document.getElementById("signup").disabled= true;
    }
    else{
        pass2.className ="error";
        document.getElementById("signup").disabled= true;
        document.getElementById("text").innerHTML="password are not matched";

    }
}