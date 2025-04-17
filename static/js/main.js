// Add active class to current navigation item
document.addEventListener('DOMContentLoaded', function() {
    const currentLocation = window.location.pathname;
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
    
    navLinks.forEach(link => {
        const linkPath = link.getAttribute('href');
        if (currentLocation === linkPath || 
            (linkPath !== '/' && currentLocation.startsWith(linkPath))) {
            link.classList.add('active');
            link.style.color = getComputedStyle(document.documentElement)
                .getPropertyValue('--gold-gradient-start');
        }
    });

    // Initialize tooltips if any
    if (typeof bootstrap !== 'undefined' && bootstrap.Tooltip) {
        const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
        tooltipTriggerList.map(function (tooltipTriggerEl) {
            return new bootstrap.Tooltip(tooltipTriggerEl);
        });
    }

    // Add scroll animation for cards
    const animateOnScroll = () => {
        const cards = document.querySelectorAll('.service-card');
        cards.forEach(card => {
            const cardPosition = card.getBoundingClientRect().top;
            const screenPosition = window.innerHeight / 1.3;
            
            if (cardPosition < screenPosition) {
                card.style.transform = 'translateY(0)';
                card.style.opacity = '1';
            }
        });
    };

    // Set initial state for cards
    document.querySelectorAll('.service-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(20px)';
        card.style.transition = 'all 0.6s ease-out';
    });

    // Run on load and scroll
    window.addEventListener('scroll', animateOnScroll);
    animateOnScroll();
});