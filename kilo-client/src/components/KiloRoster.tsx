import "./styles/KiloRoster.css"
import type { User } from "../api/utility/interface";
import { get_users } from "../api/user";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";



function KiloRoster() {
    // Users object of interface type User
    const [users, setUsers] = useState<User[]>([]);
    const navigate = useNavigate();
    console.log(users)

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

    const handleClick = (user:User) => {
        navigate("/individual-page", { state: user });
    }

    return (
    <div className="roster-container">
        <h2>Kilo Roster</h2>
        <table className="roster-table">
            <thead>
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Is Admin</th>
                    <th>Kilo Access</th>
                </tr>
            </thead>
            <tbody>
            {users.map((user) => (
                <tr key={user.id} className="roster-row" onClick={() => handleClick(user)}>
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
