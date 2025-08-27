import {Routes, Route} from "react-router-dom"
import './App.css'
import LoginPage from "./pages/LoginPage"
import Home from "./pages/Home"

function App() {

  return (
    <div className="app-container">
      <Routes>
        <Route path="/" element={<Home/>}/>
        <Route path="/login" element={<LoginPage/>}/>
      </Routes>
    </div>
  )
}

export default App
