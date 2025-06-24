import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import SumVisualizer from "./components/SumVisualizer"

function App() {
  return (
    <div className="min-h-screen bg-gray-100 text-gray-800 flex items-center justify-center">
      <SumVisualizer />
    </div>
  )
}

export default App

