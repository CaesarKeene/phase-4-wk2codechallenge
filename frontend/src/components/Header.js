import React from 'react';
import { Link } from 'react-router-dom';

const Header = () => {
  const navStyle = {
    backgroundColor: '#f2f2f2',
    padding: '10px',
    borderBottom: '1px solid #ccc',
  };

  const ulStyle = {
    listStyleType: 'none',
    margin: 0,
    padding: 0,
    display: 'flex',
    justifyContent: 'space-around',
  };

  const liStyle = {
    margin: 0,
    padding: 0,
  };

  const linkStyle = {
    textDecoration: 'none',
    color: '#333',
    fontWeight: 'bold',
  };

  return (
    <header>
      <nav style={navStyle}>
        <ul style={ulStyle}>
          <li style={liStyle}>
            <Link to="/" style={linkStyle}>Home</Link>
          </li>
          <li style={liStyle}>
            <Link to="/pizzas" style={linkStyle}>Pizzas</Link>
          </li>
          <li style={liStyle}>
            <Link to="/restaurants" style={linkStyle}>Restaurants</Link>
          </li>
          <li style={liStyle}>
            <Link to="/restaurant_pizzas" style={linkStyle}>Restaurant Pizzas</Link>
          </li>
        </ul>
      </nav>
    </header>
  );
};

export default Header;
