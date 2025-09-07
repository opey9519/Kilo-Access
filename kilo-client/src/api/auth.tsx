import type { ApiError, SigninResponse } from "./utility/interface";
import { getAuthHeaders } from "./utility/utility";
import { getToken } from "./utility/utility";

// POST | Signin, takes in first_name, last_name, password and returns JWT associated with User
export async function signin(
    first_name: string, last_name: string, password: string
    ): Promise <SigninResponse | ApiError> {
    try {
        const response = await fetch("https://kilo-access-server.onrender.com/signin", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({first_name, last_name, password})
        });

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to signin." };
        }

        const data = await response.json();
        return data as SigninResponse;

    } catch (error) {
        console.log("Failed to signin", error)
        return { error: true, message: "Network error while signing in." };
    }
}

// POST 
export async function signout(token: string) {
    try {
        const response = await fetch("https://kilo-access-server.onrender.com/signout", {
            method: "POST",
            headers: getAuthHeaders(token)
        });

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to signout." };          
        }

        const data = await response.json();
        return {"data":data, "status": response.status}
    } catch (error) {
        console.log("Failed to sign out", error)
        return { error: true, message: "Network error while signing out." };
    }
}


// POST | Refresh - Authorization required and refresh token required
export async function refreshAccessToken(refresh_token: string) {
    const token = getToken();


    if (!refresh_token) {
       console.log("No refresh token available");
       return;
    }

    try {
        const response = await fetch("https://kilo-access-server.onrender.com/refresh", {
            method: "POST",
            headers: {
                "Authorization": `Bearer ${token}`,
                "Content-Type": "application/json"
            },
            body: JSON.stringify({refresh_token})
        })

        if (!response.ok) {
            console.log("Failed to refresh token")
            localStorage.removeItem("token")
            localStorage.removeItem("refresh_token")
            // setUser({
            //     isAuthenticated: false,
            //     token: null
            // })
        }

        const refresh_response = await response.json()
        const new_access_token = refresh_response.access_token
        localStorage.setItem("token", new_access_token)
        return refresh_response;

    } catch (error) {
        console.log("Error refreshing access token", error)
    }
}