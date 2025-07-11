# Backend Management Documentation

## Overview

The Blackbird SDK includes a sophisticated backend management system that automatically handles server deployment, scaling, health monitoring, and resource management across different platforms.

## Core Backend Features

### Automatic Backend Deployment

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.server import BackendManager
# Initialize SDK with automatic backend managementsdk = BlackbirdSDK(development_mode=True)
# Backend is automatically started during SDK initialization# Check backend statusbackend_status = sdk.get_backend_status()
print("Backend Status:")
print(f"  Running: {backend_status['is_running']}")
print(f"  Port: {backend_status['port']}")
print(f"  Health Check: {backend_status['health_check']}")
print(f"  Process ID: {backend_status.get('process_id', 'Unknown')}")
```

### Manual Backend Management

```python
# Get backend manager instancebackend_manager = BackendManager.get_instance()
# Start backend manuallybackend_path = r"C:\decompute-app\sdk\blackbird_sdk\backends\windows\decompute.py"success = backend_manager.start_backend(backend_path, port=5012)
if success:
    print("✅ Backend started successfully")
else:
    print("❌ Failed to start backend")
# Check backend healthhealth_status = backend_manager.health_check()
print(f"Backend health: {'✅ Healthy' if health_status else '❌ Unhealthy'}")
# Get detailed statusstatus = backend_manager.get_backend_status()
print("Detailed Backend Status:")
for key, value in status.items():
    print(f"  {key}: {value}")
```

### Platform-Specific Backend Management

```python
from blackbird_sdk.acceleration.platform_manager import PlatformManager
# Initialize platform managerplatform_manager = PlatformManager()
# Get platform informationplatform_info = platform_manager.get_platform_info()
print("Platform Information:")
print(f"  OS: {platform_info['platform']}")
print(f"  Processor: {platform_info['processor']}")
print(f"  GPU Type: {platform_info.get('gpu_type', 'None')}")
print(f"  Memory: {platform_info.get('memory_gb', 'Unknown')} GB")
print(f"  CPU Cores: {platform_info.get('cpu_cores', 'Unknown')}")
# Get optimized backend configurationbackend_config = platform_manager.get_optimized_config()
print("\nOptimized Backend Configuration:")
for key, value in backend_config.items():
    print(f"  {key}: {value}")
```

## Backend Health Monitoring

### Comprehensive Health Checks

```python
class BackendHealthMonitor:
“““Comprehensive backend health monitoring system.”“”

