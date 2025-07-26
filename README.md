# BlackBird SDK - Enterprize Edition

> **⚠️ IMPORTANT NOTES:**
>
> **Python Version Requirement**: This SDK is obfuscated and only works with Python 3.12. Using any other Python version will result in import or runtime errors. Verify your version with ```python --version``` before proceeding.
>
> **Storage Space Requirement**: Ensure you have at least 35GB of available storage space on your system. This is necessary for downloading models, dependencies, and running the SDK efficiently. Insufficient space may cause installation failures or runtime issues.

## Features Enabled
- Inference File Upload
- Custom Agent Creation
- Web Search
- All Features

For detailed documentation, please see the [Blackbird SDK Documentation](./docs/index.md).
---

## Installation & Setup

### Step 1: Extract the ZIP file
```bash
# Extract this zip file to your desired location
unzip blackbird_sdk_enterprise.zip
cd blackbird_sdk_enterprise
```

### Step 2: Install Dependencies with pip (Python=3.12)

#### Install Basic Dependencies
```bash
# Install required dependencies
pip install -r requirements_windows.txt // for windows

pip install -r requirements_mac.txt // for mac
```

#### Install Pyjwt
```bash
# Install Pyjwt
pip install --force-reinstall --upgrade PyJWT
```


#### Install Pytorch 2.6.0
```bash
# Install Pytorch
pip install torch==2.6.0+cu124 torchvision==0.21.0+cu124 torchaudio==2.6.0+cu124 --index-url https://download.pytorch.org/whl/cu124
```


### Step 3: Set Up Your License Blob
```bash
# Linux/Mac
export BLACKBIRD_LICENSE_BLOB="your-license-blob-jwt-token-here"

# Windows Command Prompt
set BLACKBIRD_LICENSE_BLOB=your-license-blob-jwt-token-here

# Windows PowerShell
$env:BLACKBIRD_LICENSE_BLOB="your-license-blob-jwt-token-here"
```


### Step 4: Install Blackbird SDK and Pyarmor into your venv
```bash
# Linux/Mac
cp -r /path/to/your/project/blackbird_sdk $VIRTUAL_ENV/lib/python3.12/site-packages/
cp -r /path/to/your/project/pyarmor_runtime_009116 $VIRTUAL_ENV/lib/python3.12/site-packages/
# Make sure pyarmor_runtime.so is in your site-package
cp /path/to/your/project/pyarmor_runtime_009116/pyarmor_runtime.so $VIRTUAL_ENV/lib/python3.12/site-packages/pyarmor_runtime_009116/


# Windows Command Prompt/Windows PowerShell
xcopy C:\path\to\your\project\blackbird_sdk %VIRTUAL_ENV%\Lib\site-packages\blackbird_sdk /s /e /h /y
xcopy C:\path\to\your\project\pyarmor_runtime_009116 %VIRTUAL_ENV%\Lib\site-packages\pyarmor_runtime_009116 /s /e /h /y
```


### Step 5: Download Models
```bash
# In your project folder
cd blackbird_sdk\utils

# Download models for your project
python model_downloader.py
```

### Step 6: Set your Hugging Face token
Create a `.env` file inside your project folder, and add the following line:

```bash
# Replace your-huggingface-token with your actual Hugging Face access token.
HF_token=your-huggingface-token
```

### Step 7: Test the SDK
```python
import sys
import os

# Add the SDK to your Python path
sys.path.insert(0, os.path.join(os.getcwd(), "blackbird_sdk"))

from blackbird_sdk import BlackbirdSDK

# Initialize SDK (will prompt for license if not configured)
sdk = BlackbirdSDK()
print("SDK initialized successfully!")
```

### Step 8: Run Installation Test (Recommended)
```bash
python test_sdk_installation.py
```

This test will:
- Verify folder structure is correct
- Test SDK imports
- Check license configuration
- Validate PyArmor runtime files
- Guide you through license setup if needed

---

## File Structure
After extraction, your folder should look like this:
```
blackbird_sdk_unlimited/
|-- blackbird_sdk/          # Main SDK package (add this to your Python path)
|-- pyarmor_runtime_009116/ # Obfuscation runtime (required)
|-- requirements.txt        # Dependencies
|-- README.md              # This file
|-- test_sdk_installation.py # Installation test script
|-- .env.example           # Environment configuration template
`-- tier_config.json       # Tier configuration
```

---

## Usage Examples

### Basic Usage
```python
import sys
import os
import shutil

# Clear the license cache
config_dir = os.path.expanduser("~/AppData/Local/BlackbirdSDK")
if os.path.exists(config_dir):
    shutil.rmtree(config_dir)
    print("✅ Cleared existing license configuration")

# Set the license blob directly (replace with your professional blob if needed)
license_blob = "your-licence-blob"
os.environ["BLACKBIRD_LICENSE_BLOB"] = license_blob
print("License blob set in environment!")

