import "./styles/Individual.css"
import Loading from "./Loading";
import type { User } from "../api/utility/interface";
import { useEffect, useState, useContext } from "react";
import { useLocation, useNavigate } from "react-router-dom";
import { get_user } from "../api/user";
import { getToken } from "../api/utility/utility";
import { edit_athlete, delete_athlete } from "../api/admin/athlete";
import { edit_officer, delete_officer } from "../api/admin/officer";
import { AuthContext } from "../AuthContext";

function Individual() {
    const auth = useContext(AuthContext);
    if (!auth) return;
    
    const {user} = auth;

    // Current athlete/officer viewed
    const location = useLocation();
    const navigate = useNavigate();
    const userDisplayed = location.state as User;

    // Editing 
    const [qrCode, setQrCode] = useState<string>("");
    const [firstName, setFirstName] = useState(userDisplayed.first_name)
    const [lastName, setLastName] = useState(userDisplayed.last_name)
    const [isEditing, setIsEditing] = useState(false);
    const [hasKiloAccess, setHasKiloAccess] = useState(userDisplayed.kilo_access);
    const [loading, setLoading] = useState(true);

    // Load QR code 
    useEffect(() => {
        async function fetchUser(user_id: number) {
            const result = await get_user(user_id);

            if ("qr_code" in result) {
                setQrCode(result.qr_code);
            } else {
                console.error(result.message);
            }
            setLoading(false);
        }

        fetchUser(userDisplayed.id);
    }, [userDisplayed.id]);

    // Editing User?
    const onEditClick = () => {
        setIsEditing(!isEditing);
    }

    // Deleting User?
    const onDeleteClick = async () => {
        if (!token) {
            console.error("No token available!");
            return;
        }

        if (userDisplayed.is_admin) {
            await delete_officer(userDisplayed.id, token);
            navigate('/')
        } else {
            await delete_athlete(userDisplayed.id, token);
            navigate('/')
        }
    }

    const token = getToken() || ""; // fallback to empty string if null

    const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        if (!token) {
        console.error("No token available!");
        return;
        }


        if (userDisplayed.is_admin) {
            await edit_officer(userDisplayed.id, token, firstName, lastName, hasKiloAccess);
            setIsEditing(!isEditing)
        } else {
            await edit_athlete(userDisplayed.id, token, firstName, lastName, hasKiloAccess);
            setIsEditing(!isEditing)
        }
    };


    return (
        <div className="individual-container-wrapper">
            <div className="individual-container">
                {
                    user.isAuthenticated ?
                    <>
                        <img
                            onClick={onEditClick}
                            className="adminButton"
                            src="/images/icons8-edit-pencil-50.png"
                            alt="Edit"
                        />

                        <img
                            onClick={onDeleteClick}
                            className="adminButton"
                            id="trashButton"
                            src="/images/trashbin.png"
                            alt="Delete" 
                        />
                    </>
                    :
                    <></>
                }
                

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
                            <h2>{userDisplayed.first_name} {userDisplayed.last_name}</h2>
                        </div>

                        <p>Is Admin: {userDisplayed.is_admin ? "✅" : "❌"}</p>
                        <p>Has Kilo Access: {userDisplayed.kilo_access ? "✅" : "❌"}</p>

                        {loading ? 
                            <>
                                <Loading />
                            </>
                            :
                            <>
                                {qrCode && <img src={qrCode} alt="QR Code" className="qr-code" />}    
                            </>
                        }
                        

                    </>
                }
                
                
            </div>
        </div>
    );
}

export default Individual;
