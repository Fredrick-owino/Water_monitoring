import React from 'react';
import './Services.css';

const Services = () => {
  return (
    <div className="services-container">
      <h2>Our Services</h2>
      <div className="services-grid">
        <div className="service-item">
          <img src="/assets/iot7.jpeg" alt="IoT Monitoring" />
          <h3>IoT Monitoring</h3>
          <p>Real-time data collection using IoT sensors to monitor water quality and weather conditions.</p>
        </div>
        <div className="service-item">
          <img src="/assets/iot8.jpeg" alt="Machine Learning" />
          <h3>Machine Learning Analysis</h3>
          <p>Predictive analytics powered by machine learning models trained with local data.</p>
        </div>
        <div className="service-item">
          <img src="/assets/iot10.jpeg" alt="Data Visualization" />
          <h3>Data Visualization</h3>
          <p>Graphical dashboards for visualizing water quality and meteorological data in real-time.</p>
        </div>
      </div>
    </div>
  );
};

export default Services;
