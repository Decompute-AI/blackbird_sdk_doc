# Session Management Documentation

## Overview

The Blackbird SDK includes a comprehensive session management system that handles user sessions, quotas, rate limiting, and usage tracking for enterprise-grade applications.

## Core Session Features

### Session Creation and Management

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.session.session_types import QuotaType, RateLimitType
# Initialize SDKsdk = BlackbirdSDK(development_mode=True)
# Create user session with specific tiersession = sdk.session_manager.create_session(
    user_id="user123",
    tier="pro",  # Options: free, basic, pro, enterprise    metadata={
        "department": "research",
        "project": "ai_analysis",
        "created_by": "admin"    }
)
print(f"Session created: {session.session_id}")
print(f"User ID: {session.user_id}")
print(f"Status: {session.status}")
```

### Session Information and Status

```python
# Get session detailssession_data = sdk.session_manager.get_session_data(session.session_id)
print(f"Session Data: {session_data}")
# Check session statussession = sdk.session_manager.get_session(session.session_id)
if session:
    print(f"Session active: {session.is_active}")
    print(f"Age: {session.age_seconds} seconds")
    print(f"Idle time: {session.idle_seconds} seconds")
    print(f"Concurrent operations: {session.concurrent_operations}")
```

## Quota Management

### Understanding Quotas

The session system supports multiple quota types:

- **API_CALLS**: Number of API requests
- **TOKENS**: Token usage for AI models
- **STORAGE**: Storage space used
- **BANDWIDTH**: Data transfer limits
- **CONCURRENT_REQUESTS**: Simultaneous operations

### Quota Monitoring

```python
# Get all quotas for a sessionquotas = sdk.session_manager.get_quota(session.session_id)
print("Current Quotas:")
for quota_type, info in quotas.items():
    print(f"  {quota_type}:")
    print(f"    Used: {info['used']}/{info['limit']}")
    print(f"    Remaining: {info['remaining']}")
    print(f"    Usage: {info['usage_percentage']:.1f}%")
# Get specific quotaapi_quota = sdk.session_manager.get_quota(session.session_id, QuotaType.API_CALLS)
print(f"API Calls: {api_quota}")
```

### Quota Usage Tracking

```python
# Track usage for different operationsdef track_operation_usage(session_id, operation_name, resource_type, amount):
    """Track resource usage for an operation."""    try:
        success = sdk.session_manager.track_usage(
            session_id=session_id,
            operation=operation_name,
            resource_type=resource_type,
            amount=amount,
            metadata={"timestamp": time.time(), "operation": operation_name}
        )
        if success:
            print(f"✅ Tracked {amount} {resource_type.value} for {operation_name}")
        return success
    except QuotaExceededError as e:
        print(f"❌ Quota exceeded: {e.message}")
        print(f"   Used: {e.used}, Limit: {e.limit}")
        return False# Track different types of usagetrack_operation_usage(session.session_id, "send_message", QuotaType.API_CALLS, 1)
track_operation_usage(session.session_id, "file_upload", QuotaType.STORAGE, 1024)  # 1KBtrack_operation_usage(session.session_id, "ai_inference", QuotaType.TOKENS, 150)
```

### Custom Quota Handlers

```python
class QuotaManager:
    def __init__(self, sdk):
        self.sdk = sdk
        self.usage_callbacks = []
    def add_usage_callback(self, callback):
        """Add callback for usage events."""        self.usage_callbacks.append(callback)
        self.sdk.session_manager.add_usage_callback(callback)
    def check_quota_status(self, session_id):
        """Check if any quotas are near limits."""        quotas = self.sdk.session_manager.get_quota(session_id)
        warnings = []
        for quota_type, info in quotas.items():
            usage_pct = info['usage_percentage']
            if usage_pct >= 90:
                warnings.append(f"{quota_type}: {usage_pct:.1f}% used")
            elif usage_pct >= 75:
                warnings.append(f"{quota_type}: {usage_pct:.1f}% used (warning)")
        return warnings
    def predict_quota_exhaustion(self, session_id):
        """Predict when quotas might be exhausted."""        # Get usage history        session_obj = self.sdk.session_manager.get_session(session_id)
        if not session_obj:
            return {}
        usage_history = self.sdk.session_manager.get_usage_history(
            session_obj.user_id,
            limit=100        )
        # Simple prediction based on recent usage patterns        # In production, this could use more sophisticated algorithms        predictions = {}
        for quota_type, quota_info in self.sdk.session_manager.get_quota(session_id).items():
            remaining = quota_info['remaining']
            if remaining > 0:
                # Calculate average usage rate                recent_usage = [
                    record for record in usage_history
                    if record['resource_type'] == quota_type
                ]
                if recent_usage:
                    avg_rate = len(recent_usage) / len(usage_history) if usage_history else 0                    if avg_rate > 0:
                        time_to_exhaustion = remaining / avg_rate
                        predictions[quota_type] = {
                            'time_to_exhaustion_hours': time_to_exhaustion,
                            'predicted_exhaustion': time.time() + (time_to_exhaustion * 3600)
                        }
        return predictions
