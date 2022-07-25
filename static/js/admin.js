var x = document.getElementById("login");
var y = document.getElementById("register");
var z = document.getElementById("btn");

var error = document.getElementById("error")
error.style.height="10px"





function register(){
    x.style.left="-400px";
    y.style.left="50px";
    z.style.left="110px";
}
function login(){
    x.style.left="50px";
    y.style.left="450px";
    z.style.left="0px";
}

function validateName(){
    const name = document.getElementById("fname").value;
 

    if(name.length ==0){
        error.innerHTML = "First name required";
        error.style.color='red'
        return false;
    }
    if(!name.match(/^[A-Za-z]*$/)){
        error.innerHTML = "only letters";
        error.style.color='red'
        return false;
    }
    if(name.length <3){
        error.innerHTML = "Write Firstname";
        error.style.color='red'
        return false;
    }
    
    
    error.innerHTML='Valid';
    error.style.color='green'
    return true;
}

function validateLName(){
    const lname = document.getElementById("lname").value;

    if(lname.length ==0){
        error.innerHTML = "Lastname required";
        error.style.color='red'
        return false;
    }
    if(lname.length <3){
        error.innerHTML = "Write Surname";
        error.style.color='red'
        return false;
    }
    if(!lname.match(/^[A-Za-z]*$/)){
        error.innerHTML = "only letters";
        error.style.color='red'
        return false;
    }
    
    error.innerHTML='Valid';
    error.style.color='green'
    return true;

}

function validateEmail(){
    var email = document.getElementById('email').value;

    if(email.length ==0){
        error.innerHTML='Email is required';
        error.style.color='red'
        return false;
    }
    if(!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        error.innerHTML = 'Invalid';
        error.style.color='red'
        return false;
    }

    error.innerHTML='Valid';
    error.style.color='green'
    return true;
}

function validateUSer(){
    var user = document.getElementById('user').value;

    if(user.length ==0){
        error.innerHTML='Email is required';
        error.style.color='red'
        return false;
    }
    if(user.length<5){
        error.innerHTML = 'must have more than 5 char';
        error.style.color='red';
        return false;

    }
 
    error.innerHTML='Valid';
    error.style.color='green'
    return true;
}

function validatePassword(){
    var pasw = document.getElementById('pasw').value;

    if(pasw.length ==0){
        error.innerHTML='Password is required';
        error.style.color='red'
        return false;
    }
    if(pasw.length<5){
        error.innerHTML = 'must have more than 5 char';
        error.style.color='red';
        return false;

    }
 
    error.innerHTML='Valid';
    error.style.color='green'
    return true;
}

function validateForm(){
    if (!validateName() || !validateEmail() || !validateLName() || !validatePassword() || !validateUSer){
        // error.style.display='block';
        error.innerHTML = 'Please! Fix error to submit form';
        setTimeout(function(){error.style.display = 'none';},3000);
        return false;
    }
}