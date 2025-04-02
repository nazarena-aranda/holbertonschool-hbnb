function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) return parts.pop().split(';').shift();
}

function checkAuthentication() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
    const logoutLink = document.getElementById('logout-link');
    
    if (loginLink && logoutLink) {
        if (!token) {
            loginLink.style.display = 'block';
            logoutLink.style.display = 'none';
        } else {
            loginLink.style.display = 'none';
            logoutLink.style.display = 'block';
        }
    }
}

async function fetchPlaces() {
    try {
        const response = await fetch('http://localhost:5000/api/v1/places', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            credentials: 'include'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const places = await response.json();
        displayPlaces(places);
    } catch (error) {
        console.error('Error fetching places:', error);
        showError('Error loading places. Please try again later.');
    }
}

function displayPlaces(places) {
    const placesList = document.getElementById('places-list');
    if (!placesList) return;

    placesList.innerHTML = ''; 

    places.forEach(place => {
        const placeCard = document.createElement('div');
        placeCard.className = 'place-card';
        
        placeCard.innerHTML = `
            <h2>${place.title}</h2>
            <p class="price">Price: $${place.price}</p>
            <p class="description">${place.description}</p>
            <button class="view-details" onclick="window.location.href='place.html?id=${place.id}'">View Details</button>
        `;
        
        placesList.appendChild(placeCard);
    });
}

function filterPlaces(maxPrice) {
    const places = document.querySelectorAll('.place-card');
    
    places.forEach(place => {
        const priceText = place.querySelector('.price').textContent;
        const priceMatch = priceText.match(/\$?\s*(\d+)/);
        const price = priceMatch ? parseInt(priceMatch[1]) : 0;
        
        if (maxPrice === 'all' || parseInt(maxPrice) >= price) {
            place.style.display = '';
        } else {
            place.style.display = 'none';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    checkAuthentication();

    const currentPage = window.location.pathname.split('/').pop();
    
    switch (currentPage) {
        case 'index.html':
        case '':
            fetchPlaces();
            break;
        case 'place.html':
            handlePlaceDetailsPage();
            break;
    }

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

    const logoutLink = document.getElementById('logout-link');
    if (logoutLink) {
        logoutLink.addEventListener('click', (event) => {
            event.preventDefault();
            document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
            window.location.href = 'login.html';
        });
    }
});

async function handlePlaceDetailsPage() {
    const urlParams = new URLSearchParams(window.location.search);
    const placeId = urlParams.get('id');
    
    if (placeId) {
        await fetchPlaceDetails(placeId);
    } else {
        showError('No place ID provided');
    }
}

async function fetchPlaceDetails(placeId) {
    try {
        const response = await fetch(`http://localhost:5000/api/v1/places/${placeId}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            credentials: 'include'
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const place = await response.json();
        displayPlaceDetails(place);
    } catch (error) {
        console.error('Error fetching place details:', error);
        showError('Error loading place details. Please try again later.');
    }
}

function showError(message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'error-message';
    errorDiv.textContent = message;
    
    const container = document.getElementById('place-details') || document.getElementById('places-list');
    if (container) {
        container.insertBefore(errorDiv, container.firstChild);
        setTimeout(() => errorDiv.remove(), 5000); // Remove after 5 seconds
    }
}

function displayPlaceDetails(place) {
    const placeDetails = document.getElementById('place-details');
    if (!placeDetails) return;

    placeDetails.innerHTML = `
        <div class="place-details">
            <h2>${place.title}</h2>
            <p class="description">${place.description || 'No description available'}</p>
            <div class="info">
                <p><strong>Price:</strong> $${place.price}</p>
                <p><strong>Location:</strong> ${place.latitude}, ${place.longitude}</p>
            </div>
            <div class="amenities">
                <h3>Amenities</h3>
                <ul>
                    ${place.amenities ? place.amenities.map(amenity => `<li>${amenity.name}</li>`).join('') : '<li>No amenities available</li>'}
                </ul>
            </div>
            <div class="reviews">
                <h3>Reviews</h3>
                <ul>
                    ${place.reviews && place.reviews.length > 0 
                        ? place.reviews.map(review => `
                            <li>
                                <p>${review.text}</p>
                                <p>Rating: ${review.rating}/5</p>
                                <p>By: ${review.author ? `${review.author.first_name} ${review.author.last_name}` : 'Anonymous'}</p>
                            </li>
                        `).join('')
                        : '<li>No reviews yet</li>'
                    }
                </ul>
            </div>
            <button onclick="window.location.href='add_review.html?place_id=${place.id}'">Add Review</button>
        </div>
    `;
}