# 📊 IoT Dashboard Documentation

## Project Overview

A real-time IoT sensor monitoring dashboard that displays live sensor data with interactive charts, alerts, and data visualization. Built with HTML5, CSS3, Chart.js, and vanilla JavaScript.

## ✨ Key Features

### 🎯 Real-time Monitoring
- **Live Sensor Readings**: Temperature, Humidity, and Motion sensors
- **Auto-updating Data**: Configurable update intervals (1s, 2s, 5s, 10s)
- **Data History**: Track trends with rolling window of up to 100 data points
- **Status Indicators**: Real-time status with visual alerts

### 📊 Data Visualization
- **Line Charts**: Temperature and Humidity trends over time
- **Bar Charts**: Motion detection patterns
- **Doughnut Charts**: Motion detection ratio
- **Mini Charts**: Quick sparkline views on sensor cards
- **Data Tables**: Recent readings with timestamps

### ⚠️ Alert System
- **Temperature Alerts**: High (>28°C), Low (<16°C), Critical (>30°C, <15°C)
- **Humidity Alerts**: High (>80%), Low (<30%), Critical (>85%, <25%)
- **Motion Alerts**: Real-time motion detection notifications
- **Alert History**: Timestamped alert logs

### 📈 Statistics
- **Min/Max/Average**: For each sensor type
- **Detection Rate**: Motion detection percentage
- **Trend Analysis**: Visual pattern recognition

## 🚀 Getting Started

### Quick Start
1. Open `dashboard.html` in any modern web browser
2. Click **"Start"** button to begin data simulation
3. Watch real-time data update and visualize

### Controls
- **Update Interval**: Change update frequency (1s to 10s)
- **Data Points**: Set history size (10 to 100 readings)
- **Start/Stop**: Control simulation
- **Reset**: Clear all data and restart

## 📋 Dashboard Components

### 1. Header Section
- Dashboard title and description
- Live status indicator with pulse animation
- Last update timestamp
- Status color: Green = Live, Red = Paused

### 2. Control Panel
- **Update Interval Selector**: Choose data update frequency
  - 1 second: High frequency updates
  - 2 seconds: Balanced updates (default)
  - 5 seconds: Lower frequency
  - 10 seconds: Very low frequency

- **Data Points Selector**: Control history size
  - 10: Minimal history
  - 20: Default - balanced view
  - 50: Extended history
  - 100: Maximum - full trend analysis

- **Control Buttons**:
  - ▶️ Start: Begin simulation
  - ⏹️ Stop: Pause simulation
  - 🔄 Reset: Clear all data

### 3. Alerts Panel
Real-time alerts displayed with:
- Alert severity indicators (Warning/Critical)
- Alert message with sensor details
- Timestamp of alert occurrence
- Visual color coding (Yellow/Red)

### 4. Sensor Cards (3 main cards)

#### 🌡️ Temperature Card
- Current temperature in °Celsius
- Min/Max/Average statistics
- Real-time status (Normal/Warning/Critical)
- Mini sparkline chart for quick trend view
- Status colors:
  - 🟢 Green: Normal (16-28°C)
  - 🟡 Yellow: Warning (<16°C or >28°C)
  - 🔴 Red: Critical (<15°C or >30°C)

#### 💧 Humidity Card
- Current humidity percentage
- Min/Max/Average statistics
- Real-time status (Normal/Warning/Critical)
- Mini sparkline chart
- Status colors:
  - 🟢 Green: Normal (30-80%)
  - 🟡 Yellow: Warning (<30% or >80%)
  - 🔴 Red: Critical (<25% or >85%)

#### 🚨 Motion Card
- Motion detection status (Detected/None)
- Detection count
- Total readings
- Detection percentage
- Status indicator:
  - 🟢 No Motion
  - 🟡 Motion Detected

### 5. Charts Section (4 Interactive Charts)

