# Installation & Setup

### System Requirements

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
2.  Extract the ZIP file to your desired directory.
3.  Open PowerShell (Windows) or Terminal (Linux) in the extracted directory.
4.  Activate the virtual environment:
    *   **Windows:** `.\\venv\\Scripts\\Activate.ps1`
    *   **Linux:** `source venv/bin/activate`
5.  Test the SDK:
    ```python
    python -c "from sdk.blackbird_sdk_obfuscated import BlackBirdSDK; print('SDK loaded successfully!')"
    ```

**For Mac Systems (Apple Silicon + MLX):**

1.  Download the Mac package from the license server.
2.  Extract the ZIP file to your desired directory.
3.  Set up your Python environment:
    ```bash
    python -m venv blackbird_env
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
