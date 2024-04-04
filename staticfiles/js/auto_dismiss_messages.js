document.addEventListener('DOMContentLoaded', (event) => {
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(function(alert) {
        setTimeout(function() {
            let bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();

            alert.addEventListener('closed.bs.alert', function () {
                alert.remove();

                if (!alert.parentNode.querySelector('.alert-dismissible')) {
                    alert.parentNode.style.height = '0';
                }
            });
        }, 3000);
    });
});