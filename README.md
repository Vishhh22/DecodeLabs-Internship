# 🔬 DecodeLabs Internship - Project 1: Sensor Data Simulator

## Project Overview

A comprehensive **pure Python** IoT sensor data simulator that collects, processes, and logs real-time sensor data. This project demonstrates core IoT concepts, data handling, and sensor simulation techniques.

**Language**: 100% Python 3.7+
**Dependencies**: None (Python standard library only)

## 📊 Features

### Sensor Simulation
- 🌡️ **Temperature Sensor**: Realistic fluctuations (15-35°C) with natural drift
- 💧 **Humidity Sensor**: Gradual changes (20-95%) with ±2% variation
- 🚨 **Motion Sensor**: Binary detection with configurable probability (30% default)

### Data Management
- Real-time data collection with configurable intervals
- JSON export for data analysis
- CSV export for spreadsheet compatibility
- In-memory data storage with full access

### Analysis & Monitoring
- Real-time console display of sensor readings
- Alert system with threshold-based notifications
- Comprehensive statistics (Min, Max, Average, Range)
- Detection rate calculation for motion sensor

### Architecture
- Object-oriented design with base sensor class
- Extensible architecture for adding new sensors
- Clean separation of concerns
- Dataclass usage for structured data

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.7 or higher
```

### Installation

```bash
# Clone the repository
git clone https://github.com/Vishhh22/DecodeLabs-Internship.git
cd DecodeLabs-Internship

# No additional dependencies needed!
```

### Basic Usage

```bash
# Run with default settings (30 seconds, 2-second intervals)
python sensor_simulator.py

# Custom duration and interval
python sensor_simulator.py 60 1          # 60 seconds, 1-second interval

# Don't save data
python sensor_simulator.py 30 2 --no-save

# Export only JSON
python sensor_simulator.py 30 2 --format json
```

## 📋 Command Line Options

```
Usage: python sensor_simulator.py [duration] [interval] [options]

Positional Arguments:
  duration          Simulation duration in seconds (default: 30)
  interval          Time between readings in seconds (default: 2.0)

Optional Arguments:
  --no-save         Do not save data to files
  --format {json,csv,both}
                    Export format (default: both)
  -h, --help        Show this help message
```

## 🎯 Usage Examples

### Example 1: Quick Test
```bash
python sensor_simulator.py 10 1
```
- Runs for 10 seconds
- Collects data every 1 second
- Generates 30 data points (3 sensors × 10 readings)

### Example 2: Extended Monitoring
```bash
python sensor_simulator.py 300 5
```
- Runs for 5 minutes
- Collects data every 5 seconds
- Generates 300 data points
- Good for trend analysis

### Example 3: Quick Check (No Save)
```bash
python sensor_simulator.py 20 2 --no-save
```
- Preview data without file storage
- Useful for testing

## 💻 Python API

### Basic Usage

```python
from sensor_simulator import SensorSimulator

# Create simulator
simulator = SensorSimulator()

# Run simulation
simulator.run_simulation(duration_seconds=60, interval=2.0)

# Get statistics
stats = simulator.get_statistics()

# Export data
simulator.export_data(format='both')
```

### Advanced Usage

```python
from sensor_simulator import (
    SensorSimulator,
    TemperatureSensor,
    HumiditySensor,
    MotionSensor
)

# Create custom simulator with different sensor IDs
simulator = SensorSimulator(
    temp_id="ROOM_TEMP",
    humid_id="ROOM_HUMIDITY",
    motion_id="DOOR_MOTION"
)

# Collect individual readings
readings = simulator.collect_reading()
for reading in readings:
    print(reading)  # Uses __str__ method

# Access logger data
temp_readings = simulator.logger.get_data_by_type('temperature')
print(f"Temperature readings: {len(temp_readings)}")

# Get alerts
alerts = simulator.get_alerts()
print(f"Alerts: {len(alerts)}")
```

### Custom Sensor Implementation

```python
from sensor_simulator import BaseSensor, SensorReading, SensorType
import datetime

class PressureSensor(BaseSensor):
    """Custom pressure sensor"""
    
    def __init__(self, sensor_id="PRES_001", initial_pressure=1013.25):
        super().__init__(sensor_id, min_val=950.0, max_val=1050.0, initial_val=initial_pressure)
        self.sensor_type = "pressure"
    
    def read(self) -> SensorReading:
        drift = random.uniform(-1.0, 1.0)
        self.current_value = self._constrain_value(self.current_value + drift)
        
        return SensorReading(
            sensor_type=self.sensor_type,
            value=round(self.current_value, 2),
            unit="hPa",
            timestamp=datetime.datetime.now().isoformat(),
            sensor_id=self.sensor_id
        )
```

## 📊 Output Files

### sensor_data.json
```json
[
  {
    "sensor_type": "temperature",
    "value": 22.34,
    "unit": "°C",
    "timestamp": "2026-05-22T10:30:45.123456",
    "sensor_id": "TEMP_001"
  },
  {
    "sensor_type": "humidity",
    "value": 52.16,
    "unit": "%",
    "timestamp": "2026-05-22T10:30:45.234567",
    "sensor_id": "HUM_001"
  }
]
```

### sensor_data.csv
```csv
sensor_type,value,unit,timestamp,sensor_id
temperature,22.34,°C,2026-05-22T10:30:45.123456,TEMP_001
humidity,52.16,%,2026-05-22T10:30:45.234567,HUM_001
motion,0.0,state,2026-05-22T10:30:45.345678,MOTION_001
```

## 📈 Console Output Example

```
================================================================================
🔬 SENSOR DATA SIMULATOR
================================================================================
Duration: 30s | Interval: 2.0s
Sensors: Temperature, Humidity, Motion
================================================================================

