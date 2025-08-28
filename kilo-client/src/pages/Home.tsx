import "./styles/Home.css"
import Header from "../components/Header";
import Footer from "../components/Footer";
import KiloRoster from "../components/KiloRoster";

function Home() {
    return(
        <div className="Home">
            <Header />
            <div className="components">
                <KiloRoster />
            </div>
            <Footer />
        </div>
    );
}

export default Home;