import "./styles/LoginForm.css"
import { signin, signout } from "../api/auth";
import { getToken } from "../api/utility/utility";
import { AuthContext } from "../AuthContext";
import { useState, useContext } from "react";
import { useNavigate } from "react-router-dom";


function LoginForm() {
    const auth = useContext(AuthContext)
    if (!auth) return;
    // Deconstruct user object & login/logout functions
    const {user, login, logout} = auth
    console.log(user)

    const navigate = useNavigate();

    // Email and Password credential fields (updated on user input)
    const [password, setPassword] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    

    // Sends sign in request to backend, if good sends data to context function
    const handleLogin = async (e:React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        const result = await signin(firstName, lastName, password);
        console.log(result)

        if ("status" in result && result.status === 200) {
            const {access_token, refresh_token} = result;
            login(access_token, refresh_token);
            navigate('/') // Send home on successful login
        }
    }

    // Sends sign out request to backend, if good, logs out through context
    const handleLogout = async (e:React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        e.preventDefault();

        const token = getToken();
        if (!token) return
        const result = await signout(token);

        if (result.status === 200) {
            logout()
        }
    }


    return (
        <div className="container LoginForm">
            {/* If LoggedIn, show logout; if LoggedOut, show Login Form */}
            {user.isAuthenticated ? (

                <div className="LogoutBox">
                    <h1>
                        You Are Logged In!
                    </h1>
                    <button className="Logout" onClick={handleLogout}>
                        Logout
                    </button>
                </div>

            ) : 

                <form className="Form" action="" method="POST" onSubmit={handleLogin}>
                    <div className="Credentials">

                        <div className="FirstUserBox">
                            <label className="text" htmlFor="">First Name</label>
                            <input className="user" value={firstName} onChange={(e) => setFirstName(e.target.value)} type="text" required />
                        </div>

                        <div className="SecondUserBox">
                            <label className="text" htmlFor="">Last Name</label>
                            <input className="user" value={lastName} onChange={(e) => setLastName(e.target.value)} type="text" required />
                        </div>

                        <div className="PassBox">
                            <label className="text" htmlFor="">Password</label>
                            <input className="Password" value={password} onChange={(e) => setPassword(e.target.value)} type="password" required />
                        </div>

                        {/* <div className="RegisterBox">
                            <p id="RegisterPara">
                                Dont have an account?
                            </p>

                            <Link id="RegisterButton" to="/register">Register</Link>
                        </div> */}

                    </div>

                    <div className="SubmitButton">
                        <button type="submit" className="LoginButton">
                            Login
                        </button>
                    </div>

                </form>}
        </div>
    );
}

export default LoginForm;