# Usagequota_manager = QuotaManager(sdk)
# Add usage callbackdef usage_alert(usage_record):
    print(f"🔔 Usage Alert: {usage_record.operation} used {usage_record.amount} {usage_record.resource_type.value}")
quota_manager.add_usage_callback(usage_alert)
# Check quota statuswarnings = quota_manager.check_quota_status(session.session_id)
for warning in warnings:
    print(f"⚠️ Quota Warning: {warning}")
```

## Rate Limiting

### Rate Limit Enforcement

```python
# Enforce rate limits for operationsdef safe_api_call(session_id, operation_func, *args, **kwargs):
    """Make API call with rate limiting."""    try:
        # Check rate limit before operation        sdk.session_manager.enforce_rate_limit(
            session_id=session_id,
            operation="api_call",
            limit_type=RateLimitType.PER_MINUTE
        )
        # Perform the operation        result = operation_func(*args, **kwargs)
        # Track usage        sdk.session_manager.track_usage(
            session_id=session_id,
            operation="api_call",
            resource_type=QuotaType.API_CALLS,
            amount=1        )
        return result
    except RateLimitError as e:
        print(f"⏱️ Rate limit exceeded: {e.message}")
        if e.retry_after:
            print(f"   Retry after: {e.retry_after:.1f} seconds")
        raise# Usage with rate limitingdef send_message_with_limits(session_id, message):
    """Send message with rate limiting."""    return safe_api_call(
        session_id,
        lambda: sdk.send_message(message)
    )
# Test rate limitingtry:
    for i in range(10):
        response = send_message_with_limits(session.session_id, f"Test message {i}")
        print(f"Message {i}: Success")
        time.sleep(0.1)  # Small delayexcept RateLimitError as e:
    print(f"Rate limit hit: {e}")
```

### Custom Rate Limiting

```python
class CustomRateLimiter:
    def __init__(self, sdk):
        self.sdk = sdk
        self.custom_limits = {}
    def set_custom_limit(self, session_id, operation, max_calls, time_window):
        """Set custom rate limit for specific operation."""        if session_id not in self.custom_limits:
            self.custom_limits[session_id] = {}
        self.custom_limits[session_id][operation] = {
            'max_calls': max_calls,
            'time_window': time_window,
            'calls': [],
            'last_reset': time.time()
        }
    def check_custom_limit(self, session_id, operation):
        """Check if custom rate limit allows operation."""        if session_id not in self.custom_limits:
            return True        if operation not in self.custom_limits[session_id]:
            return True        limit_info = self.custom_limits[session_id][operation]
        current_time = time.time()
        # Reset if time window passed        if current_time - limit_info['last_reset'] > limit_info['time_window']:
            limit_info['calls'] = []
            limit_info['last_reset'] = current_time
        # Clean old calls outside time window        limit_info['calls'] = [
            call_time for call_time in limit_info['calls']
            if current_time - call_time < limit_info['time_window']
        ]
        # Check limit        if len(limit_info['calls']) >= limit_info['max_calls']:
            return False        # Record this call        limit_info['calls'].append(current_time)
        return True# Usagerate_limiter = CustomRateLimiter(sdk)
# Set custom limitsrate_limiter.set_custom_limit(session.session_id, "file_upload", 5, 60)  # 5 per minuterate_limiter.set_custom_limit(session.session_id, "ai_inference", 20, 3600)  # 20 per hour# Check before operationsif rate_limiter.check_custom_limit(session.session_id, "file_upload"):
    print("File upload allowed")
else:
    print("File upload rate limit exceeded")
