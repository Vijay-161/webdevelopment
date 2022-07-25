var nameError = document.getElementById('name_error');
var phoneError = document.getElementById('phone_error');
var emailError = document.getElementById('email_error');
var addressError = document.getElementById('address_error');
var submitError = document.getElementById('submit_error');
var passwordError = document.getElementById('password_error');
var confirmPasswordError = document.getElementById('confirmPassword_error');

function validateName(){
    var name= document.getElementById('contactName').value;
 

    if(name.length ==0){
        nameError.innerHTML = "Name required";
        return false;
    }
    if(!name.match(/^[A-Za-z]*\s{1}[A-Za-z]*$/)){
        nameError.innerHTML = "Write fullName";
        return false;
    }
    nameError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}

function validatePhone(){
    var phone = document.getElementById('contactPhone').value;

    if (phone.length ==0){
        phoneError.innerHTML ='Phone required';
        return false;
    }
    if (phone.length !==10){
        phoneError.innerHTML ='10 digits required';
        return false;
    }
    if (!phone.match(/^[0-9]{10}$/)){
        phoneError.innerHTML ='Only digits';
        return false;
    }

    phoneError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}

function validateEmail(){
    var email = document.getElementById('contactEmail').value;

    if(email.length ==0){
        emailError.innerHTML='Email required';
        return false;
    }
    if(!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)){
        emailError.innerHTML = 'Invalid';
        return false;
    }

    emailError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}

function validateAddress(){
    var address = document.getElementById('contactAddress').value;
    

    if(address.length ==0){
        addressError.innerHTML = "Address required";
        return false;
    }

    if(!address.match(/^[A-Za-z\._\-[0-9]*\s{1}[A-Za-z]*$/)){
        addressError.innerHTML = "Write full Address";
        return false;
    }


    addressError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}
function validatePassword(){
    var password = document.getElementById('contactPassword').value;

    if(password.length ==0){
        passwordError.innerHTML = "Password required";
        return false;
    }
    if(password.length<6){
        passwordError.innerHTML = "Minimum 6 characters";
        return false;
    }
    passwordError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}

function validateConfirmPassword(){
    var confirmPassword = document.getElementById('contactConfirmPassword').value;
    var password = document.getElementById('contactPassword').value;

    if(confirmPassword.length ==0){
        confirmPasswordError.innerHTML = "Password required";
        return false;
    }
    if(confirmPassword.length<6){
        confirmPasswordError.innerHTML = "Minimum 6 characters";
        return false;
    }
    if(confirmPassword != password){
        confirmPasswordError.innerHTML = "Not matched with password"
        return false;
    }
    confirmPasswordError.innerHTML='<i class="fas fa-check-circle"></i>';
    return true;
}

// function validateForm(){
//     if (!validateName() || !validateEmail() || !validatePhone() || !validateAddress() || !validatePassword() || !validateConfirmPassword()){
//         submitError.style.display='block';
//         submitError.innerHTML = 'Please! Fix error to submit form';
//         setTimeout(function(){submitError.style.display = 'none';},3000);
//         return false
//     }
// }