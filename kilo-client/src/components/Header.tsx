import './styles/Header.css'
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
// import AuthContext from '../AuthContext';
// import { getToken } from '../api/utility/utility';
// import { signout } from '../api/auth';
// import { useContext } from 'react';
// import { useNavigate } from 'react-router-dom';

function Header() {
    // Temporary User
    const user = true

    // const {user, logout} = useContext(AuthContext);

    // const navigate = useNavigate();

    // Sends sign out request to backend, if good, logs out through context
    const handleLogout = async (e: React.MouseEvent<HTMLButtonElement, MouseEvent>) => {
        e.preventDefault();
        // console.log("Attempted logout")

        // const token = getToken();
        // const result = await signout(token);

        // if (result.status === 200) {
        //     logout();
        //     navigate('/') // Send home on successful login
        // }
    }

    // console.log(user)
    return (
        <Navbar bg='dark' variant='dark' sticky="top" expand="lg" className="navbar">
            <Container>
                <Navbar.Brand href="/">Kilo Access</Navbar.Brand>
                <Navbar.Toggle aria-controls="basic-navbar-nav" />
                <Navbar.Collapse id="basic-navbar-nav">
                <Nav className="links me-auto">
                    {user ?
                        <Nav.Link href='create'>Create</Nav.Link>
                    :
                        <></>
                    }

                    {user ? 
                        <Nav.Link onClick={handleLogout}>Logout</Nav.Link>
                    :
                        <Nav.Link href="login">Admin Login</Nav.Link>
                    }
                </Nav>
                </Navbar.Collapse>
            </Container>
    </Navbar>
    );
}

export default Header;