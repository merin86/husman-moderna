/**
 * This script enhances the deletion process of reviews on the website. Upon full loading of the document content,
 * it searches for all buttons that have a 'data-delete-url' attribute and attaches an event listener to each. 
 * These listeners handle the 'click' event to activate a confirmation dialogue.
 * This approach allows users to confirm their intention to delete a review, effectively preventing accidental deletions.
 */
document.addEventListener("DOMContentLoaded", function () {

    var deleteButtons = document.querySelectorAll('[data-delete-url]');
    deleteButtons.forEach(function (button) {

        button.addEventListener('click', function (event) {

            var deleteUrl = button.getAttribute('data-delete-url');
            var deleteConfirmBtn = document.getElementById('deleteReviewConfirmBtn');
            deleteConfirmBtn.href = deleteUrl;

            var deleteModal = new bootstrap.Modal(document.getElementById('deleteConfirmModal'));
            deleteModal.show();
        });
    });
});