# Print and decode the JWT
try:
    import jwt
    payload = jwt.decode(license_blob, options={"verify_signature": False})
    print("Decoded JWT:", payload)
except Exception as e:
    print("JWT decode error:", e)

# Add the parent directory to Python path so we can import blackbird_sdk
parent_dir = os.path.dirname(os.getcwd())  # Go up one level from blackbird_sdk
sys.path.insert(0, parent_dir)

from blackbird_sdk import BlackbirdSDK

if __name__ == "__main__":
    sdk = BlackbirdSDK(development_mode=True)  # Will reuse the async backend if running
    sdk.initialize_agent("general")
    response = sdk.send_message("Hello, what is the weather today?")
    print("Chat response:", response)
```


### Custom Agent Creation (Professional+)
```python
#!/usr/bin/env python3
"""
Basic Custom Agent Creation Example
Demonstrates creating a simple custom agent with the Blackbird SDK
"""
import sys
import os


# Add the SDK to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../.."))
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.builder import (
   create_agent, AgentPersonality, AgentCapability
)


def create_basic_agent():
   """Create a basic custom agent."""
   print("🚀 Creating Basic Custom Agent")
   print("=" * 50)

   try:
       # Initialize SDK
       sdk = BlackbirdSDK(development_mode=True)

       # Create a simple customer support agent
       agent = (create_agent("customer_support", "Helpful customer service assistant")
           .personality(AgentPersonality.SUPPORTIVE)
           .system_prompt("""
               You are a helpful customer support representative.
               - Always be polite and professional
               - Listen to customer concerns carefully
               - Provide clear, step-by-step solutions
               - Escalate complex issues when necessary
           """)
           .with_capabilities([
               AgentCapability.EMAIL_INTEGRATION,
               AgentCapability.WEB_SEARCH
           ])
           .temperature(0.6)
           .max_tokens(2000)
           .instruction("tone", "Friendly and professional")
           .instruction("escalation", "Escalate technical issues to Level 2 support")
           .metadata("version", "1.0")
           .metadata("created_by", "Support Team")
           .build(sdk)
       )

       # Deploy the agent
       success = sdk.deploy_custom_agent(agent)

       if success:
           print("✅ Agent deployed successfully!")

           # Test the agent
           print("\n🧪 Testing Agent Response:")
           response = sdk.send_message_to_custom_agent(
               "customer_support",
               "Hello, I'm having trouble with my account login"
           )
           print(f"🤖 Agent Response: {response}")

           # Save agent configuration
           agent.save_config("customer_support_config.yaml")
           print("💾 Agent configuration saved to customer_support_config.yaml")

       return agent

   except Exception as e:
       print(f"❌ Error creating agent: {e}")
       import traceback
       traceback.print_exc()
       return None


if __name__ == "__main__":
   agent = create_basic_agent()
```

### Web Search Integration (Enterprise+)
```python
"""
Test: Custom Agent with Web Search Integration
Creates a custom agent with web search capability and tests chat with web_search enabled.
"""
import sys
import os
import re


# Add the SDK to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../.."))
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.builder import (
   create_agent, AgentPersonality, AgentCapability
)


def test_agent_with_web_search():
   print("🚀 Testing Custom Agent with Web Search Capability")
   print("=" * 60)
   try:
       sdk = BlackbirdSDK(development_mode=False)
       agent = (
           create_agent("websearch_support", "Web-augmented support agent")
           .personality(AgentPersonality.SUPPORTIVE)
           .system_prompt(
               """
               You are a helpful customer support representative with access to real-time web search.
               - Always be polite and professional
               - Use web search results to provide up-to-date information
               - Provide clear, step-by-step solutions
               """
           )
           .with_capabilities([
               AgentCapability.WEB_SEARCH
           ])
           .temperature(0.5)
           .max_tokens(1500)
           .instruction("tone", "Friendly and professional")
           .metadata("version", "1.1-websearch-test")
           .build(sdk)
       )
       success = sdk.deploy_custom_agent(agent)
       assert success, "Agent deployment failed!"
       print("✅ Agent deployed successfully!")
       # Test the agent with web_search enabled
       print("\n🧪 Testing Agent Web Search Response:")
       response = sdk.send_message_to_custom_agent(
           "websearch_support",
           "What are the latest AI trends in 2024?",
           extra_payload={"web_search": True}
       )
       # Handle response type (dict or str)
       if isinstance(response, dict):
           response_text = response.get("response", str(response))
       else:
           response_text = str(response)
       print(f"🤖 Agent Response: {response_text}")
       # Check that the response includes web search context (simple heuristic)
    #    assert re.search(r'(https?://|Source:|Web Search Results)', response_text, re.IGNORECASE), "Web search context not found in response!"
    #    print("✅ Web search context found in agent response!")
       # Save agent config
       agent.save_config("websearch_support_config.yaml")
       print("💾 Agent configuration saved to websearch_support_config.yaml")
       print("\n🎉 Test passed!")
   except Exception as e:
       print(f"❌ Test failed: {e}")
       raise


