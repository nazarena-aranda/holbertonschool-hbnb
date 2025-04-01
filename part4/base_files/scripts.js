
function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}


function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');

    
    if (loginLink) {
        if (!token) {
            loginLink.style.display = 'block';
        } else {
            loginLink.style.display = 'none';
            
            fetchPlaces(token);
        }
    }
}


async function fetchPlaces(token) {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (!response.ok) {
            throw new Error('Failed to fetch places');
        }

        const places = await response.json();
        displayPlaces(places);
    } catch (error) {
    }
}


function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = ''; 

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        placeCard.dataset.price = place.price_per_night;
        
        placeCard.innerHTML = `
            <h2>${place.name}</h2>
            <p class="price">Price per night: $${place.price_per_night}</p>
            <button class="view-details" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
        `;
        
        placesList.appendChild(placeCard);
    });
}


function filterPlaces(maxPrice) {
    const places = document.querySelectorAll('.place-card');
    
    places.forEach(place => {
        const price = parseInt(place.dataset.price);
        if (maxPrice === 'all' || price <= maxPrice) {
            place.style.display = 'block';
        } else {
            place.style.display = 'none';
        }
    });
}


document.addEventListener('DOMContentLoaded', () => {
   
    checkAuthentication();

 
    const priceFilter = document.getElementById('price-filter');
    if (priceFilter) {
        priceFilter.addEventListener('change', (event) => {
            filterPlaces(event.target.value);
        });
    }

 
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://localhost:5000/api/v1/auth/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ email, password })
                });

                if (response.ok) {
                    const data = await response.json();
                    
                    const expirationDate = new Date();
                    expirationDate.setDate(expirationDate.getDate() + 7);
                    document.cookie = `token=${data.access_token}; expires=${expirationDate.toUTCString()}; path=/`;
                    
                   
                    window.location.href = 'index.html';
                } else {
                    const errorData = await response.json();
                    alert('Login failed: ' + (errorData.message || response.statusText));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during login. Please try again.');
            }
        });
    }

    const signupForm = document.getElementById('signup-form');
    if (signupForm) {
        signupForm.addEventListener('submit', async (event) => {
            event.preventDefault();
            
            const first_name = document.getElementById('first_name').value;
            const last_name = document.getElementById('last_name').value;
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;

            try {
                const response = await fetch('http://localhost:5000/api/v1/auth/signup', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        first_name,
                        last_name,
                        email,
                        password
                    })
                });

                if (response.ok) {
                    const data = await response.json();
                    
                    const expirationDate = new Date();
                    expirationDate.setDate(expirationDate.getDate() + 7);
                    document.cookie = `token=${data.access_token}; expires=${expirationDate.toUTCString()}; path=/`;
                    
                    window.location.href = 'index.html';
                } else {
                    const errorData = await response.json();
                    alert('Signup failed: ' + (errorData.message || response.statusText));
                }
            } catch (error) {
                console.error('Error:', error);
                alert('An error occurred during signup. Please try again.');
            }
        });
    }
});