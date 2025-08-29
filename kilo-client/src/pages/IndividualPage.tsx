import "./styles/IndividualPage.css"
import Header from "../components/Header";
import Footer from "../components/Footer";
import Individual from "../components/Individual";

function IndividualPage() {
    return(
        <div className="IndividualPage">
            <Header />
            <div className="components">
                <Individual />
            </div>
            <Footer />
        </div>
    );
}

export default IndividualPage;