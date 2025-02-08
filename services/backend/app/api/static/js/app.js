// JavaScript functionality for SwagPopUps

document.addEventListener('DOMContentLoaded', () => {
    console.log('SwagPopUps website loaded successfully.');

    // Example: Add event listeners for dynamic elements
    const heroButton = document.querySelector('#regClick .btn');
    if (heroButton) {
        heroButton.addEventListener('click', () => {
            alert("Welcome to SwagPopUps! Let's get started!");
        });
    }

    const heroButton2 = document.querySelector('.regPromo .btn');
    if (heroButton2) {
        heroButton2.addEventListener('click', () => {
            alert("Welcome to SwagPopUps! Let's get started!");
        });
    }

    const heroButton3 = document.querySelector('#regClick');
    if (heroButton3) {
        heroButton3.addEventListener('click', () => {
            alert("Welcome to SwagPopUps! Let's get started!");
        });
    }

    // Example: Future functionality for AJAX requests
    // function fetchProducts() {
    //     fetch('/api/products')
    //         .then(response => response.json())
    //         .then(data => {
    //             console.log('Products:', data);
    //         })
    //         .catch(error => console.error('Error fetching products:', error));
    // }

    // Future code for managing interactions, animations, or API calls can be added here
});

document.addEventListener("DOMContentLoaded", function () {
    const quantityInputs = document.querySelectorAll('input[type="number"]');
    const totalElement = document.querySelector('.cart-summary h2');

    quantityInputs.forEach(input => {
        input.addEventListener('input', function () {
            let total = 0;
            document.querySelectorAll('tr').forEach(row => {
                const price = parseFloat(row.querySelector('.price').textContent);
                const quantity = parseInt(row.querySelector('input[type="number"]').value, 10);
                total += price * quantity;
            });
            totalElement.textContent = `Total: $${total.toFixed(2)}`;
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const applyFiltersButton = document.getElementById('applyFilters');
    const productGrid = document.getElementById('productGrid');
    const categoryFilter = document.getElementById('categoryFilter');
    const priceFilter = document.getElementById('priceFilter');

    applyFiltersButton.addEventListener('click', function () {
        const category = categoryFilter.value.toLowerCase();
        const maxPrice = parseFloat(priceFilter.value) || Infinity;

        Array.from(productGrid.children).forEach(productCard => {
            const productCategory = productCard.getAttribute('data-category').toLowerCase();
            const productPrice = parseFloat(productCard.getAttribute('data-price'));

            if (
                (category && productCategory !== category) ||
                (maxPrice && productPrice > maxPrice)
            ) {
                productCard.style.display = 'none';
            } else {
                productCard.style.display = 'block';
            }
        });
    });
});