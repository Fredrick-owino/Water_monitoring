import React from 'react';
import './Home.css';

const Home = () => {
  return (
    <div className="home-container">
      <h2>Welcome To The Lake Victoria Water Quality Monitoring System</h2>
      <p>This platform helps monitor water quality and meteorological data in real-time.</p>
      <div className="image-container">
        <img src="/assets/lake.jpg" alt="Lake Victoria" />
      </div>
    </div>
  );
};

export default Home;
