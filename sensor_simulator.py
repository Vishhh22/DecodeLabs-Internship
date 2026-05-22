"""
DecodeLabs Internship - Project 1: Sensor Data Simulator
Real-time IoT sensor data collection with data logging and analysis

Key Features:
- Temperature, Humidity, and Motion sensor simulation
- Realistic data with natural drift patterns
- JSON and CSV data export
- Comprehensive statistics and analysis
- Extensible architecture for adding new sensors
"""

import random
import time
import json
import csv
import datetime
import sys
import os
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from enum import Enum
from pathlib import Path


class SensorType(Enum):
    """Enumeration of sensor types"""
    TEMPERATURE = "temperature"
    HUMIDITY = "humidity"
    MOTION = "motion"


@dataclass
class SensorReading:
    """Data class for individual sensor readings"""
    sensor_type: str
    value: float
    unit: str
    timestamp: str
    sensor_id: str
    
    def to_dict(self):
        return asdict(self)
    
    def __str__(self):
        return f"[{self.timestamp}] {self.sensor_id}: {self.value}{self.unit}"


class BaseSensor:
    """Base class for all sensor types"""
    
    def __init__(self, sensor_id: str, min_val: float, max_val: float, initial_val: float):
        self.sensor_id = sensor_id
        self.min_value = min_val
        self.max_value = max_val
        self.current_value = initial_val
        self.drift_range = (max_val - min_val) * 0.05  # 5% of range
        
    def _constrain_value(self, value: float) -> float:
        """Keep value within valid range"""
        return max(self.min_value, min(self.max_value, value))
    
    def read(self) -> SensorReading:
        """Override in subclass"""
        raise NotImplementedError


class TemperatureSensor(BaseSensor):
    """Simulates a temperature sensor with realistic drift"""
    
    def __init__(self, sensor_id: str = "TEMP_001", initial_temp: float = 22.0):
        super().__init__(sensor_id, min_val=15.0, max_val=35.0, initial_val=initial_temp)
        self.sensor_type = SensorType.TEMPERATURE.value
        
    def read(self) -> SensorReading:
        """
        Generate simulated temperature reading with natural variation
        Range: 15-35°C with ±1°C drift per reading
        """
        drift = random.uniform(-1.0, 1.0)
        self.current_value = self._constrain_value(self.current_value + drift)
        
        return SensorReading(
            sensor_type=self.sensor_type,
            value=round(self.current_value, 2),
            unit="°C",
            timestamp=datetime.datetime.now().isoformat(),
            sensor_id=self.sensor_id
        )


class HumiditySensor(BaseSensor):
    """Simulates a humidity sensor with gradual changes"""
    
    def __init__(self, sensor_id: str = "HUM_001", initial_humidity: float = 50.0):
        super().__init__(sensor_id, min_val=20.0, max_val=95.0, initial_val=initial_humidity)
        self.sensor_type = SensorType.HUMIDITY.value
        
    def read(self) -> SensorReading:
        """
        Generate simulated humidity reading
        Range: 20-95% with ±2% drift per reading
        """
        drift = random.uniform(-2.0, 2.0)
        self.current_value = self._constrain_value(self.current_value + drift)
        
        return SensorReading(
            sensor_type=self.sensor_type,
            value=round(self.current_value, 2),
            unit="%",
            timestamp=datetime.datetime.now().isoformat(),
            sensor_id=self.sensor_id
        )


class MotionSensor(BaseSensor):
    """Simulates a motion sensor (binary: detected/not detected)"""
    
    def __init__(self, sensor_id: str = "MOTION_001", detection_probability: float = 0.3):
        super().__init__(sensor_id, min_val=0.0, max_val=1.0, initial_val=0.0)
        self.sensor_type = SensorType.MOTION.value
        self.detection_probability = detection_probability
        
    def read(self) -> SensorReading:
        """
        Generate simulated motion detection
        Returns 1.0 for motion detected, 0.0 for no motion
        """
        self.current_value = 1.0 if random.random() < self.detection_probability else 0.0
        
        return SensorReading(
            sensor_type=self.sensor_type,
            value=self.current_value,
            unit="state",
            timestamp=datetime.datetime.now().isoformat(),
            sensor_id=self.sensor_id
        )


