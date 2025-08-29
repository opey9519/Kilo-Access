import "./styles/CreateUserPage.css"
import Header from "../components/Header";
import Footer from "../components/Footer";
import CreateUser from "../components/CreateUser";

function CreateUserPage() {
    return(
        <div className="CreateUserPage">
            <Header />
            <div className="components">
                <CreateUser />
            </div>
            <Footer />
        </div>
    );
}

export default CreateUserPage