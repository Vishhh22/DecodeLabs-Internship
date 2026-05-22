# DecodeLabs Internship - Sensor Data Collection Simulator

## 🎯 Project Overview

This project simulates real-world sensor data collection, including temperature, humidity, and motion detection. The simulator generates realistic sensor readings, displays them in real-time, and logs data for analysis.

## ✨ Features

- **🌡️ Temperature Sensor**: Simulates realistic temperature fluctuations (15-35°C)
- **💧 Humidity Sensor**: Tracks humidity levels with natural variation (20-95%)
- **🚨 Motion Sensor**: Detects motion events with configurable probability
- **📊 Real-time Display**: Shows sensor readings as they're collected
- **💾 Data Logging**: Saves data in both JSON and CSV formats
- **📈 Statistics**: Calculates min, max, and average values for each sensor

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- No additional dependencies required (uses only Python standard library)

### Installation

```bash
# Clone or navigate to the repository
cd DecodeLabs-Internship

# Verify Python installation
python --version
```

### Running the Simulator

```bash
# Run with default settings (30 seconds, 2-second intervals)
python sensor_simulator.py

# For custom duration and intervals, modify the main() function
```

## 📋 Project Structure

```
DecodeLabs-Internship/
├── sensor_simulator.py      # Main simulator code
├── README.md                # This file
├── requirements.txt         # Python dependencies (empty - uses stdlib only)
├── sensor_data.json         # Generated JSON log file
└── sensor_data.csv          # Generated CSV log file
```

## 🔧 How It Works

### Sensor Classes

#### 1. **TemperatureSensor**
- Generates temperature readings in Celsius
- Simulates realistic drift with ±0.5°C variation per cycle
- Maintains value within 15-35°C range

```python
temp_sensor = TemperatureSensor(sensor_id="TEMP_001")
reading = temp_sensor.read()  # Returns SensorReading object
```

#### 2. **HumiditySensor**
- Generates humidity readings as percentages
- Smaller variation (±2%) to simulate slower change rate
- Maintains value within 20-95% range

```python
humidity_sensor = HumiditySensor(sensor_id="HUM_001")
reading = humidity_sensor.read()
```

#### 3. **MotionSensor**
- Detects motion state (binary: 0 or 1)
- Configurable detection probability (default: 30%)
- Useful for alarm systems or activity tracking

```python
motion_sensor = MotionSensor(sensor_id="MOTION_001")
reading = motion_sensor.read()  # Returns 0.0 or 1.0
```

### Data Storage

All readings are automatically saved in two formats:

**JSON Format** (`sensor_data.json`):
```json
[
  {
    "sensor_type": "temperature",
    "value": 22.45,
    "unit": "°C",
    "timestamp": "2026-05-22T10:30:45.123456",
    "sensor_id": "TEMP_001"
  },
  ...
]
```

**CSV Format** (`sensor_data.csv`):
```csv
sensor_type,value,unit,timestamp,sensor_id
temperature,22.45,°C,2026-05-22T10:30:45.123456,TEMP_001
```

## 📊 Example Output

```
============================================================
🔬 SENSOR DATA SIMULATOR STARTED
============================================================
Duration: 30s | Interval: 2.0s
============================================================

[10:30:45] Sensor Readings:
--------------------------------------------------
  🌡️  TEMP_001         22.34 °C
  💧 HUM_001          52.16 %
  🚨 MOTION_001            0.00 state

[10:30:47] Sensor Readings:
--------------------------------------------------
  🌡️  TEMP_001         22.89 °C
  💧 HUM_001          50.45 %
  🚨 MOTION_001            1.00 state

============================================================
📊 SIMULATION SUMMARY
============================================================
Total Readings Collected: 15
Total Data Points: 45
Sensors Active: 3 (Temperature, Humidity, Motion)
============================================================

============================================================
📈 SENSOR STATISTICS
============================================================
Temperature (°C):
  Min: 21.50°C | Max: 23.85°C | Avg: 22.67°C
Humidity (%):
  Min: 48.20% | Max: 54.30% | Avg: 51.23%
Motion Detection:
  Detections: 4 / 15 readings
============================================================
```