class SensorDataLogger:
    """Handles logging and storage of sensor data"""
    
    def __init__(self, log_file: str = "sensor_data.json", csv_file: str = "sensor_data.csv"):
        self.log_file = Path(log_file)
        self.csv_file = Path(csv_file)
        self.readings: List[SensorReading] = []
        
    def add_reading(self, reading: SensorReading) -> None:
        """Add a sensor reading to the log"""
        self.readings.append(reading)
        
    def save_json(self) -> None:
        """Save all readings to a JSON file"""
        try:
            with open(self.log_file, 'w') as f:
                data = [reading.to_dict() for reading in self.readings]
                json.dump(data, f, indent=2)
            print(f"✓ JSON data saved to {self.log_file}")
        except IOError as e:
            print(f"✗ Error saving JSON: {e}")
        
    def save_csv(self) -> None:
        """Save all readings to a CSV file"""
        if not self.readings:
            print("✗ No data to save")
            return
            
        try:
            with open(self.csv_file, 'w', newline='') as f:
                fieldnames = ['sensor_type', 'value', 'unit', 'timestamp', 'sensor_id']
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                
                writer.writeheader()
                for reading in self.readings:
                    writer.writerow(reading.to_dict())
                    
            print(f"✓ CSV data saved to {self.csv_file}")
        except IOError as e:
            print(f"✗ Error saving CSV: {e}")
        
    def display_latest(self, count: int = 10) -> None:
        """Display the latest N readings"""
        print(f"\n{'='*80}")
        print(f"📋 Latest {count} Sensor Readings")
        print(f"{'='*80}")
        
        for i, reading in enumerate(self.readings[-count:], 1):
            symbol = "🌡️ " if reading.sensor_type == "temperature" else \
                    "💧 " if reading.sensor_type == "humidity" else "🚨 "
            print(f"{i:2d}. {symbol} {reading.sensor_id:15} {reading.value:8.2f} {reading.unit:5} | {reading.timestamp}")
        print()
    
    def get_data_by_type(self, sensor_type: str) -> List[SensorReading]:
        """Get all readings of a specific sensor type"""
        return [r for r in self.readings if r.sensor_type == sensor_type]


