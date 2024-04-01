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