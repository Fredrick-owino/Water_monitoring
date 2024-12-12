import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const Visualization = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Simulate fetching data from an API
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/data'); // Replace with your backend endpoint
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2>Real-Time Data Visualization</h2>
      <p>Below are graphs visualizing water quality and meteorological parameters:</p>
      <div style={{ width: '100%', height: 400 }}>
        <ResponsiveContainer>
          <LineChart data={data}>
            <CartesianGrid stroke="#ccc" />
            <XAxis dataKey="timestamp" />
            <YAxis />
            <Tooltip />
            <Line type="monotone" dataKey="temperature" stroke="#ff7300" name="Temperature (°C)" />
            <Line type="monotone" dataKey="dissolvedOxygen" stroke="#387908" name="Dissolved Oxygen (mg/L)" />
          </LineChart>
        </ResponsiveContainer>
      </div>
    </div>
  );
};

export default Visualization;