class SensorSimulator:
    """Main simulator that manages multiple sensors and collects data"""
    
    def __init__(self, temp_id: str = "TEMP_001", humid_id: str = "HUM_001", 
                 motion_id: str = "MOTION_001"):
        self.temp_sensor = TemperatureSensor(temp_id)
        self.humidity_sensor = HumiditySensor(humid_id)
        self.motion_sensor = MotionSensor(motion_id)
        self.logger = SensorDataLogger()
        self.reading_count = 0
        self.start_time = None
        self.alerts: List[Dict] = []
        
    def collect_reading(self) -> List[SensorReading]:
        """Collect readings from all sensors"""
        readings = [
            self.temp_sensor.read(),
            self.humidity_sensor.read(),
            self.motion_sensor.read()
        ]
        
        for reading in readings:
            self.logger.add_reading(reading)
            
        self.reading_count += 1
        return readings
    
    def display_current_readings(self, readings: List[SensorReading]) -> None:
        """Display current sensor readings in a formatted way"""
        print(f"\n[{datetime.datetime.now().strftime('%H:%M:%S')}] 📊 Sensor Readings:")
        print("-" * 80)
        
        for reading in readings:
            symbol = "🌡️ " if reading.sensor_type == "temperature" else \
                    "💧 " if reading.sensor_type == "humidity" else "🚨 "
            status = self._get_status(reading)
            print(f"  {symbol} {reading.sensor_id:15} {reading.value:8.2f} {reading.unit:5} | {status}")
    
    def _get_status(self, reading: SensorReading) -> str:
        """Get status of a reading based on thresholds"""
        if reading.sensor_type == "temperature":
            if reading.value > 30:
                return "🔴 CRITICAL (High)"
            elif reading.value < 15:
                return "🔴 CRITICAL (Low)"
            elif reading.value > 28:
                return "🟡 WARNING (High)"
            elif reading.value < 16:
                return "🟡 WARNING (Low)"
            return "🟢 Normal"
        
        elif reading.sensor_type == "humidity":
            if reading.value > 85:
                return "🔴 CRITICAL (High)"
            elif reading.value < 25:
                return "🔴 CRITICAL (Low)"
            elif reading.value > 80:
                return "🟡 WARNING (High)"
            elif reading.value < 30:
                return "🟡 WARNING (Low)"
            return "🟢 Normal"
        
        elif reading.sensor_type == "motion":
            return "🚨 MOTION DETECTED!" if reading.value == 1.0 else "🟢 No Motion"
        
        return "✓ OK"
    
    def run_simulation(self, duration_seconds: int = 30, interval: float = 2.0) -> None:
        """
        Run the sensor simulation for specified duration
        
        Args:
            duration_seconds: Total simulation time in seconds
            interval: Interval between readings in seconds
        """
        print(f"\n{'='*80}")
        print(f"🔬 SENSOR DATA SIMULATOR")
        print(f"{'='*80}")
        print(f"Duration: {duration_seconds}s | Interval: {interval}s")
        print(f"Sensors: Temperature, Humidity, Motion")
        print(f"{'='*80}")
        
        self.start_time = time.time()
        
        try:
            while time.time() - self.start_time < duration_seconds:
                readings = self.collect_reading()
                self.display_current_readings(readings)
                self._check_alerts(readings)
                
                # Wait before next reading
                elapsed = time.time() - self.start_time
                if elapsed < duration_seconds:
                    time.sleep(min(interval, duration_seconds - elapsed))
                    
        except KeyboardInterrupt:
            print("\n\n⚠️  Simulation interrupted by user")
        
        # Display summary and save data
        self._print_summary()
        self.save_data()
    
    def _check_alerts(self, readings: List[SensorReading]) -> None:
        """Check for alert conditions"""
        for reading in readings:
            if reading.sensor_type == "temperature":
                if reading.value > 30 or reading.value < 15:
                    self.alerts.append({
                        'type': 'CRITICAL',
                        'message': f'{reading.sensor_id}: Temperature {reading.value}°C',
                        'timestamp': reading.timestamp
                    })
            elif reading.sensor_type == "humidity":
                if reading.value > 85 or reading.value < 25:
                    self.alerts.append({
                        'type': 'CRITICAL',
                        'message': f'{reading.sensor_id}: Humidity {reading.value}%',
                        'timestamp': reading.timestamp
                    })
            elif reading.sensor_type == "motion" and reading.value == 1.0:
                self.alerts.append({
                    'type': 'WARNING',
                    'message': f'{reading.sensor_id}: Motion Detected',
                    'timestamp': reading.timestamp
                })
    
    def _print_summary(self) -> None:
        """Print simulation summary statistics"""
        elapsed = time.time() - self.start_time if self.start_time else 0
        
        print(f"\n{'='*80}")
        print(f"📊 SIMULATION SUMMARY")
        print(f"{'='*80}")
        print(f"Readings Collected: {self.reading_count}")
        print(f"Total Data Points: {len(self.logger.readings)}")
        print(f"Duration: {elapsed:.1f}s")
        print(f"Alerts Triggered: {len(self.alerts)}")
        print(f"{'='*80}\n")
    
    def save_data(self) -> None:
        """Save collected data to files"""
        print("💾 Saving sensor data...")
        self.logger.save_json()
        self.logger.save_csv()
        self.logger.display_latest(10)
    
    def get_statistics(self) -> Dict:
        """Calculate and display statistics for each sensor type"""
        stats = {
            'temperature': [],
            'humidity': [],
            'motion': []
        }
        
        for reading in self.logger.readings:
            if reading.sensor_type == 'temperature':
                stats['temperature'].append(reading.value)
            elif reading.sensor_type == 'humidity':
                stats['humidity'].append(reading.value)
            elif reading.sensor_type == 'motion':
                stats['motion'].append(reading.value)
        
        print(f"\n{'='*80}")
        print(f"📈 SENSOR STATISTICS")
        print(f"{'='*80}")
        
        if stats['temperature']:
            temps = stats['temperature']
            print(f"\n🌡️  Temperature (°C):")
            print(f"    Readings: {len(temps)}")
            print(f"    Min:  {min(temps):.2f}°C")
            print(f"    Max:  {max(temps):.2f}°C")
            print(f"    Avg:  {sum(temps)/len(temps):.2f}°C")
            print(f"    Range: {max(temps) - min(temps):.2f}°C")
        
        if stats['humidity']:
            humidity = stats['humidity']
            print(f"\n💧 Humidity (%):")
            print(f"    Readings: {len(humidity)}")
            print(f"    Min:  {min(humidity):.2f}%")
            print(f"    Max:  {max(humidity):.2f}%")
            print(f"    Avg:  {sum(humidity)/len(humidity):.2f}%")
            print(f"    Range: {max(humidity) - min(humidity):.2f}%")
        
        if stats['motion']:
            motion = stats['motion']
            motion_count = sum(motion)
            total = len(motion)
            print(f"\n🚨 Motion Detection:")
            print(f"    Readings: {total}")
            print(f"    Detections: {int(motion_count)}")
            print(f"    Detection Rate: {(motion_count/total)*100:.1f}%")
        
        print(f"{'='*80}\n")
        
        return stats
    
    def export_data(self, format: str = "both") -> None:
        """
        Export data in different formats
        
        Args:
            format: 'json', 'csv', or 'both'
        """
        print(f"\n📤 Exporting data as {format}...")
        if format in ['json', 'both']:
            self.logger.save_json()
        if format in ['csv', 'both']:
            self.logger.save_csv()
    
    def get_alerts(self) -> List[Dict]:
        """Get all recorded alerts"""
        return self.alerts
    
    def print_alerts(self) -> None:
        """Print all alerts that occurred during simulation"""
        if not self.alerts:
            print("\n✓ No alerts triggered")
            return
        
        print(f"\n{'='*80}")
        print(f"🚨 ALERTS LOG")
        print(f"{'='*80}")
        
        for i, alert in enumerate(self.alerts, 1):
            icon = "🔴" if alert['type'] == "CRITICAL" else "🟡"
            print(f"{i:2d}. {icon} [{alert['type']}] {alert['message']} at {alert['timestamp']}")
        
        print(f"{'='*80}\n")


