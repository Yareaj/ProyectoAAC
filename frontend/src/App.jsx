import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./pages/LandingPage";
import SumVisualizer from "./pages/SumVisualizer";
import RestVisualizer from "./pages/SubVisualizer";
import MultiplicationVisualizer from "./pages/MultiplicacionVisualizer";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/suma" element={<SumVisualizer />} />
        <Route path="/resta" element={<RestVisualizer />} />
        <Route path="/multiplicacion" element={<MultiplicationVisualizer />} />
      </Routes>
    </Router>
  );
}

export default App;
