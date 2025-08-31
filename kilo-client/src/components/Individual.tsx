import "./styles/Individual.css"
import type { User } from "../api/utility/interface";
import { useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { get_user } from "../api/user";
import { getToken } from "../api/utility/utility";
import { edit_athlete } from "../api/admin/athlete";
import { edit_officer } from "../api/admin/officer";

function Individual() {
    const location = useLocation();
    const user = location.state as User;

    const [qrCode, setQrCode] = useState<string>("");
    const [firstName, setFirstName] = useState(user.first_name)
    const [lastName, setLastName] = useState(user.last_name)
    const [isEditing, setIsEditing] = useState(false);
    const [hasKiloAccess, setHasKiloAccess] = useState(user.kilo_access);

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


    const onEditClick = () => {
        setIsEditing(!isEditing);
    }

    const token = getToken() || ""; // fallback to empty string if null

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!token) {
        console.error("No token available!");
        return;
        }

        if (user.is_admin) {
            await edit_officer(user.id, token, firstName, lastName, hasKiloAccess);
        } else {
            await edit_athlete(user.id, token, firstName, lastName, hasKiloAccess);
        }


    };


    return (
        <div className="individual-container-wrapper">
            <div className="individual-container">
                <img
                    onClick={onEditClick}
                    id="editPencil"
                    src="/images/icons8-edit-pencil-50.png"
                    alt="Edit"
                />

                {isEditing ? 
                    <>
                        <div className="individual-container-top">
                            <form onSubmit={handleSubmit} action="">
                                <div className="editing-names">
                                    <div className="editing-name">
                                        <label id="editing-first-name" htmlFor="">First Name</label>    
                                        <input type="text" value={firstName} onChange={(e) => setFirstName(e.target.value)}/>    
                                    </div>


                                    <div className="editing-name">
                                        <label id="editing-last-name" htmlFor="">Last Name</label>
                                        <input type="text" value={lastName} onChange={(e) => setLastName(e.target.value)}/>    
                                    </div>
                                </div>

                                <div>

                                    <fieldset>
                                        <legend>Kilo Access:</legend>
                                        <label className="kilo-access">
                                            <input
                                            type="radio"
                                            checked={hasKiloAccess === true}
                                            onChange={() => setHasKiloAccess(true)}
                                            />
                                            Yes
                                        </label>
                                        <label className="kilo-access">
                                            <input
                                            type="radio"
                                            checked={hasKiloAccess === false}
                                            onChange={() => setHasKiloAccess(false)}
                                            />
                                            No
                                        </label>
                                    </fieldset>
                                </div>

                                <button className="editing-button" type="submit">Edit User</button>
                            </form>
                        </div>
                    </>
                :
                    <>
                        <div className="individual-container-top">
                            <h2>{user.first_name} {user.last_name}</h2>
                        </div>

                        <p>Is Admin: {user.is_admin ? "✅" : "❌"}</p>
                        <p>Has Kilo Access: {user.kilo_access ? "✅" : "❌"}</p>
                        {qrCode && <img src={qrCode} alt="QR Code" className="qr-code" />}    
                    </>
                }
                
                
            </div>
        </div>
    );
}

export default Individual;
