import {Routes, Route} from "react-router-dom"
import './App.css'
import LoginPage from "./pages/LoginPage"
import Home from "./pages/Home"
import IndividualPage from "./pages/IndividualPage"

function App() {

  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<LoginPage/>}/>
        <Route path="/individual-page" element={<IndividualPage/>}/>
      </Routes>
    </div>
  )
}

export default App