def main():
    """Main entry point for the sensor simulator"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='DecodeLabs Sensor Simulator - IoT Data Collection',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python sensor_simulator.py                    # Default: 30s, 2s interval
  python sensor_simulator.py 60 1              # 60 seconds, 1 second interval
  python sensor_simulator.py 120 0.5           # 120 seconds, 0.5 second interval
        """
    )
    
    parser.add_argument('duration', nargs='?', type=int, default=30,
                       help='Simulation duration in seconds (default: 30)')
    parser.add_argument('interval', nargs='?', type=float, default=2.0,
                       help='Time between readings in seconds (default: 2.0)')
    parser.add_argument('--no-save', action='store_true',
                       help='Do not save data to files')
    parser.add_argument('--format', choices=['json', 'csv', 'both'], default='both',
                       help='Export format (default: both)')
    
    args = parser.parse_args()
    
    # Validate arguments
    if args.duration <= 0:
        print("Error: Duration must be positive")
        sys.exit(1)
    
    if args.interval <= 0:
        print("Error: Interval must be positive")
        sys.exit(1)
    
    # Create and run simulator
    simulator = SensorSimulator()
    simulator.run_simulation(duration_seconds=args.duration, interval=args.interval)
    simulator.get_statistics()
    simulator.print_alerts()
    
    if not args.no_save:
        simulator.export_data(args.format)


if __name__ == "__main__":
    main()
