// Function to toggle the sidebar
function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('show');

    const mainContent = document.getElementById('main-content');
    if (sidebar.classList.contains('show')) {
        mainContent.style.marginLeft = '250px'; // Adjust for the sidebar width
    } else {
        mainContent.style.marginLeft = '0';
    }
}

// Event listener for the toggle button
const toggleButton = document.querySelector('.toggle-btn');
toggleButton.addEventListener('click', toggleSidebar);
