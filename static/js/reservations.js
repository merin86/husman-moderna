/**
 * This script handles the deletion of reservations within the web application. 
 * The script queries all delete buttons identified by the attribute 'data-bs-toggle="modal"'.
 */
document.addEventListener("DOMContentLoaded", function() {
    var deleteButtons = document.querySelectorAll('button[data-bs-toggle="modal"]');
    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            var deleteUrl = button.getAttribute('data-delete-url');
            var deleteForm = document.getElementById('deleteForm');
            deleteForm.action = deleteUrl;
        });
    });
});