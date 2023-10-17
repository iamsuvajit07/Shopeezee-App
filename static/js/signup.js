const wrapper = document.querySelector('.wrapper');
const form = document.querySelector('form');
const nextBtn = document.getElementById('next');
const hideIcon = document.querySelector('#hide-icon');
const showIcon = document.querySelector('#show-icon');
const conPasswordField = document.querySelector('#passwordcon-field');
const birthdate = document.getElementById('birthdate');
const passwordField = document.querySelector('#password-field');
const error = document.querySelector('#error');
const success = document.querySelector('#success');
const signup = document.getElementById('signup-link');
const backBtn = document.getElementById('back-btn');





// Wrap JavaScript code inside a DOMContentLoaded event listener
document.addEventListener('DOMContentLoaded', function () {
    // Get the form and submit button elements


    // Function to enable/disable the submit button based on form validity
    const validateForm = () => {
        if (form.checkValidity()) {
            nextBtn.removeAttribute('disabled');
        } else {
            nextBtn.setAttribute('disabled', true);
        }
    };

    // Add input event listeners to all form inputs
    form.querySelectorAll('input, select').forEach(input => {
        input.addEventListener('input', validateForm);
    });


    // Add onchange event listener to date input for age validation
    birthdate.addEventListener('change', function () {
        // Get the selected date
        const selectedDate = new Date(this.value);

        // Get 12 years ago from today
        const maxDate = new Date(Date.now() - 12 * 365 * 24 * 60 * 60 * 1000);
        maxDate.setHours(0, 0, 0, 0);

        // Compare the selected date to 12 years ago from today
        if (selectedDate > maxDate) {
            // If selected date is after 12 years ago from today, reset the input value
            this.value = '';
            alert('You must be at least 12 years old to sign up.');
        }

        validateForm();

    });



});





// Add click event listener to the next button
nextBtn.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent form submission

    //perform click on next button ---->>>>>>>
    wrapper.classList.add('active');

});

// Add click event listener to the back button
backBtn.addEventListener('click', function (event) {
    event.preventDefault(); // Prevent form submission

    //perform click on next button ---->>>>>>>
    wrapper.classList.remove('active');

});







// hide and show icon on password field ----->>>>>
function showPassword() {

    if (conPasswordField.type === 'password') {
        conPasswordField.type = 'text';
        hideIcon.style.display = 'none';
        showIcon.style.display = 'block';

    } else {
        conPasswordField.type = 'password';
        hideIcon.style.display = 'block';
        showIcon.style.display = 'none';

    }

};







// password & confirm password checker ----->>>


function validatePassword() {
    const passwordValue = passwordField.value.trim();
    const confirmValue = conPasswordField.value.trim();

    if (passwordValue === '' || confirmValue === '') {
        signup.disabled = true;
        success.style.display = 'none';
    } else if (passwordField.value !== conPasswordField.value) {
        error.style.display = 'block';
        success.style.display = 'none';
        signup.disabled = true;
    } else {
        error.style.display = 'none';
        success.style.display = 'block';
        signup.disabled = false;
    }
};

passwordField.addEventListener('change', validatePassword);
conPasswordField.addEventListener('keyup', validatePassword);