[10:30:45] 📊 Sensor Readings:
--------------------------------------------------------------------------------
  🌡️  TEMP_001             22.34 °C   | 🟢 Normal
  💧  HUM_001              52.16 %    | 🟢 Normal
  🚨  MOTION_001           0.00 state | 🟢 No Motion

[10:30:47] 📊 Sensor Readings:
--------------------------------------------------------------------------------
  🌡️  TEMP_001             22.89 °C   | 🟢 Normal
  💧  HUM_001              50.45 %    | 🟢 Normal
  🚨  MOTION_001           1.00 state | 🚨 MOTION DETECTED!

================================================================================
📊 SIMULATION SUMMARY
================================================================================
Readings Collected: 2
Total Data Points: 6
Duration: 2.1s
Alerts Triggered: 1
================================================================================

================================================================================
📈 SENSOR STATISTICS
================================================================================

🌡️  Temperature (°C):
    Readings: 2
    Min:  22.34°C
    Max:  22.89°C
    Avg:  22.62°C
    Range: 0.55°C

💧 Humidity (%):
    Readings: 2
    Min:  50.45%
    Max:  52.16%
    Avg:  51.31%
    Range: 1.71%

🚨 Motion Detection:
    Readings: 2
    Detections: 1
    Detection Rate: 50.0%
================================================================================
```

## 🎓 Skills Demonstrated

✅ **Object-Oriented Programming**
- Class inheritance and polymorphism
- Base class design patterns
- Dataclass usage

✅ **Data Handling**
- JSON serialization/deserialization
- CSV file I/O
- Data aggregation and filtering

✅ **Sensor Concepts**
- Realistic sensor simulation
- Drift and noise modeling
- Range constraints
- Threshold-based alerts

✅ **Python Best Practices**
- Type hints throughout
- Comprehensive docstrings
- Command-line argument parsing
- Error handling
- Enum usage for type safety

✅ **Statistical Analysis**
- Min/Max/Average calculations
- Rate calculations
- Data normalization

## 📁 Project Structure

```
DecodeLabs-Internship/
├── sensor_simulator.py       # Main simulator (100% Python)
├── README.md                 # This file
├── requirements.txt          # No external dependencies
└── sensor_data.*            # Generated output files (JSON/CSV)
```

## 🔧 Sensor Configuration

### Temperature Sensor
- **Range**: 15-35°C
- **Drift**: ±1°C per reading
- **Pattern**: Random walk with constraints
- **Use Case**: Room temperature monitoring

### Humidity Sensor
- **Range**: 20-95%
- **Drift**: ±2% per reading
- **Pattern**: Smooth gradual changes
- **Use Case**: Environmental monitoring

### Motion Sensor
- **Type**: Binary (0/1)
- **Probability**: 30% (configurable)
- **Response**: Immediate state change
- **Use Case**: Security/occupancy detection

## ⚠️ Alert Thresholds

### Temperature
- 🟢 Normal: 16-28°C
- 🟡 Warning: <16°C or >28°C
- 🔴 Critical: <15°C or >30°C

### Humidity
- 🟢 Normal: 30-80%
- 🟡 Warning: <30% or >80%
- 🔴 Critical: <25% or >85%

### Motion
- 🟢 Normal: No motion (0)
- 🚨 Alert: Motion detected (1)

## 🔄 Extending the Project

### Add a New Sensor

```python
class LightSensor(BaseSensor):
    def __init__(self, sensor_id="LIGHT_001"):
        super().__init__(sensor_id, 0, 100, 50)
        self.sensor_type = "light"
    
    def read(self) -> SensorReading:
        # Your implementation
        pass
```

### Modify Simulation Parameters

```python
# Adjust drift range
sensor.drift_range = 0.1  # Smaller drift = more stable

# Change alert thresholds
# Modify _get_status() method in SensorSimulator
```

## 📊 Data Analysis Examples

```python
# Load and analyze saved data
import json

with open('sensor_data.json') as f:
    data = json.load(f)

# Get only temperature readings
temp_data = [r['value'] for r in data if r['sensor_type'] == 'temperature']

# Calculate statistics
print(f"Temperature range: {min(temp_data):.2f} - {max(temp_data):.2f}°C")
print(f"Average: {sum(temp_data)/len(temp_data):.2f}°C")
```

## 🚀 Future Enhancements

- [ ] Database integration (SQLite, PostgreSQL)
- [ ] Real-time WebSocket support
- [ ] Advanced anomaly detection
- [ ] Machine learning predictions
- [ ] Multi-location sensor networks
- [ ] MQTT publisher/subscriber
- [ ] Cloud data sync (AWS, GCP)
- [ ] Real hardware sensor integration
- [ ] Data visualization dashboards

## 📚 Resources

- [Python dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Python Enum](https://docs.python.org/3/library/enum.html)
- [JSON Module](https://docs.python.org/3/library/json.html)
- [CSV Module](https://docs.python.org/3/library/csv.html)
- [IoT Sensor Best Practices](https://en.wikipedia.org/wiki/Internet_of_things)

## 📝 License

MIT License - Part of DecodeLabs Internship Program

## 👤 Author

Created as part of DecodeLabs Internship - IoT Sensor Data Collection Track

---

**Ready to monitor your sensors? Run `python sensor_simulator.py` and start collecting data! 🚀**
