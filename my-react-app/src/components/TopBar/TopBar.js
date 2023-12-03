import React from 'react';
import './TopBar.css';
import WelcomeBanner from './WelcomeBanner';
import SearchBar from './SearchBar';

function TopBar() {
  return (
    <div className="top-bar">
      <WelcomeBanner />
      <SearchBar />
    </div>
  );
}

export default TopBar;
