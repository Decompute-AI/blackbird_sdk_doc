# Installation & Setup

### System Requirements

- **Python**: 3.12

**CUDA Systems:**

- Windows 10/11 or Linux (Ubuntu 18.04+)
- NVIDIA GPU with CUDA support
- CUDA drivers installed
- 8GB+ RAM recommended

**Mac Systems:**

- macOS 12.0+ (Monterey or later)
- Apple Silicon (M1/M2/M3) or Intel Mac
- 8GB+ RAM recommended

### Getting Your Package

Users need to:

1. Contact the license server administrator
2. Receive the download URL
3. Choose their system type (CUDA or Mac)
4. Download the appropriate package

### Installation Steps

**For CUDA Systems (Windows/Linux with NVIDIA GPUs):**

1.  Download the CUDA package from the license server.
2.  Extract the ZIP file and rename the extracted folder to `blackbird_sdk`.
3.  Open PowerShell (Windows) or Terminal (Linux) in the `blackbird_sdk` directory.
4.  Activate the virtual environment:
    *   **Windows:** `.\\venv\\Scripts\\Activate.ps1`
    *   **Linux:** `source venv/bin/activate`
5.  **For Windows:** Install dependencies in the correct order:
    ```bash
    pip install -r requirements.txt
    pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0+cu124 --index-url https://download.pytorch.org/whl/cu124
    ```
6.  Test the SDK:
    ```python
    python -c "from sdk.blackbird_sdk_obfuscated import BlackBirdSDK; print('SDK loaded successfully!')"
    ```

**For Mac Systems (Apple Silicon + MLX):**

1.  Download the Mac package from the license server.
2.  Extract the ZIP file and rename the extracted folder to `blackbird_sdk`.
3.  Set up your Python 3.12 environment:
    ```bash
    python3.12 -m venv blackbird_env
    source blackbird_env/bin/activate
    ```
4.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Optional:** Install MLX for optimized training:
    ```bash
    pip install mlx
    ```
6.  Test the SDK:
    ```python
    python -c "from blackbird_sdk_obfuscated import BlackBirdSDK; print('SDK loaded successfully!')"
    ```

### What's Included in Your Package

**CUDA Package Contents:**

*   ✅ Obfuscated SDK (protected with PyArmor)
*   ✅ Complete virtual environment with all dependencies
*   ✅ CUDA-optimized packages (PyTorch, Transformers)
*   ✅ Unsloth support for optimized training
*   ✅ Ready to run immediately on NVIDIA GPUs

**Mac Package Contents:**

*   ✅ Obfuscated SDK (protected with PyArmor)
*   ✅ Requirements file for dependencies
*   ✅ Apple Silicon optimized packages
*   ✅ MLX support for training
*   ⚠️ Manual environment setup required

### Virtual Environment Information

**For CUDA Users:** The package includes a complete virtual environment (`.venv`) with all dependencies pre-installed. This environment contains:

*   PyTorch with CUDA support
*   Transformers library
*   All required Python packages
*   Unsloth for optimized training

**For Mac Users:** You'll need to create your own virtual environment and install dependencies from the provided `requirements.txt` file.

### Quick Start

**CUDA Systems:**

```python
# Make sure your virtual environment is activated
from sdk.blackbird_sdk_obfuscated import BlackBirdSDK
import asyncio

async def main():
    sdk = BlackBirdSDK()
    response = await sdk.chat_async("Hello, world!")
    print(response)

asyncio.run(main())
```

### Common Errors and Fixes

#### Error: `Could not find module blackbird_sdk` or `Could not find module pyarmor_runtime`

This error occurs when the Python interpreter cannot find the necessary SDK files. To resolve this, you need to add the `blackbird_sdk` folder (which contains the `pyarmor_runtime` folder) to your Python path.

**Windows (Command Prompt):**
```bash
set PYTHONPATH=%PYTHONPATH%;C:\\path\\to\\blackbird_sdk
```

**Windows (PowerShell):**
```powershell
$env:PYTHONPATH = "$env:PYTHONPATH;C:\\path\\to\\blackbird_sdk"
```

**Linux/macOS (Bash):**
```bash
export PYTHONPATH=$PYTHONPATH:/path/to/blackbird_sdk
```

**Note:** Replace `C:\\path\\to\\blackbird_sdk` or `/path/to/blackbird_sdk` with the actual path to the `blackbird_sdk` directory you created in the installation steps.

#### Error: SDK Fails to Initialize

If the SDK fails to initialize, it may be because another process is already using the default port (5012). To resolve this, you need to find and stop the process using that port.

**Windows:**
1.  Find the process ID (PID) using port 5012:
    ```bash
    netstat -ano | findstr :5012
    ```
2.  Kill the process using its PID (replace `YOUR_PID` with the actual PID from the previous command):
    ```bash
    taskkill /PID YOUR_PID /F
    ```

**macOS/Linux:**
1.  Find the process ID (PID) using port 5012:
    ```bash
    lsof -i :5012
    ```
2.  Kill the process using its PID (replace `YOUR_PID` with the actual PID from the previous command):
    ```bash
    kill -9 YOUR_PID
    ```

**Mac Systems:**

```python
from blackbird_sdk_obfuscated import BlackBirdSDK
import asyncio

async def main():
    sdk = BlackBirdSDK()
    response = await sdk.chat_async("Hello, world!")
    print(response)

asyncio.run(main())
```
