import "./styles/KiloRoster.css"
import { get_users } from "../api/user";
import { useEffect, useState } from "react";
import type { User } from "../api/utility/interface";


function KiloRoster() {
    // Users object of interface type User
    const [users, setUsers] = useState<User[]>([]);

    //  Fetch users
    useEffect(() => {
        async function fetchUsers() {
            const result = await get_users();

            if ("users" in result) {
                setUsers(result.users);
            } else {
                console.error(result.message);
            }
        }

        fetchUsers();
    }, []);

    return (
    <div className="roster-container">
        <h2>Kilo Roster</h2>
        <table className="roster-table">
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Is Admin</th>
                    <th>Has Kilo Access</th>
                </tr>
            </thead>
            <tbody>
            {users.map((user) => (
                <tr key={user.id} className="roster-row">
                    <td>{user.first_name}</td>
                    <td>{user.last_name}</td>
                    <td>{user.is_admin ? "✅" : "❌"}</td>
                    <td>{user.kilo_access ? "✅" : "❌"}</td>
                </tr>
            ))}
            </tbody>
        </table>
    </div>
    );
}

export default KiloRoster;
