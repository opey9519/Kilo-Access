import { getAuthHeaders } from "../utility/utility";

// POST | Creates an athlete given credentials (Must be an admin to call this)
export async function create_athlete(token: string, first_name: string, last_name: string, is_admin: boolean, kilo_access: boolean) {
    try {
        const response = await fetch("https://kilo-access-server.onrender.com/athlete", {
            method: "POST",
            headers: getAuthHeaders(token),
            body: JSON.stringify({first_name, last_name, is_admin, kilo_access})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to create athlete." };
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Failed to create athlete", error);
        return { error: true, message: "Network error while creating athlete." };
    }
}

// PUT | Edits an athletes name
export async function edit_athlete(id: number, token: string, new_first_name: string, new_last_name: string, has_kilo_access: boolean) {
    console.log(has_kilo_access)
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/athlete/${id}`, {
            method: "PUT",
            headers: getAuthHeaders(token),
            body: JSON.stringify({new_first_name, new_last_name, has_kilo_access})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to edit athlete." };
        }

        const data = await response.json();
        console.log(data)
        return data;
    } catch (error) {
        console.log("Failed to edit athlete", error);
        return { error: true, message: "Network error while editing athlete." };       
    }
}

// PATCH | Updates kilo access of athlete
export async function update_athlete_kilo_access(id: number, token: string, kilo_access: boolean) {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/athlete/${id}`, {
            method: "PATCH",
            headers: getAuthHeaders(token),
            body: JSON.stringify({kilo_access})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to edit athlete kilo priviliges."};
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Failed to edit athlete kilo priviliges", error);
        return { error: true, message: "Network error while editing athlete kilo priviliges." };       
    }
}

// DELETE | Deletes athlete from database
export async function delete_athlete(id: number, token: string) {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/athlete/${id}`, {
            method: "DELETE",
            headers: getAuthHeaders(token)
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to delete athlete."};
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.log("Failed to delete athlete", error);
        return { error: true, message: "Network error while deleting athlete." };       
    }
}