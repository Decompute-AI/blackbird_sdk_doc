> **⚠️ IMPORTANT NOTES:**
>
> **Python Version Requirement**: This SDK is obfuscated and only works with Python 3.12.0, Using any other Python version will result in import or runtime errors. Verify your version with ```python --version``` before proceeding. 
>
> **Storage Space Requirement**: Ensure you have at least 19GB of available storage space on your system. This is necessary for downloading models, dependencies, and running the SDK efficiently. Insufficient space may cause installation failures or runtime issues.

## Features Enabled
- Inference File Upload
- Custom Agent Creation
- Web Search
- All Features

For detailed documentation, please see the [Blackbird SDK Documentation](./docs/index.md).
---

## Installation & Setup
Step 0: Create and Activate a Virtual Environment
macOS/Linux:

```bash
python3 -m venv venv             # Create virtual environment
source venv/bin/activate         # Activate it
```
Windows:
```cmd
python -m venv venv              # Create virtual environment
venv\Scripts\activate            # Activate it
```
Conda:
```bash
conda create -n blackbird_env python=3.12 -y  # Create Conda environment
conda activate blackbird_env                 # Activate it
```

### Step 1: Extract the ZIP file
```bash
# Extract this zip file to your desired location
unzip blackbird_sdk_enterprise.zip
cd blackbird_sdk_enterprise (
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


#### Install Pytorch 2.6.0 (Just for Windows Users)
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
export PYTHONPATH='blackbird_sdk:$PYTHONPATH'  
export PYTHONPATH='pyarmor_runtime_009116:$PYTHONPATH'

#Or if you are using a conda env you can also copy paste your folders to your site-packages
# stay in the blackbird_sdk_mac directory if not ( cd  to blackbird_sdk_mac)

echo $CONDA_PREFIX
cp -r blackbird_sdk $CONDA_PREFIX/lib/python3.12/site-packages/
cp -r pyarmor_runtime_009116 $CONDA_PREFIX/lib/python3.12/site-packages/
# Make sure pyarmor_runtime.so is in your site-package
cp pyarmor_runtime_009116/pyarmor_runtime.so $CONDA_PREFIX/lib/python3.12/site-packages/pyarmor_runtime_009116/


# Windows Command Prompt/Windows PowerShell
xcopy C:\path\to\your\project\blackbird_sdk %VIRTUAL_ENV%\Lib\site-packages\blackbird_sdk /s /e /h /y
xcopy C:\path\to\your\project\pyarmor_runtime_009116 %VIRTUAL_ENV%\Lib\site-packages\pyarmor_runtime_009116 /s /e /h /y
```


### Step 5: Set your Hugging Face token
Create a `.env` file inside your project folder, and add the following line:

```bash
# Replace your-huggingface-token with your actual Hugging Face access token.
HF_token=your-huggingface-token
```


### Step 6: Download Models
```bash
# In your project folder

# Download models for your project
python blackbird_sdk/utils/model_downloader.py
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


---

## File Structure
After extraction, your folder should look like this:
```
blackbird_sdk_mac/
|-- blackbird_sdk/          # Main SDK package (add this to your Python path)
|-- pyarmor_runtime_009116/ # Obfuscation runtime (required)
|-- requirements.txt        # Dependencies
|-- README.md              # This file
```

---

## Usage Examples

### Basic Usage
```python
import sys
import os
import shutil


# Add the parent directory to Python path so we can import blackbird_sdk
parent_dir = os.path.dirname(os.getcwd())  # Go up one level from blackbird_sdk
sys.path.insert(0, parent_dir)

from blackbird_sdk import BlackbirdSDK

