# Water Monitoring System - Backend

This repository contains the backend implementation for the Water Monitoring System, which monitors water and atmospheric conditions using IoT sensors and provides predictive analytics using machine learning.

## Features
- Real-time data collection and storage
- Threshold-based alert system
- Historical data analysis
- Integration with machine learning models for predictions

## Technologies Used
- Python (Flask)
- SQLite
- SQLAlchemy
- Flask-Migrate
- IoT Integration

## Endpoints
| Method | Endpoint           | Description                         |
|--------|--------------------|-------------------------------------|
| GET    | `/api/data`        | Fetch sensor data                  |
| POST   | `/api/alerts`      | Create an alert                    |
| GET    | `/api/history`     | Retrieve historical data           |
| POST   | `/api/inject`      | Inject test data (for debugging)   |

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone -b backend https://github.com/Fredrick-owino/water_monitoring.git
