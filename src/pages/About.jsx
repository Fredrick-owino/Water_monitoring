
import React from 'react';
import './About.css';

const About = () => {
  return (
    <div className="about-container">
      <h2>About Us</h2>
      <p>We are dedicated to preventing fish kills and improving aquaculture using IoT and machine learning technologies.</p>
      <div className="image-container">
        <img src="/assets/iot9.jpeg" alt="Our Team" />
      </div>
    </div>
  );
};

export default About;
