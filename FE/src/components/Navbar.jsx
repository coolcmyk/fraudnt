import React, { useState } from 'react';
import styled from 'styled-components';

const NavbarContainer = styled.nav`
  width: 100%;
  background: linear-gradient(45deg, #6a11cb, #2575fc);
  padding: 20px 40px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.2);
  position: sticky;
  top: 0;
  z-index: 1000;
`;

const Logo = styled.div`
  font-size: 2.5rem;
  font-family: 'Poppins', sans-serif;
  color: white;
  font-weight: bold;
  text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.5);
`;

const NavLinks = styled.div`
  display: flex;
  gap: 30px;

  @media (max-width: 768px) {
    gap: 10px;
  }
`;

const NavLink = styled.a`
  font-family: 'Poppins', sans-serif;
  font-size: 1.25rem;
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;

  &:hover {
    color: #e0e0e0;
  }

  @media (max-width: 768px) {
    font-size: 1rem;
  }
`;

const DropdownContainer = styled.div`
  position: relative;
  display: inline-block;
`;

const DropdownButton = styled.div`
  font-family: 'Poppins', sans-serif;
  font-size: 1.25rem;
  color: white;
  cursor: pointer;
  display: flex;
  align-items: center;

  &:hover {
    color: #e0e0e0;
  }
`;

const DropdownContent = styled.div`
  display: ${({ show }) => (show ? 'block' : 'none')};
  position: absolute;
  background-color: #2d2d2d;
  min-width: 160px;
  box-shadow: 0px 8px 16px rgba(0, 0, 0, 0.2);
  z-index: 1;
  border-radius: 8px;
  margin-top: 10px;
`;

const DropdownItem = styled.a`
  color: white;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
  transition: background-color 0.3s ease;

  &:hover {
    background-color: #575757;
  }
`;

const Navbar = () => {
  const [dropdownOpen, setDropdownOpen] = useState(false);

  const toggleDropdown = () => {
    setDropdownOpen(!dropdownOpen);
  };

  return (
    <NavbarContainer>
      <Logo>FRAUDN'T</Logo>
      <NavLinks>
        <NavLink href="#interactions">Interactions</NavLink>
        <NavLink href="#compiler">Compiler</NavLink>
        <NavLink href="#history">History</NavLink>
        <NavLink href="#submit">Submit</NavLink>
        <DropdownContainer>
          <DropdownButton onClick={toggleDropdown}>
            Account ▼
          </DropdownButton>
          <DropdownContent show={dropdownOpen}>
            <DropdownItem href="#home">Home</DropdownItem>
            <DropdownItem href="#settings">Settings</DropdownItem>
            <DropdownItem href="#logout">Log out</DropdownItem>
          </DropdownContent>
        </DropdownContainer>
      </NavLinks>
    </NavbarContainer>
  );
};

export default Navbar;