#### 📈 Temperature Trend Chart
- Line chart with area fill
- X-axis: Timestamps
- Y-axis: Temperature (°C, range 10-40)
- Color: Red (#ef4444)
- Shows temperature fluctuations over time

#### 📊 Humidity Trend Chart
- Line chart with area fill
- X-axis: Timestamps
- Y-axis: Humidity (%, range 0-100)
- Color: Blue (#3b82f6)
- Shows humidity variations over time

#### 🚨 Motion Detection Chart
- Bar chart showing motion events
- X-axis: Timestamps
- Y-axis: Motion state (0 or 1)
- Colors: Amber for detected, Gray for no motion
- Shows motion detection pattern

#### 📉 Data Distribution Chart
- Doughnut chart
- Shows ratio of motion detected vs. no motion
- Colors: Amber and Gray
- Displays percentage breakdown

### 6. Data Table
Recent readings with columns:
- **Timestamp**: ISO format with HH:MM:SS
- **Sensor Type**: Temperature/Humidity/Motion
- **Value**: Current reading
- **Unit**: °C, %, or State
- **Status**: Health indicator (✓ OK, ⚠️ High, ❌ Low, 🚨 Alert)
- Shows last 10 readings (30 total rows from last 10 timestamps)

## 🎨 Design Features

### Color Scheme
- **Primary Gradient**: Blue (#1e3c72 to #2a5298)
- **Temperature**: Red (#ef4444)
- **Humidity**: Blue (#3b82f6)
- **Motion**: Amber (#f59e0b)
- **Status**:
  - 🟢 Green (#4ade80) - Normal
  - 🟡 Yellow (#fbbf24) - Warning
  - 🔴 Red (#ef4444) - Critical

### Responsive Design
- **Desktop**: Full 4-column layout for charts
- **Tablet**: 2-column layout
- **Mobile**: Single column, optimized controls
- Touch-friendly buttons and inputs
- Adaptive font sizes

### Animations
- Pulse effect on status indicator
- Smooth chart transitions
- Card hover effects (scale + shadow)
- Status indicator animations
- Loading effects

## 📊 Sensor Simulation Details

### Temperature Sensor
```javascript
Range: 15-35°C
Initial: ~20-25°C
Variation: ±1°C per reading
Pattern: Realistic drift with small random fluctuations
Formula: temp = current_temp + (Math.random() - 0.5) * 2
```

### Humidity Sensor
```javascript
Range: 20-95%
Initial: ~50-70%
Variation: ±1.5% per reading
Pattern: Smooth, gradual changes
Formula: humid = current_humid + (Math.random() - 0.5) * 3
```

### Motion Sensor
```javascript
Type: Binary (0/1)
Probability: 30% chance per reading
Response: Immediate state change
Pattern: Random detection events
Formula: motion = Math.random() < 0.3 ? 1 : 0
```

## ⚠️ Alert Thresholds

### Temperature
- **Normal**: 16°C to 28°C
- **Warning**: < 16°C or > 28°C
- **Critical**: < 15°C or > 30°C

### Humidity
- **Normal**: 30% to 80%
- **Warning**: < 30% or > 80%
- **Critical**: < 25% or > 85%

### Motion
- **Alert**: Motion detected (value = 1)
- **Clear**: No motion (value = 0)

## 🔧 Configuration Options

### Update Intervals
```
1000ms  // 1 second - Real-time, high CPU usage
2000ms  // 2 seconds - Balanced (default)
5000ms  // 5 seconds - Lower CPU, smoother updates
10000ms // 10 seconds - Minimal updates, low CPU
```

### Data Points
```
10     // Minimal history, focused view
20     // Default - balanced view
50     // Extended history
100    // Maximum - full trend analysis
```

## 📈 How Data Updates Work

```
1. User clicks "Start"
2. Update interval is set from dropdown
3. Every interval (1-10 seconds):
   a. Generate realistic sensor values
   b. Add to data arrays
   c. Maintain max data points
   d. Update card displays
   e. Refresh all charts
   f. Check alert thresholds
   g. Update alert panel
   h. Add row to data table
   i. Update statistics (min/max/avg)
4. User can adjust interval or reset anytime
```

## 🎓 Skills Demonstrated

✅ **Data Visualization**
- Chart.js library mastery
- Multiple chart types (Line, Bar, Doughnut)
- Real-time data rendering
- Interactive visualizations
- Performance optimization

✅ **Monitoring Concepts**
- Real-time data collection
- Alert systems with thresholds
- Threshold-based notifications
- Historical data tracking
- Pattern recognition

✅ **Web Development**
- HTML5 semantic markup
- CSS3 advanced styling
- Flexbox and Grid layouts
- Responsive design
- CSS animations

✅ **JavaScript**
- DOM manipulation
- Event handling
- Array operations
- Data aggregation
- Statistics calculation

✅ **UI/UX Design**
- Color psychology
- Visual hierarchy
- Animation timing
- Touch-friendly design
- Accessibility

## 🔄 Future Enhancements

- 📥 Export data to CSV/JSON formats
- ⏮️ Historical data playback with timeline
- 📍 Multiple sensor instances/locations
- ⚙️ Custom alert threshold configuration
- 🔍 Data filtering and search functionality
- 🌍 Timezone support for timestamps
- 🌙 Dark mode theme toggle
- 🔌 Real hardware sensor integration
- 📡 MQTT data feed support
- ☁️ Cloud data synchronization
- 📱 Mobile app version
- 🔐 User authentication
- 📊 Advanced analytics

## 📚 Technologies Used

- **HTML5**: Semantic markup, Canvas API
- **CSS3**: Gradients, animations, flexbox, grid
- **JavaScript**: ES6+, DOM API, Event handling
- **Chart.js 3.x**: Data visualization library
- **Browser APIs**: 
  - Canvas for charts
  - RequestAnimationFrame for smooth updates
  - LocalStorage (future enhancement)

## 🐛 Browser Support

✅ Chrome 60+
✅ Firefox 55+
✅ Safari 12+
✅ Edge 79+
✅ Mobile browsers (iOS Safari, Chrome Mobile)

## 📝 Usage Examples

### Example 1: Quick Monitoring Session
1. Open dashboard.html
2. Default settings: 2s updates, 20 data points
3. Click Start
4. Watch for 2 minutes
5. Review trends in charts
6. Click Stop

### Example 2: Long-term Trend Analysis
1. Set Update Interval: 5 seconds
2. Set Data Points: 100
3. Click Start
4. Let run for 10 minutes
5. Observe extended trends
6. Check statistics for comprehensive min/max/avg

### Example 3: Alert Monitoring
1. Set Update Interval: 1 second
2. Set Data Points: 20
3. Click Start
4. Monitor Alerts panel
5. Watch for critical warnings
6. Review recent readings in table

## 🎯 Learning Outcomes

After working with this dashboard, you'll master:

- Real-time data visualization techniques
- Chart library selection and implementation
- Alert and notification systems
- Statistical analysis of sensor data
- Responsive web design patterns
- JavaScript event handling and DOM manipulation
- Chart.js library advanced features
- Performance optimization for real-time data
- Data-driven UI updates
- Color theory in UI design
- Animation timing and performance

## 🚀 Quick Links

- View Dashboard: Open `dashboard.html`
- Documentation: This file
- Sensor Simulator: See `sensor_simulator.py`
- Main Project: Check `README.md`

---

**Ready to monitor your IoT sensors? Open dashboard.html and click Start! 🚀**

**Last Updated**: 2026-05-22
**Version**: 1.0.0
