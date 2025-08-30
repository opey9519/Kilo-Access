import "./styles/LoginPage.css"
import Header from "../components/Header";
import Login from "../components/LoginForm";
import Footer from "../components/Footer";

function LoginPage() {
    return (
        <div className="Login">
            <Header />
            <div className="components">
                <Login />
            </div>
            <Footer />
        </div>
    );
}

export default LoginPage;