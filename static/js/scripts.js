document.addEventListener('DOMContentLoaded', function() {
    const registerForm = document.getElementById('registerForm');
    const postForm = document.getElementById('postForm');
    const postsList = document.getElementById('posts-list');

    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('username').value;
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;

        fetch('/users/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, email, password }),
        })
        .then(response => response.json())
        .then(data => alert(data.message))
        .catch(error => console.error('Error:', error));
    });

    postForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const username = document.getElementById('post-username').value;
        const content = document.getElementById('content').value;

        fetch('/posts/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, content }),
        })
        .then(response => response.json())
        .then(post => {
            const postItem = document.createElement('div');
            postItem.className = 'post-item';
            postItem.innerHTML = `
                <h4>${post.author}</h4>
                <p>${post.content}</p>
                <small>${post.timestamp}</small>
            `;
            postsList.appendChild(postItem);
        })
        .catch(error => console.error('Error:', error));
    });
});