if __name__ == "__main__":
   test_agent_with_web_search()
```

---

## Troubleshooting

### Common Issues:

1. **"No module named 'blackbird_sdk'"**
   - Make sure you've added the correct path: `sys.path.insert(0, "path/to/blackbird_sdk")`
   - The path should point to the folder containing `__init__.py`

2. **"No license found"**
   - Run the license setup code from Step 3
   - Make sure your license blob is valid and not expired
   - Make sure that you have installed PyJWT and not jwt package in your virtual environment.
   - **Clear the existing license cache and decode with jwt as shown in the Basic Usage example:**
     ```python
     import os, shutil
     config_dir = os.path.expanduser("~/AppData/Local/BlackbirdSDK")
     if os.path.exists(config_dir):
         shutil.rmtree(config_dir)
         print("✅ Cleared existing license configuration")
     # Decode your license blob
     import jwt
     payload = jwt.decode("your-license-blob", options={"verify_signature": False})
     print("Decoded JWT:", payload)
     ```
   - If this persists, refer to the fix below:
   **How to Fix (Force Remove All `jwt` Files):**
        1. **Manually Delete All `jwt` Folders in Your venv**

            1. Go to:
            ```
            path\to\your\venv\Lib\site-packages\
            ```
            2. **Delete the entire `jwt` folder** (and any `jwt-*.dist-info` folders).
            - Delete:
                - `jwt/`
                - `jwt-1.4.0.dist-info/` (if present)
                - `jwt-*.dist-info/` (any other jwt dist-info folders)

        2. **Reinstall PyJWT Cleanly**

        ```powershell
        pip install --force-reinstall --upgrade PyJWT
        ```

        3. **Verify the Correct Package is Installed**

        ```powershell
        python -c "import jwt; print(jwt.__file__); print(jwt.__version__)"
        ```
        - The path should end with `site-packages\\jwt\\__init__.py`
        - The version should be `2.x.x` (e.g., `2.8.0`)

        4. **Re-run your script**

        ```powershell
        python .\blackbird_sdk\basic_usage.py
        ```


        - The old `jwt` package leaves files behind that shadow the real `PyJWT`.
        - Deleting the `jwt` folder ensures only `PyJWT` is present.
        - After this, `import jwt` will refer to the correct package.


3. **"License validation failed"**
   - Check your internet connection (license server validation required)
   - Verify your license blob is correct
   - Contact support if the issue persists

4. **Import errors with obfuscated code**
   - Make sure `pyarmor_runtime_009116` folder is in the same directory
   - Don't move or rename the runtime folder

### Development Mode

You can run the SDK with `BlackbirdSDK(development_mode=True)` to see detailed logs.

### Virtual Environment Setup:
If using conda or venv:
```bash
# Option 1: Install in development mode
cd blackbird_sdk_unlimited
pip install -e ./blackbird_sdk

# Option 2: Copy to site-packages
cp -r blackbird_sdk $CONDA_PREFIX/lib/python*/site-packages/
cp -r pyarmor_runtime_009116 $CONDA_PREFIX/lib/python*/site-packages/
```

---

## Support

- **License Issues:** Contact your license provider
- **Technical Support:** Check the troubleshooting section above
- **Server URL:** https://9b683c5fbe39.ngrok-free.app

---

## Important Notes

- This SDK build is **obfuscated**
- Features are enforced at runtime based on your license blob
- The `pyarmor_runtime_009116` folder must remain in the same directory as `blackbird_sdk`
- Use the exact import: `from blackbird_sdk import BlackbirdSDK`

**Welcome to BlackBird SDK!**

<script>
document.querySelectorAll('pre > code').forEach(function (codeBlock) {
    var button = document.createElement('button');
    button.className = 'copy-code-button';
    button.type = 'button';
    button.innerText = 'Copy';

    button.addEventListener('click', function () {
        var code = codeBlock.innerText;
        var ta = document.createElement('textarea');
        ta.value = code;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        button.innerText = 'Copied!';
        setTimeout(function () {
            button.innerText = 'Copy';
        }, 2000);
    });

    var pre = codeBlock.parentNode;
    if (pre.parentNode.classList.contains('highlight')) {
        var highlight = pre.parentNode;
        highlight.parentNode.insertBefore(button, highlight);
    } else {
        pre.parentNode.insertBefore(button, pre);
    }
});
</script>
<style>
.copy-code-button {
    position: absolute;
    right: 4px;
    top: 4px;
    padding: 2px 6px;
    background: #eee;
    border: 1px solid #ddd;
    border-radius: 4px;
    cursor: pointer;
}
pre {
    position: relative;
}
</style>