## 🎓 Key Learning Concepts

### 1. **Data Handling**
- Working with data classes and structured data
- Converting between different data formats (JSON, CSV)
- Time-based data collection and management

### 2. **Sensor Concepts**
- Understanding sensor simulation vs. real hardware
- Implementing realistic sensor behavior with drift and variation
- Handling different sensor types and their characteristics

### 3. **Software Design Patterns**
- **Object-Oriented Programming**: Separate classes for each sensor type
- **Data Class Usage**: Structured sensor reading representation
- **Logger Pattern**: Centralized data storage and retrieval
- **Enum Pattern**: Type-safe sensor type definition

### 4. **Real-time Data Processing**
- Continuous data collection in intervals
- Real-time display of readings
- Graceful handling of interrupts (Ctrl+C)

## 🔄 Extending the Project

### Add a New Sensor Type

```python
class PressureSensor:
    """Simulates a pressure sensor"""
    
    def __init__(self, sensor_id: str = "PRES_001"):
        self.sensor_id = sensor_id
        self.current_pressure = 1013.25  # hPa
        
    def read(self) -> SensorReading:
        drift = random.uniform(-1.0, 1.0)
        self.current_pressure += drift
        self.current_pressure = max(950.0, min(1050.0, self.current_pressure))
        
        return SensorReading(
            sensor_type="pressure",
            value=round(self.current_pressure, 2),
            unit="hPa",
            timestamp=datetime.datetime.now().isoformat(),
            sensor_id=self.sensor_id
        )

# Add to SensorSimulator.__init__():
# self.pressure_sensor = PressureSensor()
```

### Modify Sensor Behavior

```python
# Create a more sensitive temperature sensor
temp_sensor = TemperatureSensor()

# Adjust drift in the read() method:
# Change drift = random.uniform(-0.5, 0.5)
# To: drift = random.uniform(-0.1, 0.1)  # More stable
# Or: drift = random.uniform(-2.0, 2.0)  # More volatile
```

### Change Collection Parameters

```python
# In main() function:
simulator.run_simulation(
    duration_seconds=60,  # 60 seconds instead of 30
    interval=1.0          # Collect every 1 second instead of 2
)
```

## 📁 Output Files

After running the simulator, you'll find:

- **`sensor_data.json`**: Complete sensor data in JSON format
- **`sensor_data.csv`**: Complete sensor data in CSV format

These files can be imported into data analysis tools like:
- Excel/Google Sheets
- Python Pandas
- Jupyter Notebooks
- Database systems

## 🐛 Troubleshooting

### Import Errors
```bash
# Ensure you're in the correct directory
cd DecodeLabs-Internship

# Verify Python version
python --version  # Should be 3.7 or higher
```

### File Not Found Errors
- Ensure the script is run from the project directory
- Check that you have write permissions for output files

### No Data Generated
- Verify the simulation is running for sufficient duration
- Check the interval isn't too long
- Look for error messages in the console

## 📚 Resources

- [Python Data Classes](https://docs.python.org/3/library/dataclasses.html)
- [Python datetime Module](https://docs.python.org/3/library/datetime.html)
- [Python JSON Module](https://docs.python.org/3/library/json.html)
- [Sensor Simulation Best Practices](https://en.wikipedia.org/wiki/Sensor_data_fusion)

## 🎯 Skills Demonstrated

✅ Object-Oriented Programming
✅ Data Handling & Serialization
✅ File I/O Operations
✅ Real-time Data Collection
✅ Statistical Analysis
✅ CSV/JSON Data Formats
✅ Error Handling & Logging
✅ Simulation & Modeling

## 📝 License

This project is part of the DecodeLabs Internship program.

## 👤 Author

Developed as part of DecodeLabs Internship - Sensor Data Collection Track

---

**Happy Simulating! 🚀**
