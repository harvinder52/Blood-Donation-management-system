
function handleFormSubmit() {
    const form = document.forms['myform1'];

    if (form.checkValidity()) {
        // Show Bootstrap Modal
        var successModal = new bootstrap.Modal(document.getElementById('successModal'));
        successModal.show();

        // Clear the form after a short delay
        setTimeout(() => {
            form.reset();
        }, 1000);
    } else {
        form.reportValidity(); // shows validation messages
    }
}

