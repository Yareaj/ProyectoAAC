import React, { useState } from "react"
import { Link } from "react-router-dom"

const Layout = ({ children }) => {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen)
  }

  return (
    <div className="bg-gray-900 text-white min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-gray-800 p-4 shadow-md">
        <nav className="container mx-auto flex flex-wrap justify-between items-center">
          {/* Logo & title */}
          <h1 className="text-2xl md:text-3xl font-bold">
            <Link to="/" className="flex items-center space-x-2">
              {/* Optional logo */}
              <span>Aritmética Base-b</span>
            </Link>
          </h1>

          {/* Burger Menu Button */}
          <button
            className="md:hidden text-white focus:outline-none"
            onClick={toggleMenu}
          >
            ☰
          </button>

          {/* Navigation Links */}
          <ul
            className={`${
              isMenuOpen ? "block" : "hidden"
            } w-full md:w-auto md:flex md:space-x-6 mt-4 md:mt-0 text-lg`}
          >
            <li>
              <Link
                to="/suma"
                className="hover:text-blue-400 block md:inline-block py-2 md:py-0"
              >
                Suma
              </Link>
            </li>
            <li>
              <Link
                to="/resta"
                className="hover:text-blue-400 block md:inline-block py-2 md:py-0"
              >
                Resta
              </Link>
            </li>
            <li>
              <Link
                to="/multiplicacion"
                className="hover:text-blue-400 block md:inline-block py-2 md:py-0"
              >
                Multiplicación
              </Link>
            </li>
            <li>
              <Link
                to="/division"
                className="hover:text-blue-400 block md:inline-block py-2 md:py-0"
              >
                División
              </Link>
            </li>
          </ul>
        </nav>
      </header>

      {/* Main content */}
      <main className="flex-grow container mx-auto p-6">{children}</main>

      {/* Footer */}
      <footer className="bg-gray-800 p-4 text-center text-gray-400 text-xs md:text-sm">
        <p>
          Álgebra Abstracta y Computacional | 2025-1 | Universidad Nacional de Colombia
        </p>
      </footer>
    </div>
  )
}

export default Layout
