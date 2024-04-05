/**
 * This script automatically dismisses and removes Bootstrap alerts after 3 seconds.
 * The script queries all elements with the class 'alert-dismissible' to identify dismissible Bootstrap alerts.
 * Upon dismissal, the alert is removed from the DOM to prevent it from taking up space or affecting layout.
 */
document.addEventListener('DOMContentLoaded', (event) => {
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();

            // Once the alert is closed, remove it from the DOM
            alert.addEventListener('closed.bs.alert', function () {
                alert.remove();

                // If there are no more alerts, remove the extra space by setting the container's height to 0
                if (!alert.parentNode.querySelector('.alert-dismissible')) {
                    alert.parentNode.style.height = '0';
                }
            });
        }, 3000);
    });
});