```

## Concurrency Management

### Managing Concurrent Operations

```python
# Manage concurrent operationsdef with_concurrency_control(session_id, operation_name):
    """Decorator for concurrency control."""    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Increment concurrent operations                sdk.session_manager.manage_concurrency(
                    session_id=session_id,
                    operation=operation_name,
                    increment=True                )
                # Execute operation                result = func(*args, **kwargs)
                return result
            finally:
                # Decrement concurrent operations                sdk.session_manager.manage_concurrency(
                    session_id=session_id,
                    operation=operation_name,
                    increment=False                )
        return wrapper
    return decorator
# Usage@with_concurrency_control(session.session_id, "file_processing")
def process_large_file(file_path):
    """Process large file with concurrency control."""    print(f"Processing {file_path}...")
    time.sleep(2)  # Simulate processing time    return f"Processed {file_path}"# Test concurrency limitsimport threading
def worker(file_id):
    try:
        result = process_large_file(f"file_{file_id}.txt")
        print(f"Worker {file_id}: {result}")
    except RateLimitError as e:
        print(f"Worker {file_id}: Concurrency limit exceeded")
# Start multiple workersthreads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()
# Wait for completionfor thread in threads:
    thread.join()
```

## Session Analytics and Monitoring

### Usage Analytics

```python
class SessionAnalytics:
    def __init__(self, sdk):
        self.sdk = sdk
    def get_user_analytics(self, user_id):
        """Get comprehensive analytics for a user."""        # Get user sessions        sessions = self.sdk.session_manager.get_user_sessions(user_id)
        # Get usage history        usage_history = self.sdk.session_manager.get_usage_history(user_id, limit=1000)
        # Calculate analytics        total_sessions = len(sessions)
        active_sessions = len([s for s in sessions if s.is_active])
        # Usage by operation        operation_counts = {}
        resource_usage = {}
        for record in usage_history:
            op = record['operation']
            resource = record['resource_type']
            amount = record['amount']
            operation_counts[op] = operation_counts.get(op, 0) + 1            resource_usage[resource] = resource_usage.get(resource, 0) + amount
        return {
            'user_id': user_id,
            'total_sessions': total_sessions,
            'active_sessions': active_sessions,
            'total_operations': len(usage_history),
            'operation_breakdown': operation_counts,
            'resource_usage': resource_usage,
            'most_used_operation': max(operation_counts, key=operation_counts.get) if operation_counts else None        }
    def get_system_analytics(self):
        """Get system-wide analytics."""        stats = self.sdk.session_manager.get_statistics()
        return {
            'system_stats': stats,
            'timestamp': time.time()
        }
# Usageanalytics = SessionAnalytics(sdk)
# Get user analyticsuser_analytics = analytics.get_user_analytics("user123")
print("User Analytics:")
print(json.dumps(user_analytics, indent=2))
# Get system analyticssystem_analytics = analytics.get_system_analytics()
print("System Analytics:")
print(json.dumps(system_analytics, indent=2))
```

### Real-time Monitoring

```python
class SessionMonitor:
    def __init__(self, sdk):
        self.sdk = sdk
        self.monitoring = False        self.alerts = []
    def start_monitoring(self):
        """Start real-time session monitoring."""        self.monitoring = True        def monitor_loop():
            while self.monitoring:
                try:
                    self.check_system_health()
                    time.sleep(30)  # Check every 30 seconds                except Exception as e:
                    print(f"Monitoring error: {e}")
        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()
        print("📊 Session monitoring started")
    def check_system_health(self):
        """Check system health and generate alerts."""        stats = self.sdk.session_manager.get_statistics()
        # Check for high session count        if stats['active_sessions'] > 100:
            self.add_alert(f"High session count: {stats['active_sessions']}")
        # Check session distribution        if stats['average_sessions_per_user'] > 5:
            self.add_alert(f"High sessions per user: {stats['average_sessions_per_user']:.1f}")
    def add_alert(self, message):
        """Add monitoring alert."""        alert = {
            'timestamp': time.time(),
            'message': message
        }
        self.alerts.append(alert)
        print(f"🚨 Alert: {message}")
    def get_alerts(self, last_n=10):
        """Get recent alerts."""        return self.alerts[-last_n:]
# Usagemonitor = SessionMonitor(sdk)
monitor.start_monitoring()
# Get alerts after some timetime.sleep(5)
alerts = monitor.get_alerts()
for alert in alerts:
    print(f"Alert: {alert['message']}")
```
