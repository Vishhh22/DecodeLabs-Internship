"""
Quick demo script to show sample outputs without running full simulation
"""

import json
import random
import datetime
from dataclasses import asdict

# Sample output 1: Real-time readings display
print("=" * 60)
print("🔬 SENSOR DATA SIMULATOR - SAMPLE OUTPUT")
print("=" * 60)
print()

print("[10:30:45] Sensor Readings:")
print("-" * 50)
print(f"  🌡️  TEMP_001         22.34 °C")
print(f"  💧 HUM_001          52.16 %")
print(f"  🚨 MOTION_001            0.00 state")
print()

print("[10:30:47] Sensor Readings:")
print("-" * 50)
print(f"  🌡️  TEMP_001         22.89 °C")
print(f"  💧 HUM_001          50.45 %")
print(f"  🚨 MOTION_001            1.00 state")
print()

print("[10:30:49] Sensor Readings:")
print("-" * 50)
print(f"  🌡️  TEMP_001         23.15 °C")
print(f"  💧 HUM_001          51.92 %")
print(f"  🚨 MOTION_001            0.00 state")
print()

print("[10:30:51] Sensor Readings:")
print("-" * 50)
print(f"  🌡️  TEMP_001         22.67 °C")
print(f"  💧 HUM_001          49.87 %")
print(f"  🚨 MOTION_001            1.00 state")
print()

# Sample output 2: Simulation summary
print("=" * 60)
print("📊 SIMULATION SUMMARY")
print("=" * 60)
print(f"Total Readings Collected: 4")
print(f"Total Data Points: 12")
print(f"Sensors Active: 3 (Temperature, Humidity, Motion)")
print("=" * 60)
print()

# Sample output 3: Statistics
print("=" * 60)
print("📈 SENSOR STATISTICS")
print("=" * 60)
print(f"Temperature (°C):")
print(f"  Min: 22.34°C | Max: 23.15°C | Avg: 22.76°C")
print()
print(f"Humidity (%):")
print(f"  Min: 49.87% | Max: 52.16% | Avg: 51.10%")
print()
print(f"Motion Detection:")
print(f"  Detections: 2 / 4 readings")
print("=" * 60)
print()

# Sample output 4: JSON data
print("=" * 60)
print("💾 SAMPLE JSON OUTPUT (sensor_data.json)")
print("=" * 60)

sample_json = [
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
    },
    {
        "sensor_type": "motion",
        "value": 0.0,
        "unit": "state",
        "timestamp": "2026-05-22T10:30:45.345678",
        "sensor_id": "MOTION_001"
    },
    {
        "sensor_type": "temperature",
        "value": 22.89,
        "unit": "°C",
        "timestamp": "2026-05-22T10:30:47.456789",
        "sensor_id": "TEMP_001"
    },
    {
        "sensor_type": "humidity",
        "value": 50.45,
        "unit": "%",
        "timestamp": "2026-05-22T10:30:47.567890",
        "sensor_id": "HUM_001"
    },
    {
        "sensor_type": "motion",
        "value": 1.0,
        "unit": "state",
        "timestamp": "2026-05-22T10:30:47.678901",
        "sensor_id": "MOTION_001"
    }
]

print(json.dumps(sample_json, indent=2))
print()

# Sample output 5: CSV data
print("=" * 60)
print("📊 SAMPLE CSV OUTPUT (sensor_data.csv)")
print("=" * 60)
print("sensor_type,value,unit,timestamp,sensor_id")
print("temperature,22.34,°C,2026-05-22T10:30:45.123456,TEMP_001")
print("humidity,52.16,%,2026-05-22T10:30:45.234567,HUM_001")
print("motion,0.0,state,2026-05-22T10:30:45.345678,MOTION_001")
print("temperature,22.89,°C,2026-05-22T10:30:47.456789,TEMP_001")
print("humidity,50.45,%,2026-05-22T10:30:47.567890,HUM_001")
print("motion,1.0,state,2026-05-22T10:30:47.678901,MOTION_001")
print("temperature,23.15,°C,2026-05-22T10:30:49.789012,TEMP_001")
print("humidity,51.92,%,2026-05-22T10:30:49.890123,HUM_001")
print("motion,0.0,state,2026-05-22T10:30:49.901234,MOTION_001")
print("temperature,22.67,°C,2026-05-22T10:30:51.012345,TEMP_001")
print("humidity,49.87,%,2026-05-22T10:30:51.123456,HUM_001")
print("motion,1.0,state,2026-05-22T10:30:51.234567,MOTION_001")
print()

# Sample output 6: Latest readings display
print("=" * 60)
print("Latest 5 Sensor Readings")
print("=" * 60)
print("[2026-05-22T10:30:45.123456] TEMP_001: 22.34°C (temperature)")
print("[2026-05-22T10:30:45.234567] HUM_001: 52.16% (humidity)")
print("[2026-05-22T10:30:45.345678] MOTION_001: 0.0state (motion)")
print("[2026-05-22T10:30:47.456789] TEMP_001: 22.89°C (temperature)")
print("[2026-05-22T10:30:47.567890] HUM_001: 50.45% (humidity)")
print()

print("✓ Data saved to sensor_data.json")
print("✓ Data saved to sensor_data.csv")
print()
print("=" * 60)
print("✅ SIMULATION COMPLETE")
print("=" * 60)
