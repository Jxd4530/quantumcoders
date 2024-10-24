document.getElementById('process-payment').addEventListener('click', function() {
    const checkbox = document.getElementById('payment-checkbox');
    if (checkbox.checked) {
        document.getElementById('loading').style.display = 'block';
        
        setTimeout(() => {
            document.getElementById('loading').style.display = 'none';
            document.getElementById('otp-dialog').style.display = 'block';
        }, 2000); // Simulating a 2-second loading time
    } else {
        alert('Please check the box to proceed with payment.');
    }
});

document.getElementById('proceed-otp').addEventListener('click', function() {
    const otpInput = document.getElementById('otp-input').value;
    if (otpInput) {
        document.getElementById('otp-dialog').style.display = 'none';
        document.getElementById('success-message').style.display = 'block';
    } else {
        alert('Please enter the OTP.');
    }
});
