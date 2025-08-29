import "./styles/Individual.css"
import type { User } from "../api/utility/interface";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { get_user } from "../api/user";

function Individual() {
    const location = useLocation();
    const user = location.state as User;

    const [qrCode, setQrCode] = useState<string>("");

    useEffect(() => {
        async function fetchUser(user_id: number) {
            const result = await get_user(user_id);

            if ("qr_code" in result) {
                setQrCode(result.qr_code);
            } else {
                console.error(result.message);
            }
        }

        fetchUser(user.id);
    }, [user.id]);

    return (
        <div className="individual-container-wrapper">
            <div className="individual-container">
                <h2>{user.first_name} {user.last_name}</h2>
                <p>Is Admin: {user.is_admin ? "✅" : "❌"}</p>
                <p>Has Kilo Access: {user.kilo_access ? "✅" : "❌"}</p>
                {qrCode && <img src={qrCode} alt="QR Code" className="qr-code" />}
            </div>
    </div>
    );
     
}

export default Individual;
