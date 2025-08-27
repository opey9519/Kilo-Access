// Retrieves JWT token from local storage
export function getToken() {
    const token = localStorage.getItem("token");

    return token;
}

// Returns common parameters
export function getAuthHeaders(token: string) {
    return {
        "Authorization": `Bearer ${token}`,
        "Content-Type": "application/json"
    };
}

// Retrieves Refresh token from local storage
export function getRefreshToken() {
    const refresh_token = localStorage.getItem("refresh_token");

    return refresh_token;
}