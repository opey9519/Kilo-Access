import type { GetUsersResponse, ApiError, GetUserResponse } from "./utility/interface";

// GET | retrieves all users
export async function get_users(): Promise <GetUsersResponse | ApiError> {
    try {
        const response = await fetch("https://kilo-access-server.onrender.com/users", {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });
 
        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to fetch all users." };
        };

        const data = await response.json();
        return data as GetUsersResponse;
    } catch (error) {
        console.log("Failed to fetch all users", error)
        return { error: true, message: "Network error while fetching users." };
    }
}

// GET | retrieve specific user & qr code
export async function get_user(id: number): Promise <GetUserResponse | ApiError> {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/user/${id}`, {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        });

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: `Failed to fetch user ${id}` };
        }

        const data = await response.json();
        return data as GetUserResponse;
    } catch (error) {
        console.log(`Failed to fetch user ${id}`, error)
        return { error: true, message: `Network error while fetching user ${id}.` };
    }
}