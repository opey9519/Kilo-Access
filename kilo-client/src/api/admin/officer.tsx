import { getAuthHeaders } from "../utility/utility";

// POST | Creates officer given credentials (Must be an admin to call this) 
export async function create_officer(token: string, first_name: string, last_name: string, is_admin: boolean, kilo_access: boolean, password: string) {
    try {
        const response = await fetch("https://kilo-access-server.onrender.com/officer", {
            method: "POST",
            headers: getAuthHeaders(token),
            body: JSON.stringify({first_name, last_name, is_admin, kilo_access, password})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to create officer." };
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Failed to create officer", error);
        return { error: true, message: "Network error while creating officer." };
    }
}

// PUT | Edits an officers name
export async function edit_officer(id: number, token: string, new_first_name: string, new_last_name: string, has_kilo_access: boolean) {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/officer/${id}`, {
            method: "PUT",
            headers: getAuthHeaders(token),
            body: JSON.stringify({new_first_name, new_last_name, has_kilo_access})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to edit officer." };
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Failed to edit officer", error);
        return { error: true, message: "Network error while editing officer." };       
    }
}

// PATCH | Updates kilo access of officer
export async function update_officer_kilo_access(id: number, token: string, kilo_access: boolean) {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/officer/${id}`, {
            method: "PATCH",
            headers: getAuthHeaders(token),
            body: JSON.stringify({kilo_access})
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to edit officer kilo priviliges."};
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.log("Failed to edit officer kilo priviliges", error);
        return { error: true, message: "Network error while editing officer kilo priviliges." };       
    }
}

// DELETE | Deletes athlete from database
export async function delete_officer(id: number, token: string) {
    try {
        const response = await fetch(`https://kilo-access-server.onrender.com/officer/${id}`, {
            method: "DELETE",
            headers: getAuthHeaders(token)
        })

        if (!response.ok) {
            console.error("Server returned error:", await response.text());
            return { error: true, message: "Failed to delete officer."};
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.log("Failed to delete officer", error);
        return { error: true, message: "Network error while deleting officer." };       
    }
}