if __name__ == "__main__":
    sdk = BlackbirdSDK()  
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
       sdk = BlackbirdSDK()
      
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
### Publish your agent to marketplace
```
#!/usr/bin/env python3
"""
Blackbird Agent Marketplace - Complete Usage Example

This example demonstrates how to:
1. Create custom agents
2. Publish them to the marketplace
3. Browse and search the marketplace
4. Load agents from the marketplace
5. Use marketplace agents

Prerequisites:
1. Start the marketplace server: python marketplace_server.py
2. Make sure BlackbirdSDK is installed with marketplace dependencies
"""

from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.builder import create_agent, AgentPersonality, AgentCapability
# Initialize SDK
sdk = BlackbirdSDK()
    
def example_create_and_publish_agent():
    """Example 1: Create and publish a custom agent."""
    print("=== Creating and Publishing a Custom Agent ===")
    
    
    # Create a custom data analysis agent
    agent = create_agent(
        name="data_scientist_pro",
        description="Advanced data scientist specializing in statistical analysis, machine learning, and data visualization."
    ).personality(AgentPersonality.ANALYTICAL).with_capabilities([
        AgentCapability.FILE_PROCESSING,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.CALCULATIONS,
        AgentCapability.WEB_SEARCH
    ]).system_prompt(
        """You are an expert data scientist with deep knowledge in:
        - Statistical analysis and hypothesis testing
        - Machine learning algorithms and model selection
        - Data visualization and storytelling with data
        - Python libraries: pandas, numpy, scikit-learn, matplotlib, seaborn
        - R programming for statistical computing
        
        Provide detailed, accurate analysis with proper statistical reasoning.
        Always explain your methodology and assumptions clearly.
        """
    ).temperature(0.3).build(sdk)
    
    # Deploy the agent locally first
    sdk.deploy_custom_agent(agent)
    print(f"✅ Agent '{agent.config.name}' created and deployed locally")
    
    # Test the agent
    response = sdk.send_message_to_custom_agent(
        "data_scientist_pro", 
        "Explain the difference between Type I and Type II errors in hypothesis testing."
    )
    # Fix the slice error - ensure response is a string
    response_text = str(response) if response is not None else "No response"
    print(f"🤖 Agent response: {response_text[:200]}...")
    
    # Publish to marketplace
    try:
        result = agent.publish_to_marketplace(
            author="data_expert_123",
            display_name="Data Scientist Pro",
            category="Data Science",
            tags=["data-science", "statistics", "machine-learning", "analysis"],
            version="1.0.0"
        )
        print(f"🎉 Successfully published to marketplace! Agent ID: {result['agent']['id']}")
        return True
    except Exception as e:
        print(f"❌ Failed to publish: {e}")
        return False

def example_browse_marketplace():
    """Example 2: Browse available agents in the marketplace."""
    print("\n=== Browsing the Marketplace ===")
    
    
    try:
        # Browse all agents
        agents = sdk.browse_marketplace()
        print(f"📋 Found {len(agents)} agents in the marketplace:")
        
        for agent in agents:
            print(f"\n🤖 {agent.display_name} (v{agent.version})")
            print(f"   Author: {agent.author}")
            print(f"   Category: {agent.category}")
            print(f"   Description: {agent.description}")
            print(f"   Downloads: {agent.download_count} | Rating: {agent.rating}/5")
            if agent.is_featured:
                print("   ⭐ Featured Agent")
            if agent.tags:
                print(f"   Tags: {', '.join(agent.tags)}")
                
    except Exception as e:
        print(f"❌ Failed to browse marketplace: {e}")

def example_search_marketplace():
    """Example 3: Search for specific types of agents."""
    print("\n=== Searching the Marketplace ===")
    
    # sdk = BlackbirdSDK()
    
    search_queries = ["finance", "code", "data"]
    
    for query in search_queries:
        try:
            print(f"\n🔍 Searching for: '{query}'")
            results = sdk.search_marketplace(query)
            
            if results:
                print(f"   Found {len(results)} matching agents:")
                for agent in results:
                    print(f"   • {agent.display_name} by {agent.author}")
            else:
                print("   No agents found")
                
        except Exception as e:
            print(f"❌ Search failed for '{query}': {e}")

def example_load_and_use_marketplace_agent():
    """Example 4: Load an agent from marketplace and use it."""
    print("\n=== Loading Agent from Marketplace ===")
    
    # sdk = BlackbirdSDK()
    
    try:
        # Load a financial advisor agent from marketplace
        print("📥 Loading 'financial_advisor' from marketplace...")
        agent = sdk.load_agent_from_marketplace('financial_advisor')
        print(f"✅ Loaded and deployed agent: {agent.config.display_name if hasattr(agent.config, 'display_name') else agent.config.name}")
        
        # Use the agent
        test_questions = [
            "What are the key factors to consider when building an investment portfolio?",
            "Explain the difference between stocks and bonds",
            "What is dollar-cost averaging and when should I use it?"
        ]
        
        print("\n💬 Testing the agent:")
        for question in test_questions:
            print(f"\n❓ Question: {question}")
            try:
                response = sdk.send_message_to_custom_agent('financial_advisor', question)
                # Fix the response handling
                response_text = str(response) if response is not None else "No response received"
                print(f"🤖 Response: {response_text[:300]}...")
            except Exception as e:
                print(f"❌ Error: {e}")
                
    except Exception as e:
        print(f"❌ Failed to load agent: {e}")

def example_create_specialized_agent():
    """Example 5: Create a specialized agent for a specific domain."""
    print("\n=== Creating and Publishing a Custom Agent ===")
    
    # sdk = BlackbirdSDK()
    
    # Create a marketing specialist agent
    marketing_agent = create_agent(
        name="data_scientist_pro",
        description="Advanced data scientist specializing in statistical analysis, machine learning, and data visualization."
    ).personality(AgentPersonality.ANALYTICAL).with_capabilities([
        AgentCapability.FILE_PROCESSING,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.CALCULATIONS,
        AgentCapability.WEB_SEARCH
    ]).system_prompt(
        """You are an expert data scientist with deep knowledge in:
        - Statistical analysis and hypothesis testing
        - Machine learning algorithms and model selection
        - Data visualization and storytelling with data
        - Python libraries: pandas, numpy, scikit-learn, matplotlib, seaborn
        - R programming for statistical computing
        
        Provide detailed, accurate analysis with proper statistical reasoning.
        Always explain your methodology and assumptions clearly.
        """
    ).temperature(0.3).build(sdk)
    
    # Deploy and test
    sdk.deploy_custom_agent(marketing_agent)
    print("✅ Agent 'data_scientist_pro' created and deployed locally")
    
    # Test the agent
    response = sdk.send_message_to_custom_agent(
        "data_scientist_pro",
        "Explain the difference between Type I and Type II errors in hypothesis testing."
    )
    # Fix the slice error here too
    response_text = str(response) if response is not None else "No response"
    print(f"🤖 Agent response: {response_text[:400]}...")
    
    # Publish to marketplace
    try:
        # Publish to marketplace using configurable URL
        result = marketing_agent.publish_to_marketplace(
            author="test_user",
            display_name="Test Agent",
            category="Testing",
            tags=["test", "demo"],
            version="1.0.0",
            marketplace_url='https://marketplace-blackbird.vercel.app/'  # Use configurable URL
        )
        print(f"🎉 Agent published! ID: {result['agent']['id']}")
    except Exception as e:
        print(f"❌ Example failed: {e}")

def main():
    """Run all examples."""
    print("🚀 Blackbird Agent Marketplace Example")
    print("=" * 50)
    
    # Check if marketplace is running
    
    try:
        from blackbird_sdk.marketplace.client import MarketplaceClient
        client = MarketplaceClient()
        if not client.health_check():
            print("❌ Marketplace server is not running!")
            print("Please start it with: python marketplace_server.py")
            return
        print("✅ Marketplace server is running")
    except Exception as e:
        print(f"❌ Cannot connect to marketplace: {e}")
        print("Please make sure the marketplace server is running")
        return
    
    # Run examples
    try:
        example_browse_marketplace()
        example_search_marketplace()
        example_load_and_use_marketplace_agent()
        example_create_and_publish_agent()
        example_create_specialized_agent()
        
        print("\n🎉 All examples completed successfully!")
        print("\nNext steps:")
        print("1. Visit to see the marketplace web interface")
        print("2. Create your own custom agents and publish them")
        print("3. Explore agents created by other users")
        
    except KeyboardInterrupt:
        print("\n👋 Example interrupted by user")
    except Exception as e:
        print(f"\n❌ Example failed: {e}")

if __name__ == "__main__":
    main() 
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
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.builder import (
   create_agent, AgentPersonality, AgentCapability
)


def test_agent_with_web_search():
   print("🚀 Testing Custom Agent with Web Search Capability")
   print("=" * 60)
   try:
       sdk = BlackbirdSDK()
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
Join the Discord server for help: [⁠Decompute⁠ help-📒](https://discord.com/channels/1278905687358832700/1294007046219497474)


---

## Important Notes

- This SDK build is **obfuscated** 
- Features are enforced at runtime based on your license blob
- The `pyarmor_runtime_009116` folder must remain in the same directory as `blackbird_sdk`
- Use the exact import: `from blackbird_sdk import BlackbirdSDK`

**Welcome to BlackBird SDK!**
