document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("login-form");
    const errorMessage = document.getElementById("error-message");

    form.addEventListener("submit", async function(event) {
        event.preventDefault();
        
        const username = form.username.value;
        const password = form.password.value;

        try {
            const response = await fetch("/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ username, password })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail);
            }

            window.location.href = "/dashboard"; // Redirecionar para a página de dashboard após o login bem-sucedido
        } catch (error) {
            errorMessage.textContent = error.message;
        }
    });
});
