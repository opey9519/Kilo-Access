import "./styles/Loading.css"
import Spinner from 'react-bootstrap/Spinner';

function Loading() {
    return (
        <div className="spinner-container">
            <Spinner animation="border" role="status">
                <span className="visually-hidden">Loading featured blog...</span>
            </Spinner>
        </div>
    );
}

export default Loading;