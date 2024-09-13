// checkbox1=document.getElementById("cb1")
// checkbox1.addEventListener('change', function () {
//     document.getElementById()
// });

document.addEventListener('DOMContentLoaded', function() {
    const checkboxes = document.querySelectorAll('.checkbox');
    
    checkboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const taskRow = this.closest('tr');
            if (this.checked) {
                taskRow.classList.add('completed');
            } else {
                taskRow.classList.remove('completed');
            }
        });
    });
});