import "./styles/KiloRoster.css"
import type { User } from "../api/utility/interface";
import Loading from "./Loading";
import { get_users } from "../api/user";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function KiloRoster() {
    // Users object of interface type User
    const [users, setUsers] = useState<User[]>([]);
    const [searchTerm, setSearchTerm] = useState("");
    const [loading, setLoading] = useState(true);
    const navigate = useNavigate();

    //  Fetch users
    useEffect(() => {
        async function fetchUsers() {
            const result = await get_users();

            if ("users" in result) {
                setUsers(result.users);
            } else {
                console.error(result.message);
            }
            setLoading(false);
        }

        fetchUsers();
    }, []);

    // Goes to individual User page, passing user as a prop
    const handleClick = (user:User) => {
        navigate("/individual-page", { state: user });
    }

    // Filter users by search term 
    const filteredUsers = users.filter((u) => {
        const fullName = `${u.first_name} ${u.last_name}`.toLowerCase();
        return fullName.includes(searchTerm.toLowerCase());
    });

    return (
        <div className="roster-container">
            <h2>Kilo Roster</h2>

            {/* 🔎 Search bar */}
            <input 
                type="text" 
                placeholder="Search by name..."
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                className="search-bar"
            />

            <table className="roster-table">
                <thead>
                    <tr>
                        <th>First Name</th>
                        <th>Last Name</th>
                        {/* <th>Is Admin</th> */}
                        <th>Kilo Access</th>
                    </tr>
                </thead>
                <tbody>
                    {loading ? (
                        <tr>
                            <td colSpan={4}><Loading /></td>
                        </tr>
                    ) : (
                        filteredUsers.length > 0 ? (
                            filteredUsers.map((user) => (
                                <tr 
                                    key={user._uuid} 
                                    className="roster-row" 
                                    onClick={() => handleClick(user)}
                                >
                                    <td>{user.first_name}</td>
                                    <td>{user.last_name}</td>
                                    {/* <td>{user.is_admin ? "✅" : "❌"}</td> */}
                                    <td>{user.kilo_access ? "✅" : "❌"}</td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan={4}>No users found</td>
                            </tr>
                        )
                    )}
                </tbody>
            </table>
        </div>
    );
}

export default KiloRoster;
