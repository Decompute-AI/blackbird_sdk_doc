# Installation & Setup

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 2GB+ free space for models and cache
- **Network**: Internet connection for model downloads and web features

### Installation Steps

### 1. Environment Setup

```bash
# Create virtual environmentpython -m venv blackbird_env
# Activate environment# Windows:blackbird_env\Scripts\activate# macOS/Linux:source blackbird_env/bin/activate
# Upgrade pippython -m pip install --upgrade pip
```

### 2. Install Blackbird SDK

```bash
# Install from source (development)
git clone [repository link to be added here]
cd blackbird_sdk
# install the requirements
pip install -r requirements.txt
pip install -e .
# Or install from PyPI (when available)pip install blackbird-sdk
```

### 3. Verify Installation

```python
# Test basic importpython -c "from blackbird_sdk import BlackbirdSDK; print('✅ Installation successful')"# Check versionpython -c "import blackbird_sdk; print(f'Version: {blackbird_sdk.__version__}')"
```

### Quick Start

### Basic Usage Example

```python
from blackbird_sdk import BlackbirdSDK
# Initialize SDKsdk = BlackbirdSDK(development_mode=True)
# Initialize an agentsdk.initialize_agent("finance")
# Send a messageresponse = sdk.send_message("What are the current market trends?")
print(response)
# Clean upsdk.cleanup()
```

### Advanced Setup with Configuration

```python
from blackbird_sdk import BlackbirdSDK
# Custom configurationconfig = {
    'backend_port': 5012,
    'log_level': 'INFO',
    'max_sessions': 100,
    'timeout': 300}
# Initialize with custom settingssdk = BlackbirdSDK(
    config=config,
    development_mode=False,
    user_logging=True,
    structured_logging=True)
# Initialize with specific modelsdk.initialize_agent("finance", model="unsloth/Qwen3-1.7B-bnb-4bit")
# Start interactive sessionresponse = sdk.send_message("Hello! I need help with financial analysis.")
print(f"Agent Response: {response}")
```