```
def __init__(self, backend_manager):
    self.backend_manager = backend_manager
    self.health_history = []
    self.alert_thresholds = {
        'response_time_ms': 1000,
        'memory_usage_percent': 85,
        'cpu_usage_percent': 80,
        'error_rate_percent': 5
    }

def perform_comprehensive_health_check(self):
    """Perform detailed health check with metrics."""
    import time
    import requests
    import psutil

    health_result = {
        'timestamp': time.time(),
        'overall_healthy': True,
        'checks': {},
        'metrics': {},
        'alerts': []
    }

    # Basic connectivity check
    start_time = time.time()
    try:
        response = requests.get(f"{self.backend_manager.base_url}/health", timeout=5)
        response_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        health_result['checks']['connectivity'] = {
            'status': 'healthy' if response.status_code == 200 else 'unhealthy',
            'response_time_ms': response_time,
            'status_code': response.status_code
        }

        if response_time > self.alert_thresholds['response_time_ms']:
            health_result['alerts'].append(f"High response time: {response_time:.0f}ms")

    except Exception as e:
        health_result['checks']['connectivity'] = {
            'status': 'unhealthy',
            'error': str(e)
        }
        health_result['overall_healthy'] = False

    # System resource checks
    try:
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        health_result['metrics']['cpu_usage_percent'] = cpu_percent

        if cpu_percent > self.alert_thresholds['cpu_usage_percent']:
            health_result['alerts'].append(f"High CPU usage: {cpu_percent:.1f}%")

        # Memory usage
        memory = psutil.virtual_memory()
        health_result['metrics']['memory_usage_percent'] = memory.percent
        health_result['metrics']['memory_available_gb'] = memory.available / (1024**3)

        if memory.percent > self.alert_thresholds['memory_usage_percent']:
            health_result['alerts'].append(f"High memory usage: {memory.percent:.1f}%")

        # Disk usage
        disk = psutil.disk_usage('/')
        health_result['metrics']['disk_usage_percent'] = (disk.used / disk.total) * 100

        # Network I/O
        network = psutil.net_io_counters()
        health_result['metrics']['network_bytes_sent'] = network.bytes_sent
        health_result['metrics']['network_bytes_recv'] = network.bytes_recv

        health_result['checks']['system_resources'] = {'status': 'healthy'}

    except Exception as e:
        health_result['checks']['system_resources'] = {
            'status': 'unhealthy',
            'error': str(e)
        }
        health_result['overall_healthy'] = False

    # API endpoint checks
    endpoint_checks = self._check_api_endpoints()
    health_result['checks']['api_endpoints'] = endpoint_checks

    if not all(check['status'] == 'healthy' for check in endpoint_checks.values()):
        health_result['overall_healthy'] = False

    # Store health history
    self.health_history.append(health_result)

    # Keep only last 100 entries
    if len(self.health_history) > 100:
        self.health_history = self.health_history[-100:]

    return health_result

def _check_api_endpoints(self):
    """Check health of individual API endpoints."""
    endpoints_to_check = [
        '/health',
        '/api/chat',
        '/api/agents',
        '/debug-routes'
    ]

    endpoint_results = {}

    for endpoint in endpoints_to_check:
        try:
            start_time = time.time()

            if endpoint == '/api/chat':
                # POST request for chat endpoint
                response = requests.post(
                    f"{self.backend_manager.base_url}{endpoint}",
                    json={'message': 'health check', 'agent': 'general'},
                    timeout=10
                )
            else:
                # GET request for other endpoints
                response = requests.get(
                    f"{self.backend_manager.base_url}{endpoint}",
                    timeout=5
                )

            response_time = (time.time() - start_time) * 1000

            endpoint_results[endpoint] = {
                'status': 'healthy' if response.status_code in [200, 201] else 'unhealthy',
                'response_time_ms': response_time,
                'status_code': response.status_code
            }

        except Exception as e:
            endpoint_results[endpoint] = {
                'status': 'unhealthy',
                'error': str(e)
            }

    return endpoint_results

def get_health_trends(self, hours=24):
    """Analyze health trends over time."""
    current_time = time.time()
    cutoff_time = current_time - (hours * 3600)

    # Filter recent health checks
    recent_checks = [
        check for check in self.health_history
        if check['timestamp'] >= cutoff_time
    ]

    if not recent_checks:
        return {"error": "No health data available for the specified period"}

    # Calculate trends
    trends = {
        'period_hours': hours,
        'total_checks': len(recent_checks),
        'healthy_checks': len([c for c in recent_checks if c['overall_healthy']]),
        'unhealthy_checks': len([c for c in recent_checks if not c['overall_healthy']]),
        'uptime_percentage': 0,
        'average_response_time_ms': 0,
        'common_alerts': {}
    }

    # Calculate uptime percentage
    trends['uptime_percentage'] = (trends['healthy_checks'] / trends['total_checks']) * 100

    # Calculate average response time
    response_times = []
    all_alerts = []

    for check in recent_checks:
        connectivity_check = check.get('checks', {}).get('connectivity', {})
        if 'response_time_ms' in connectivity_check:
            response_times.append(connectivity_check['response_time_ms'])

        all_alerts.extend(check.get('alerts', []))

    if response_times:
        trends['average_response_time_ms'] = sum(response_times) / len(response_times)

    # Count common alerts
    for alert in all_alerts:
        alert_type = alert.split(':')[^0]  # Get first part before colon
        trends['common_alerts'][alert_type] = trends['common_alerts'].get(alert_type, 0) + 1

    return trends

def generate_health_report(self):
    """Generate comprehensive health report."""
    latest_check = self.health_history[-1] if self.health_history else None
    trends_24h = self.get_health_trends(24)
    trends_1h = self.get_health_trends(1)

    if not latest_check:
        return "No health data available"

    report = f"""
```

# BACKEND HEALTH REPORT

Generated: {datetime.fromtimestamp(latest_check[‘timestamp’]).strftime(‘%Y-%m-%d %H:%M:%S’)}

CURRENT STATUS:
- Overall Health: {‘✅ Healthy’ if latest_check[‘overall_healthy’] else ‘❌ Unhealthy’}
- Response Time: {latest_check.get(‘checks’, {}).get(‘connectivity’, {}).get(‘response_time_ms’, ‘N/A’)}ms
- CPU Usage: {latest_check.get(‘metrics’, {}).get(‘cpu_usage_percent’, ‘N/A’)}%
- Memory Usage: {latest_check.get(‘metrics’, {}).get(‘memory_usage_percent’, ‘N/A’)}%

24-HOUR TRENDS:
- Uptime: {trends_24h.get(‘uptime_percentage’, 0):.1f}%
- Average Response Time: {trends_24h.get(‘average_response_time_ms’, 0):.0f}ms
- Total Health Checks: {trends_24h.get(‘total_checks’, 0)}
- Issues Detected: {trends_24h.get(‘unhealthy_checks’, 0)}

RECENT ALERTS


"""
