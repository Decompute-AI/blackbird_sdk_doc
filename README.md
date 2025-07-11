
# Blackbird SDK - Comprehensive Documentation

## Main SDK Documentation

### Blackbird SDK User Guide

# Blackbird SDK - Complete User Guide

## Overview

The Blackbird SDK is a comprehensive AI agent creation and management platform that enables developers to build, deploy, and manage custom AI agents with advanced capabilities including file processing, web search, function calling, and enterprise-grade features.

## Key Features

- **Custom AI Agent Creation** - Build specialized agents with unique personalities and capabilities
- **Multi-Modal File Processing** - Handle documents, spreadsheets, images, and more
- **Real-time Chat Interface** - Streaming responses with session management
- **Web Research Integration** - DuckDuckGo search and web scraping capabilities
- **Function Calling** - Calculator, calendar, and custom function integration
- **Enterprise Security** - Advanced licensing, quotas, and access controls
- **Backend Management** - Automatic backend deployment and scaling
- **Comprehensive Logging** - Structured logging and monitoring


## Installation \& Setup

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows, macOS, or Linux
- **Memory**: Minimum 4GB RAM (8GB+ recommended)
- **Storage**: 2GB+ free space for models and cache
- **Network**: Internet connection for model downloads and web features


### Installation Steps

#### 1. Environment Setup

```bash
# Create virtual environment
python -m venv blackbird_env

# Activate environment
# Windows:
blackbird_env\Scripts\activate
# macOS/Linux:
source blackbird_env/bin/activate

# Upgrade pip
python -m pip install --upgrade pip
```


#### 2. Install Blackbird SDK

```bash
# Install from source (development)
git clone https://github.com/blackbird/blackbird-sdk.git
cd blackbird-sdk
pip install -e .

# Or install from PyPI (when available)
pip install blackbird-sdk
```


#### 3. Verify Installation

```python
# Test basic import
python -c "from blackbird_sdk import BlackbirdSDK; print('✅ Installation successful')"

# Check version
python -c "import blackbird_sdk; print(f'Version: {blackbird_sdk.__version__}')"
```


### Quick Start

#### Basic Usage Example

```python
from blackbird_sdk import BlackbirdSDK

# Initialize SDK
sdk = BlackbirdSDK(development_mode=True)

# Initialize an agent
sdk.initialize_agent("finance")

# Send a message
response = sdk.send_message("What are the current market trends?")
print(response)

# Clean up
sdk.cleanup()
```


#### Advanced Setup with Configuration

```python
from blackbird_sdk import BlackbirdSDK

# Custom configuration
config = {
    'backend_port': 5012,
    'log_level': 'INFO',
    'max_sessions': 100,
    'timeout': 300
}

# Initialize with custom settings
sdk = BlackbirdSDK(
    config=config,
    development_mode=False,
    user_logging=True,
    structured_logging=True
)

# Initialize with specific model
sdk.initialize_agent("finance", model="unsloth/Qwen3-1.7B-bnb-4bit")

# Start interactive session
response = sdk.send_message("Hello! I need help with financial analysis.")
print(f"Agent Response: {response}")
```


## Feature-Specific Documentation

### 1. Agent Creation \& Management

# Agent Creation \& Management Documentation

## Overview

The Blackbird SDK provides a powerful agent creation system that allows users to build custom AI agents with specific personalities, capabilities, and behaviors tailored to their needs.

## Core Concepts

### Agent Components

- **Agent Config**: Configuration defining agent behavior and capabilities
- **Personality**: Predefined communication styles (Professional, Friendly, Analytical, etc.)
- **Capabilities**: Specific features the agent can use (File Processing, Web Search, etc.)
- **Custom Functions**: User-defined functions the agent can execute
- **System Prompts**: Instructions that guide agent behavior


### Agent Types

#### Pre-built Agents

- **General**: Basic conversational agent
- **Finance**: Financial analysis and calculations
- **Legal**: Legal document analysis and research
- **Tech**: Code review and technical support
- **Research**: Web research and data analysis
- **Image Generator**: Image creation and editing


## Creating Custom Agents

### Method 1: Builder Pattern

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability
from blackbird_sdk.creation.builder import create_agent

# Initialize SDK
sdk = BlackbirdSDK(development_mode=True)

# Create custom agent using builder pattern
agent = (create_agent("financial_advisor", "Personal financial planning assistant")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""
        You are a certified financial advisor with expertise in:
        - Personal investment strategies
        - Retirement planning
        - Risk assessment
        - Portfolio optimization
        
        Always provide evidence-based recommendations and include risk disclaimers.
    """)
    .with_capabilities([
        AgentCapability.FILE_PROCESSING,
        AgentCapability.CALCULATIONS,
        AgentCapability.WEB_SEARCH,
        AgentCapability.DATA_ANALYSIS
    ])
    .temperature(0.3)  # More focused responses
    .max_tokens(3000)
    .file_types(['.xlsx', '.csv', '.pdf'])
    .instruction("analysis_format", "Provide numerical analysis with clear explanations")
    .instruction("risk_disclosure", "Always include appropriate risk warnings")
    .metadata("version", "1.0")
    .metadata("created_by", "Financial Team")
    .build(sdk)
)

# Deploy the agent
success = sdk.deploy_custom_agent(agent)
if success:
    print("✅ Financial advisor agent deployed!")
```


### Method 2: Template-Based Creation

```python
# List available templates
templates = sdk.get_agent_templates()
print(f"Available templates: {templates}")

# Create from template and customize
agent = (sdk.create_agent_from_template("financial_analyst")
    .name("my_financial_analyst")
    .instruction("focus_areas", "Cryptocurrency and emerging markets")
    .instruction("reporting_style", "Executive summary with detailed appendix")
    .temperature(0.2)
    .build(sdk)
)

# Deploy and test
sdk.deploy_custom_agent(agent)
response = sdk.send_message_to_custom_agent(
    "my_financial_analyst", 
    "Analyze Bitcoin's recent performance"
)
```


### Method 3: Configuration File

```yaml
# financial_agent_config.yaml
name: financial_advisor
description: Advanced financial planning assistant
personality: analytical
system_prompt: |
  You are a financial advisor specializing in:
  - Investment portfolio analysis
  - Risk assessment and management
  - Financial planning strategies
  
  Provide detailed, data-driven recommendations.
capabilities:
  - file_processing
  - calculations
  - web_search
  - data_analysis
temperature: 0.3
max_tokens: 3000
file_types:
  - .xlsx
  - .csv
  - .pdf
custom_instructions:
  analysis_format: "Include charts and numerical data"
  risk_assessment: "Always mention risk factors"
metadata:
  version: "2.0"
  department: "Finance"
```

```python
# Load agent from file
agent = sdk.load_custom_agent("financial_agent_config.yaml")
sdk.deploy_custom_agent(agent)
```


## Adding Custom Functions

### Basic Custom Functions

```python
def calculate_compound_interest(principal: float, rate: float, years: int) -> dict:
    """Calculate compound interest with detailed breakdown."""
    amount = principal * (1 + rate/100) ** years
    interest = amount - principal
    
    return {
        "principal": principal,
        "rate": rate,
        "years": years,
        "final_amount": round(amount, 2),
        "total_interest": round(interest, 2),
        "growth_percentage": round((interest/principal) * 100, 2)
    }

def portfolio_risk_analysis(allocations: dict) -> dict:
    """Analyze portfolio risk based on asset allocations."""
    risk_scores = {
        "stocks": 0.8,
        "bonds": 0.3,
        "cash": 0.0,
        "crypto": 1.0,
        "real_estate": 0.6
    }
    
    total_weight = sum(allocations.values())
    weighted_risk = sum(
        (weight / total_weight) * risk_scores.get(asset, 0.5)
        for asset, weight in allocations.items()
    )
    
    return {
        "overall_risk_score": round(weighted_risk, 2),
        "risk_level": "High" if weighted_risk > 0.7 else "Medium" if weighted_risk > 0.4 else "Low",
        "recommendations": "Consider diversification" if weighted_risk > 0.8 else "Well balanced"
    }

# Create agent with custom functions
agent = (create_agent("investment_advisor", "Investment analysis specialist")
    .with_functions([calculate_compound_interest, portfolio_risk_analysis])
    .system_prompt("""
        You have access to specialized financial calculation tools:
        - calculate_compound_interest: For growth projections
        - portfolio_risk_analysis: For risk assessment
        
        Use these tools to provide accurate financial analysis.
    """)
    .build(sdk)
)
```


## Agent Management

### Deployment and Testing

```python
# Deploy custom agent
success = sdk.deploy_custom_agent(agent)

if success:
    # Test the agent
    test_queries = [
        "Calculate compound interest on $10,000 at 7% for 10 years",
        "Analyze risk for portfolio: 60% stocks, 30% bonds, 10% cash",
        "What investment strategy do you recommend for retirement planning?"
    ]
    
    for query in test_queries:
        response = sdk.send_message_to_custom_agent(agent.config.name, query)
        print(f"Query: {query}")
        print(f"Response: {response}\n")

# Save agent configuration
agent.save_config("investment_advisor_config.yaml")
```


### Agent Lifecycle Management

```python
# List deployed agents
if hasattr(sdk, 'custom_agents'):
    print("Deployed agents:")
    for name, agent in sdk.custom_agents.items():
        print(f"  - {name}: {agent.config.description}")

# Get agent information
agent_info = {
    'name': agent.config.name,
    'description': agent.config.description,
    'personality': agent.config.personality,
    'capabilities': [cap.value for cap in agent.config.capabilities],
    'temperature': agent.config.temperature,
    'max_tokens': agent.config.max_tokens
}
print(f"Agent Info: {agent_info}")

# Update agent configuration
agent.set_instruction("market_focus", "Focus on emerging market opportunities")
agent.enable_capability(AgentCapability.EMAIL_INTEGRATION)

# Remove agent
if 'investment_advisor' in sdk.custom_agents:
    del sdk.custom_agents['investment_advisor']
    print("Agent removed")
```


### 2. Chat Features

# Chat Features Documentation

## Overview

The Blackbird SDK provides comprehensive chat capabilities including real-time streaming, session management, conversation history, and multi-modal interactions.

## Core Chat Features

### Basic Chat Interface

```python
from blackbird_sdk import BlackbirdSDK

# Initialize SDK and agent
sdk = BlackbirdSDK(development_mode=True)
sdk.initialize_agent("general")

# Basic message sending
response = sdk.send_message("Hello! How can you help me today?")
print(f"Agent: {response}")

# Send follow-up message
response = sdk.send_message("Can you explain machine learning in simple terms?")
print(f"Agent: {response}")
```


### Streaming Chat

```python
# Real-time streaming responses
def on_chunk_received(chunk_text):
    """Handle each chunk as it arrives."""
    print(chunk_text, end='', flush=True)

def on_response_complete(full_response):
    """Handle complete response."""
    print(f"\n[Complete response received: {len(full_response)} characters]")

def on_error(error):
    """Handle streaming errors."""
    print(f"\nError: {error}")

# Send streaming message
sdk.send_message(
    "Explain the history of artificial intelligence",
    streaming=True,
    on_chunk=on_chunk_received,
    on_complete=on_response_complete,
    on_error=on_error
)
```


### Advanced Streaming with StreamingResponse

```python
from blackbird_sdk.session.streaming_response import StreamingResponse

# Create streaming response object
stream = sdk.stream_message("Write a detailed analysis of renewable energy trends")

# Add multiple chunk handlers
stream.on_chunk(lambda chunk: print(chunk, end=''))
stream.on_chunk(lambda chunk: save_to_log(chunk))

# Add completion handler
stream.on_complete(lambda response: process_final_response(response))

# Start streaming
stream.start()

# Get current response while streaming
current_text = stream.get_current_response()
print(f"Current length: {len(current_text)} characters")

# Wait for completion with timeout
try:
    final_response = stream.wait_for_completion(timeout=60)
    print(f"Final response: {len(final_response)} characters")
except TimeoutError:
    print("Stream timed out")
```


## Session Management

### Creating and Managing Sessions

```python
# Get session information
session_info = sdk.get_session_info()
print(f"Session ID: {session_info.get('session_id')}")
print(f"User ID: {session_info.get('user_id')}")

# Create new session with specific tier
session = sdk.session_manager.create_session(
    user_id="user123",
    tier="pro",
    metadata={"department": "research", "project": "ai_analysis"}
)

print(f"Session created: {session.session_id}")
```


### Conversation History

```python
# Get conversation history
history = sdk.get_response_history(limit=10)
for interaction in history:
    if interaction['role'] == 'user':
        print(f"You: {interaction['content']}")
    else:
        print(f"Agent: {interaction['content']}")

# Search through conversation history
search_results = sdk.search_responses("machine learning")
for result in search_results:
    print(f"Found: {result['response'][:100]}...")

# Export conversation history
export_file = sdk.export_chat_history(format='txt', output_path='my_chat.txt')
print(f"Chat history exported to: {export_file}")
```


## Interactive Chat Modes

### Terminal-Based Interactive Chat

```python
# Start interactive chat session
sdk.chat_interactive()

# This will start a terminal interface:
# 🤖 Interactive chat with general agent
# Type 'quit' to exit, 'clear' to clear history
# 
# 👤 You: Hello!
# 🤖 Agent: Hello! How can I help you today?
# 
# 👤 You: What's the weather like?
# 🤖 Agent: I don't have access to real-time weather data...
```


### Custom Interactive Chat

```python
def custom_chat_interface():
    """Custom chat interface with enhanced features."""
    print("🚀 Welcome to Blackbird Chat!")
    print("Commands: /help, /clear, /save, /load, /quit")
    
    while True:
        try:
            user_input = input("\n💬 You: ").strip()
            
            # Handle special commands
            if user_input.startswith('/'):
                command = user_input[1:].lower()
                
                if command == 'quit':
                    break
                elif command == 'clear':
                    sdk.clear_chat_history()
                    print("🗑️ Chat history cleared")
                elif command == 'save':
                    filename = f"chat_{int(time.time())}.txt"
                    sdk.export_chat_history(format='txt', output_path=filename)
                    print(f"💾 Chat saved to {filename}")
                elif command == 'help':
                    print("""
Available commands:
/quit - Exit chat
/clear - Clear chat history
/save - Save chat to file
/help - Show this help
                    """)
                continue
            
            if not user_input:
                continue
            
            # Send message with streaming
            print("🤖 Agent: ", end="")
            response = sdk.send_message(user_input, streaming=True)
            print() # New line after streaming
            
        except KeyboardInterrupt:
            print("\n👋 Chat ended by user")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")

# Run custom chat
custom_chat_interface()
```


## Multi-Agent Conversations

### Agent Switching

```python
# Initialize multiple agents
agents = ['general', 'finance', 'tech']

for agent_type in agents:
    sdk.initialize_agent(agent_type)
    print(f"✅ {agent_type} agent ready")

# Switch between agents during conversation
current_agent = 'general'
sdk.initialize_agent(current_agent)

def switch_agent(new_agent):
    global current_agent
    if new_agent in agents:
        sdk.initialize_agent(new_agent)
        current_agent = new_agent
        print(f"🔄 Switched to {new_agent} agent")
        return True
    return False

# Multi-agent conversation
messages = [
    ("general", "Hello! I need help with multiple topics."),
    ("finance", "What's the best investment strategy for beginners?"),
    ("tech", "Can you review this Python code: def factorial(n): return 1 if n <= 1 else n * factorial(n-1)"),
    ("general", "Thank you for all the help!")
]

for agent, message in messages:
    switch_agent(agent)
    response = sdk.send_message(message)
    print(f"[{agent.upper()}] {response}\n")
```


### Conversation Context Management

```python
# Maintain context across agent switches
class ContextualChatManager:
    def __init__(self, sdk):
        self.sdk = sdk
        self.conversation_context = []
        self.current_topic = None
    
    def send_contextual_message(self, message, agent_type=None):
        """Send message with conversation context."""
        if agent_type:
            self.sdk.initialize_agent(agent_type)
        
        # Build context-aware prompt
        context_prompt = self._build_context_prompt(message)
        
        response = self.sdk.send_message(context_prompt)
        
        # Store interaction
        self.conversation_context.append({
            'agent': agent_type or self.sdk.current_agent,
            'user_message': message,
            'agent_response': response,
            'timestamp': time.time()
        })
        
        return response
    
    def _build_context_prompt(self, message):
        """Build prompt with conversation context."""
        if len(self.conversation_context) > 0:
            recent_context = self.conversation_context[-3:]  # Last 3 interactions
            context_str = "\n".join([
                f"Previous: {ctx['user_message']} -> {ctx['agent_response'][:100]}..."
                for ctx in recent_context
            ])
            
            return f"""
Context from recent conversation:
{context_str}

Current message: {message}

Please respond considering the conversation context.
"""
        else:
            return message

# Usage
chat_manager = ContextualChatManager(sdk)

response1 = chat_manager.send_contextual_message(
    "I'm planning to start a tech company", 
    "general"
)

response2 = chat_manager.send_contextual_message(
    "What programming languages should my team focus on?", 
    "tech"
)

response3 = chat_manager.send_contextual_message(
    "How much initial funding will I need?", 
    "finance"
)
```


## Chat Customization

### Response Formatting

```python
# Custom response formatting
def format_response(response, agent_type):
    """Format agent responses with custom styling."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    
    formatted = f"""
┌─ {agent_type.upper()} AGENT [{timestamp}] ─┐
│ {response}
└─────────────────────────────────────────┘
"""
    return formatted

# Usage with custom formatting
agent_type = "finance"
sdk.initialize_agent(agent_type)
response = sdk.send_message("What are the benefits of diversified investing?")
formatted_response = format_response(response, agent_type)
print(formatted_response)
```


### Chat Analytics

```python
class ChatAnalytics:
    def __init__(self):
        self.metrics = {
            'total_messages': 0,
            'agent_usage': defaultdict(int),
            'response_times': [],
            'message_lengths': [],
            'topics_discussed': set()
        }
    
    def track_interaction(self, agent_type, message, response, response_time):
        """Track chat interaction metrics."""
        self.metrics['total_messages'] += 1
        self.metrics['agent_usage'][agent_type] += 1
        self.metrics['response_times'].append(response_time)
        self.metrics['message_lengths'].append(len(response))
        
        # Simple topic extraction (can be enhanced with NLP)
        keywords = ['finance', 'tech', 'legal', 'research', 'general']
        for keyword in keywords:
            if keyword.lower() in message.lower():
                self.metrics['topics_discussed'].add(keyword)
    
    def get_summary(self):
        """Get chat analytics summary."""
        if not self.metrics['response_times']:
            return "No data available"
        
        avg_response_time = sum(self.metrics['response_times']) / len(self.metrics['response_times'])
        avg_response_length = sum(self.metrics['message_lengths']) / len(self.metrics['message_lengths'])
        
        return f"""
Chat Analytics Summary:
─────────────────────
Total Messages: {self.metrics['total_messages']}
Average Response Time: {avg_response_time:.2f}s
Average Response Length: {avg_response_length:.0f} characters
Most Used Agent: {max(self.metrics['agent_usage'], key=self.metrics['agent_usage'].get)}
Topics Discussed: {', '.join(self.metrics['topics_discussed'])}
Agent Usage: {dict(self.metrics['agent_usage'])}
"""

# Usage
analytics = ChatAnalytics()

# Track interactions
start_time = time.time()
response = sdk.send_message("Explain blockchain technology")
end_time = time.time()

analytics.track_interaction(
    agent_type="tech",
    message="Explain blockchain technology",
    response=response,
    response_time=end_time - start_time
)

# Get analytics
print(analytics.get_summary())
```


### 3. File Management \& Processing

# File Management \& Processing Documentation

## Overview

The Blackbird SDK provides comprehensive file processing capabilities, supporting multiple document formats with intelligent parsing, analysis, and integration with AI agents.

## Supported File Types

### Document Formats

- **PDF**: Text extraction, OCR for scanned documents
- **Microsoft Office**: .docx, .xlsx, .pptx
- **Text Files**: .txt, .md, .csv, .json, .yaml
- **Images**: .jpg, .png, .gif, .bmp, .tiff
- **Audio**: .wav, .mp3, .m4a, .flac


### File Processing Features

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.data_pipeline.file_service import FileService

# Initialize SDK with file processing capabilities
sdk = BlackbirdSDK(development_mode=True)
sdk.initialize_agent("finance")  # Use finance agent for document analysis

# Get file service
file_service = FileService()
```


## Single File Processing

### Basic File Upload and Analysis

```python
# Process a single PDF document
file_path = r"C:\Users\Administrator\Downloads\AWS2024 SEC\annual_report.pdf"

# Method 1: Direct file processing with agent
response = sdk.chat_service.send_message_with_files(
    message="Please analyze this SEC filing and provide key financial insights",
    files=[file_path],
    options={'agent': 'finance', 'model': 'unsloth/Qwen3-1.7B-bnb-4bit'}
)

print("Analysis Results:")
print(response)
```


### Advanced File Processing

```python
# Process with specific instructions
processing_instructions = """
Please analyze this document and provide:
1. Executive summary
2. Key financial metrics
3. Risk factors identified
4. Recommendations for investors
5. Comparison with industry standards
"""

response = sdk.chat_service.send_message_with_files(
    message=processing_instructions,
    files=[file_path],
    options={
        'agent': 'finance',
        'model': 'unsloth/Qwen3-1.7B-bnb-4bit',
        'temperature': 0.3,  # More focused analysis
        'max_tokens': 4000   # Longer responses
    }
)
```


### File Type Specific Processing

```python
def process_by_file_type(file_path):
    """Process file based on its type."""
    file_extension = Path(file_path).suffix.lower()
    
    if file_extension == '.pdf':
        return process_pdf_document(file_path)
    elif file_extension in ['.xlsx', '.csv']:
        return process_spreadsheet(file_path)
    elif file_extension == '.docx':
        return process_word_document(file_path)
    elif file_extension in ['.jpg', '.png']:
        return process_image(file_path)
    else:
        return f"Unsupported file type: {file_extension}"

def process_pdf_document(file_path):
    """Specialized PDF processing."""
    message = """
    Please analyze this PDF document and provide:
    - Document structure and sections
    - Key information extracted
    - Summary of main points
    - Any data tables or figures identified
    """
    
    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={'agent': 'research'}
    )

def process_spreadsheet(file_path):
    """Specialized spreadsheet processing."""
    message = """
    Please analyze this spreadsheet and provide:
    - Data summary and statistics
    - Key trends and patterns
    - Any anomalies or notable findings
    - Recommendations based on the data
    """
    
    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={'agent': 'finance'}
    )

# Usage
file_path = "financial_data.xlsx"
result = process_by_file_type(file_path)
print(result)
```


## Multiple File Processing

### Batch File Processing

```python
# Process multiple files simultaneously
file_paths = [
    r"C:\Users\Administrator\Downloads\AWS2024 SEC\annual_report.pdf",
    r"C:\Users\Administrator\Downloads\Amazon SEC Filing 2023\quarterly_report.pdf"
]

# Compare multiple documents
comparison_message = """
Please compare these SEC filings and provide:
1. Key differences in financial performance
2. Changes in business strategy
3. Risk factor evolution
4. Investment recommendation based on comparison
"""

response = sdk.chat_service.send_message_with_files(
    message=comparison_message,
    files=file_paths,
    options={
        'agent': 'finance',
        'model': 'unsloth/Qwen3-1.7B-bnb-4bit',
        'temperature': 0.2  # More consistent analysis
    }
)

print("Comparative Analysis:")
print(response)
```


### Directory Processing

```python
import os
from pathlib import Path

def process_directory(directory_path, file_extensions=None):
    """Process all files in a directory."""
    if file_extensions is None:
        file_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    
    files_to_process = []
    
    # Find all supported files
    for file_path in Path(directory_path).rglob('*'):
        if file_path.suffix.lower() in file_extensions:
            files_to_process.append(str(file_path))
    
    print(f"Found {len(files_to_process)} files to process")
    
    # Process files in batches
    batch_size = 5
    results = []
    
    for i in range(0, len(files_to_process), batch_size):
        batch = files_to_process[i:i+batch_size]
        
        batch_message = f"""
        Please analyze this batch of documents ({len(batch)} files) and provide:
        1. Summary of each document
        2. Common themes across documents
        3. Key insights from the collection
        4. Overall conclusions
        """
        
        batch_result = sdk.chat_service.send_message_with_files(
            message=batch_message,
            files=batch,
            options={'agent': 'research'}
        )
        
        results.append({
            'batch_number': i // batch_size + 1,
            'files': batch,
            'analysis': batch_result
        })
    
    return results

# Usage
directory_path = r"C:\Users\Administrator\Downloads\financial_documents"
results = process_directory(directory_path)

for result in results:
    print(f"\n--- Batch {result['batch_number']} ---")
    print(f"Files: {[Path(f).name for f in result['files']]}")
    print(f"Analysis: {result['analysis'][:200]}...")
```


## Advanced File Processing

### OCR and Image Processing

```python
def process_scanned_document(file_path):
    """Process scanned documents with OCR."""
    message = """
    This appears to be a scanned document. Please:
    1. Extract all text using OCR
    2. Identify the document type and structure
    3. Extract key information and data
    4. Provide a summary of contents
    """
    
    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={
            'agent': 'research',
            'enable_ocr': True  # Enable OCR processing
        }
    )

# Process image with text
image_path = "scanned_invoice.jpg"
result = process_scanned_document(image_path)
print(result)
```


### Structured Data Extraction

```python
def extract_structured_data(file_path, schema):
    """Extract structured data according to a schema."""
    schema_prompt = f"""
    Please extract data from this document according to this schema:
    {json.dumps(schema, indent=2)}
    
    Return the extracted data in JSON format matching the schema structure.
    """
    
    return sdk.chat_service.send_message_with_files(
        message=schema_prompt,
        files=[file_path],
        options={'agent': 'research'}
    )

# Define extraction schema
financial_schema = {
    "company_name": "string",
    "reporting_period": "string",
    "revenue": "number",
    "net_income": "number",
    "total_assets": "number",
    "key_metrics": {
        "gross_margin": "percentage",
        "operating_margin": "percentage",
        "debt_to_equity": "ratio"
    },
    "risk_factors": ["array of strings"]
}

# Extract structured data
file_path = "annual_report.pdf"
extracted_data = extract_structured_data(file_path, financial_schema)
print("Extracted Data:", extracted_data)
```


## File Management Utilities

### File Organization

```python
class FileOrganizer:
    def __init__(self, sdk):
        self.sdk = sdk
        self.processed_files = {}
    
    def organize_by_content(self, files):
        """Organize files by their content type."""
        categories = {
            'financial': [],
            'legal': [],
            'technical': [],
            'research': [],
            'other': []
        }
        
        for file_path in files:
            category = self.classify_file_content(file_path)
            categories[category].append(file_path)
        
        return categories
    
    def classify_file_content(self, file_path):
        """Classify file content."""
        classification_message = """
        Please classify this document into one of these categories:
        - financial: Financial reports, statements, analysis
        - legal: Contracts, legal documents, compliance
        - technical: Technical specifications, code, manuals
        - research: Research papers, studies, analysis
        - other: General documents
        
        Respond with just the category name.
        """
        
        response = self.sdk.chat_service.send_message_with_files(
            message=classification_message,
            files=[file_path],
            options={'agent': 'general'}
        )
        
        return response.strip().lower()

# Usage
organizer = FileOrganizer(sdk)
files = [
    "annual_report.pdf",
    "contract.docx",
    "api_documentation.pdf",
    "research_paper.pdf"
]

organized = organizer.organize_by_content(files)
print("File Organization:", organized)
```


### File Processing Pipeline

```python
class FileProcessingPipeline:
    def __init__(self, sdk):
        self.sdk = sdk
        self.processing_steps = []
    
    def add_step(self, step_name, agent_type, instructions):
        """Add a processing step to the pipeline."""
        self.processing_steps.append({
            'name': step_name,
            'agent': agent_type,
            'instructions': instructions
        })
    
    def process_file(self, file_path):
        """Process file through the pipeline."""
        results = {}
        
        for step in self.processing_steps:
            print(f"Executing step: {step['name']}")
            
            self.sdk.initialize_agent(step['agent'])
            
            result = self.sdk.chat_service.send_message_with_files(
                message=step['instructions'],
                files=[file_path],
                options={'agent': step['agent']}
            )
            
            results[step['name']] = result
        
        return results

# Create processing pipeline
pipeline = FileProcessingPipeline(sdk)

# Add processing steps
pipeline.add_step(
    'content_extraction',
    'general',
    'Extract and summarize the main content of this document.'
)

pipeline.add_step(
    'financial_analysis',
    'finance',
    'Analyze any financial data or metrics in this document.'
)

pipeline.add_step(
    'risk_assessment',
    'legal',
    'Identify any risks, compliance issues, or legal concerns.'
)

# Process file through pipeline
file_path = "company_report.pdf"
results = pipeline.process_file(file_path)

for step_name, result in results.items():
    print(f"\n--- {step_name.upper()} ---")
    print(result[:300] + "..." if len(result) > 300 else result)
```


## Integration with Agents

### Specialized Document Agents

```python
# Create specialized document analysis agent
from blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability

document_analyzer = (create_agent("document_analyzer", "Specialized document analysis agent")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""
        You are a document analysis specialist with expertise in:
        - Extracting key information from various document types
        - Identifying document structure and organization
        - Summarizing complex documents
        - Finding specific data points and metrics
        - Comparing multiple documents
        
        Always provide structured, detailed analysis.
    """)
    .with_capabilities([
        AgentCapability.FILE_PROCESSING,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.WEB_SEARCH
    ])
    .temperature(0.2)
    .max_tokens(4000)
    .file_types(['.pdf', '.docx', '.xlsx', '.txt', '.csv'])
    .instruction("output_format", "Provide structured analysis with clear sections")
    .instruction("detail_level", "Include specific page numbers and data points")
    .build(sdk)
)

# Deploy and use the specialized agent
sdk.deploy_custom_agent(document_analyzer)

# Use for complex document analysis
complex_analysis = sdk.send_message_to_custom_agent(
    "document_analyzer",
    "Please provide a comprehensive analysis of the uploaded documents."
)
```


### File Processing with Custom Functions

```python
def extract_financial_metrics(file_path):
    """Custom function to extract financial metrics."""
    # This would integrate with specialized libraries
    # like pandas, openpyxl, or pdfplumber
    return {
        "revenue": "1.2B",
        "net_income": "150M",
        "growth_rate": "15%"
    }

# Create agent with custom file processing functions
file_agent = (create_agent("file_processor", "Advanced file processing agent")
    .with_functions([extract_financial_metrics])
    .system_prompt("""
        You have access to specialized file processing functions.
        Use these tools to provide detailed analysis of uploaded documents.
    """)
    .build(sdk)
)
```


### 4. Session Management

# Session Management Documentation

## Overview

The Blackbird SDK includes a comprehensive session management system that handles user sessions, quotas, rate limiting, and usage tracking for enterprise-grade applications.

## Core Session Features

### Session Creation and Management

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.session.session_types import QuotaType, RateLimitType

# Initialize SDK
sdk = BlackbirdSDK(development_mode=True)

# Create user session with specific tier
session = sdk.session_manager.create_session(
    user_id="user123",
    tier="pro",  # Options: free, basic, pro, enterprise
    metadata={
        "department": "research",
        "project": "ai_analysis",
        "created_by": "admin"
    }
)

print(f"Session created: {session.session_id}")
print(f"User ID: {session.user_id}")
print(f"Status: {session.status}")
```


### Session Information and Status

```python
# Get session details
session_data = sdk.session_manager.get_session_data(session.session_id)
print(f"Session Data: {session_data}")

# Check session status
session = sdk.session_manager.get_session(session.session_id)
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
# Get all quotas for a session
quotas = sdk.session_manager.get_quota(session.session_id)
print("Current Quotas:")
for quota_type, info in quotas.items():
    print(f"  {quota_type}:")
    print(f"    Used: {info['used']}/{info['limit']}")
    print(f"    Remaining: {info['remaining']}")
    print(f"    Usage: {info['usage_percentage']:.1f}%")

# Get specific quota
api_quota = sdk.session_manager.get_quota(session.session_id, QuotaType.API_CALLS)
print(f"API Calls: {api_quota}")
```


### Quota Usage Tracking

```python
# Track usage for different operations
def track_operation_usage(session_id, operation_name, resource_type, amount):
    """Track resource usage for an operation."""
    try:
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
        return False

# Track different types of usage
track_operation_usage(session.session_id, "send_message", QuotaType.API_CALLS, 1)
track_operation_usage(session.session_id, "file_upload", QuotaType.STORAGE, 1024)  # 1KB
track_operation_usage(session.session_id, "ai_inference", QuotaType.TOKENS, 150)
```


### Custom Quota Handlers

```python
class QuotaManager:
    def __init__(self, sdk):
        self.sdk = sdk
        self.usage_callbacks = []
    
    def add_usage_callback(self, callback):
        """Add callback for usage events."""
        self.usage_callbacks.append(callback)
        self.sdk.session_manager.add_usage_callback(callback)
    
    def check_quota_status(self, session_id):
        """Check if any quotas are near limits."""
        quotas = self.sdk.session_manager.get_quota(session_id)
        warnings = []
        
        for quota_type, info in quotas.items():
            usage_pct = info['usage_percentage']
            if usage_pct >= 90:
                warnings.append(f"{quota_type}: {usage_pct:.1f}% used")
            elif usage_pct >= 75:
                warnings.append(f"{quota_type}: {usage_pct:.1f}% used (warning)")
        
        return warnings
    
    def predict_quota_exhaustion(self, session_id):
        """Predict when quotas might be exhausted."""
        # Get usage history
        session_obj = self.sdk.session_manager.get_session(session_id)
        if not session_obj:
            return {}
        
        usage_history = self.sdk.session_manager.get_usage_history(
            session_obj.user_id, 
            limit=100
        )
        
        # Simple prediction based on recent usage patterns
        # In production, this could use more sophisticated algorithms
        predictions = {}
        
        for quota_type, quota_info in self.sdk.session_manager.get_quota(session_id).items():
            remaining = quota_info['remaining']
            if remaining > 0:
                # Calculate average usage rate
                recent_usage = [
                    record for record in usage_history 
                    if record['resource_type'] == quota_type
                ]
                
                if recent_usage:
                    avg_rate = len(recent_usage) / len(usage_history) if usage_history else 0
                    if avg_rate > 0:
                        time_to_exhaustion = remaining / avg_rate
                        predictions[quota_type] = {
                            'time_to_exhaustion_hours': time_to_exhaustion,
                            'predicted_exhaustion': time.time() + (time_to_exhaustion * 3600)
                        }
        
        return predictions

# Usage
quota_manager = QuotaManager(sdk)

# Add usage callback
def usage_alert(usage_record):
    print(f"🔔 Usage Alert: {usage_record.operation} used {usage_record.amount} {usage_record.resource_type.value}")

quota_manager.add_usage_callback(usage_alert)

# Check quota status
warnings = quota_manager.check_quota_status(session.session_id)
for warning in warnings:
    print(f"⚠️ Quota Warning: {warning}")
```


## Rate Limiting

### Rate Limit Enforcement

```python
# Enforce rate limits for operations
def safe_api_call(session_id, operation_func, *args, **kwargs):
    """Make API call with rate limiting."""
    try:
        # Check rate limit before operation
        sdk.session_manager.enforce_rate_limit(
            session_id=session_id,
            operation="api_call",
            limit_type=RateLimitType.PER_MINUTE
        )
        
        # Perform the operation
        result = operation_func(*args, **kwargs)
        
        # Track usage
        sdk.session_manager.track_usage(
            session_id=session_id,
            operation="api_call",
            resource_type=QuotaType.API_CALLS,
            amount=1
        )
        
        return result
        
    except RateLimitError as e:
        print(f"⏱️ Rate limit exceeded: {e.message}")
        if e.retry_after:
            print(f"   Retry after: {e.retry_after:.1f} seconds")
        raise

# Usage with rate limiting
def send_message_with_limits(session_id, message):
    """Send message with rate limiting."""
    return safe_api_call(
        session_id,
        lambda: sdk.send_message(message)
    )

# Test rate limiting
try:
    for i in range(10):
        response = send_message_with_limits(session.session_id, f"Test message {i}")
        print(f"Message {i}: Success")
        time.sleep(0.1)  # Small delay
        
except RateLimitError as e:
    print(f"Rate limit hit: {e}")
```


### Custom Rate Limiting

```python
class CustomRateLimiter:
    def __init__(self, sdk):
        self.sdk = sdk
        self.custom_limits = {}
    
    def set_custom_limit(self, session_id, operation, max_calls, time_window):
        """Set custom rate limit for specific operation."""
        if session_id not in self.custom_limits:
            self.custom_limits[session_id] = {}
        
        self.custom_limits[session_id][operation] = {
            'max_calls': max_calls,
            'time_window': time_window,
            'calls': [],
            'last_reset': time.time()
        }
    
    def check_custom_limit(self, session_id, operation):
        """Check if custom rate limit allows operation."""
        if session_id not in self.custom_limits:
            return True
        
        if operation not in self.custom_limits[session_id]:
            return True
        
        limit_info = self.custom_limits[session_id][operation]
        current_time = time.time()
        
        # Reset if time window passed
        if current_time - limit_info['last_reset'] > limit_info['time_window']:
            limit_info['calls'] = []
            limit_info['last_reset'] = current_time
        
        # Clean old calls outside time window
        limit_info['calls'] = [
            call_time for call_time in limit_info['calls']
            if current_time - call_time < limit_info['time_window']
        ]
        
        # Check limit
        if len(limit_info['calls']) >= limit_info['max_calls']:
            return False
        
        # Record this call
        limit_info['calls'].append(current_time)
        return True

# Usage
rate_limiter = CustomRateLimiter(sdk)

# Set custom limits
rate_limiter.set_custom_limit(session.session_id, "file_upload", 5, 60)  # 5 per minute
rate_limiter.set_custom_limit(session.session_id, "ai_inference", 20, 3600)  # 20 per hour

# Check before operations
if rate_limiter.check_custom_limit(session.session_id, "file_upload"):
    print("File upload allowed")
else:
    print("File upload rate limit exceeded")
```


## Concurrency Management

### Managing Concurrent Operations

```python
# Manage concurrent operations
def with_concurrency_control(session_id, operation_name):
    """Decorator for concurrency control."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                # Increment concurrent operations
                sdk.session_manager.manage_concurrency(
                    session_id=session_id,
                    operation=operation_name,
                    increment=True
                )
                
                # Execute operation
                result = func(*args, **kwargs)
                
                return result
                
            finally:
                # Decrement concurrent operations
                sdk.session_manager.manage_concurrency(
                    session_id=session_id,
                    operation=operation_name,
                    increment=False
                )
        
        return wrapper
    return decorator

# Usage
@with_concurrency_control(session.session_id, "file_processing")
def process_large_file(file_path):
    """Process large file with concurrency control."""
    print(f"Processing {file_path}...")
    time.sleep(2)  # Simulate processing time
    return f"Processed {file_path}"

# Test concurrency limits
import threading

def worker(file_id):
    try:
        result = process_large_file(f"file_{file_id}.txt")
        print(f"Worker {file_id}: {result}")
    except RateLimitError as e:
        print(f"Worker {file_id}: Concurrency limit exceeded")

# Start multiple workers
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

# Wait for completion
for thread in threads:
    thread.join()
```


## Session Analytics and Monitoring

### Usage Analytics

```python
class SessionAnalytics:
    def __init__(self, sdk):
        self.sdk = sdk
    
    def get_user_analytics(self, user_id):
        """Get comprehensive analytics for a user."""
        # Get user sessions
        sessions = self.sdk.session_manager.get_user_sessions(user_id)
        
        # Get usage history
        usage_history = self.sdk.session_manager.get_usage_history(user_id, limit=1000)
        
        # Calculate analytics
        total_sessions = len(sessions)
        active_sessions = len([s for s in sessions if s.is_active])
        
        # Usage by operation
        operation_counts = {}
        resource_usage = {}
        
        for record in usage_history:
            op = record['operation']
            resource = record['resource_type']
            amount = record['amount']
            
            operation_counts[op] = operation_counts.get(op, 0) + 1
            resource_usage[resource] = resource_usage.get(resource, 0) + amount
        
        return {
            'user_id': user_id,
            'total_sessions': total_sessions,
            'active_sessions': active_sessions,
            'total_operations': len(usage_history),
            'operation_breakdown': operation_counts,
            'resource_usage': resource_usage,
            'most_used_operation': max(operation_counts, key=operation_counts.get) if operation_counts else None
        }
    
    def get_system_analytics(self):
        """Get system-wide analytics."""
        stats = self.sdk.session_manager.get_statistics()
        
        return {
            'system_stats': stats,
            'timestamp': time.time()
        }

# Usage
analytics = SessionAnalytics(sdk)

# Get user analytics
user_analytics = analytics.get_user_analytics("user123")
print("User Analytics:")
print(json.dumps(user_analytics, indent=2))

# Get system analytics
system_analytics = analytics.get_system_analytics()
print("System Analytics:")
print(json.dumps(system_analytics, indent=2))
```


### Real-time Monitoring

```python
class SessionMonitor:
    def __init__(self, sdk):
        self.sdk = sdk
        self.monitoring = False
        self.alerts = []
    
    def start_monitoring(self):
        """Start real-time session monitoring."""
        self.monitoring = True
        
        def monitor_loop():
            while self.monitoring:
                try:
                    self.check_system_health()
                    time.sleep(30)  # Check every 30 seconds
                except Exception as e:
                    print(f"Monitoring error: {e}")
        
        monitor_thread = threading.Thread(target=monitor_loop, daemon=True)
        monitor_thread.start()
        print("📊 Session monitoring started")
    
    def check_system_health(self):
        """Check system health and generate alerts."""
        stats = self.sdk.session_manager.get_statistics()
        
        # Check for high session count
        if stats['active_sessions'] > 100:
            self.add_alert(f"High session count: {stats['active_sessions']}")
        
        # Check session distribution
        if stats['average_sessions_per_user'] > 5:
            self.add_alert(f"High sessions per user: {stats['average_sessions_per_user']:.1f}")
    
    def add_alert(self, message):
        """Add monitoring alert."""
        alert = {
            'timestamp': time.time(),
            'message': message
        }
        self.alerts.append(alert)
        print(f"🚨 Alert: {message}")
    
    def get_alerts(self, last_n=10):
        """Get recent alerts."""
        return self.alerts[-last_n:]

# Usage
monitor = SessionMonitor(sdk)
monitor.start_monitoring()

# Get alerts after some time
time.sleep(5)
alerts = monitor.get_alerts()
for alert in alerts:
    print(f"Alert: {alert['message']}")
```


### 5. Web Research \& Search

# Web Research \& Search Documentation

## Overview

The Blackbird SDK includes comprehensive web research capabilities with DuckDuckGo search integration, web scraping, content processing, and intelligent research workflows.

## Core Search Features

### Basic Web Search

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.utils.web_search import WebSearchBackend
from blackbird_sdk.web_research_pipeline.enhanced_search_manager import EnhancedSearchManager

# Initialize SDK with web search capabilities
sdk = BlackbirdSDK(development_mode=True)
sdk.initialize_agent("research")

# Initialize web search backend
web_search = WebSearchBackend()

# Basic search functionality
search_results = web_search.search(
    query="artificial intelligence trends 2024",
    max_results=10
)

print(f"Found {len(search_results)} results:")
for i, result in enumerate(search_results, 1):
    print(f"{i}. {result.get('title', 'No title')}")
    print(f"   URL: {result.get('url', 'No URL')}")
    print(f"   Snippet: {result.get('snippet', 'No snippet')[:100]}...")
    print()
```


### Agent-Integrated Search

```python
# Search with agent processing
def search_with_agent(query, agent_type="research"):
    """Search and process results with AI agent."""
    sdk.initialize_agent(agent_type)
    
    # Perform search
    search_results = web_search.search(query, max_results=5)
    
    # Process results with agent
    search_summary = "\n".join([
        f"Title: {result.get('title', 'No title')}\n"
        f"URL: {result.get('url', 'No URL')}\n"
        f"Content: {result.get('snippet', 'No snippet')}\n"
        for result in search_results
    ])
    
    analysis_prompt = f"""
    Please analyze these search results for the query: "{query}"
    
    Search Results:
    {search_summary}
    
    Provide:
    1. Summary of key findings
    2. Main themes and trends
    3. Most reliable sources
    4. Additional research recommendations
    """
    
    response = sdk.send_message(analysis_prompt)
    
    return {
        'query': query,
        'raw_results': search_results,
        'agent_analysis': response
    }

# Usage
research_result = search_with_agent("quantum computing breakthroughs 2024")
print("Agent Analysis:")
print(research_result['agent_analysis'])
```


## Advanced Web Research

### Enhanced Search Manager

```python
# Initialize enhanced search manager
search_manager = EnhancedSearchManager()

# Configure search parameters
search_config = {
    'max_results_per_source': 5,
    'enable_content_extraction': True,
    'filter_duplicates': True,
    'quality_threshold': 0.7
}

# Comprehensive research query
research_query = "renewable energy storage solutions market analysis"

# Perform enhanced search
enhanced_results = search_manager.comprehensive_search(
    query=research_query,
    config=search_config
)

print(f"Enhanced search found {len(enhanced_results)} high-quality results")
for result in enhanced_results:
    print(f"Title: {result['title']}")
    print(f"Source: {result['source']}")
    print(f"Quality Score: {result.get('quality_score', 'N/A')}")
    print(f"Content Preview: {result['content'][:200]}...")
    print("---")
```


### Multi-Source Research

```python
class MultiSourceResearcher:
    def __init__(self, sdk):
        self.sdk = sdk
        self.search_manager = EnhancedSearchManager()
    
    def research_topic(self, topic, search_depth="medium"):
        """Conduct comprehensive research on a topic."""
        print(f"🔍 Researching: {topic}")
        
        # Define search strategies based on depth
        search_strategies = {
            "basic": {
                "queries": [topic],
                "max_results": 10
            },
            "medium": {
                "queries": [
                    topic,
                    f"{topic} latest developments",
                    f"{topic} market analysis",
                    f"{topic} future trends"
                ],
                "max_results": 20
            },
            "deep": {
                "queries": [
                    topic,
                    f"{topic} comprehensive analysis",
                    f"{topic} expert opinions",
                    f"{topic} case studies",
                    f"{topic} research papers",
                    f"{topic} industry reports"
                ],
                "max_results": 50
            }
        }
        
        strategy = search_strategies.get(search_depth, search_strategies["medium"])
        all_results = []
        
        # Execute searches
        for query in strategy["queries"]:
            print(f"  Searching: {query}")
            results = self.search_manager.search(
                query=query,
                max_results=strategy["max_results"] // len(strategy["queries"])
            )
            all_results.extend(results)
        
        # Remove duplicates and filter quality
        unique_results = self._deduplicate_results(all_results)
        quality_results = self._filter_by_quality(unique_results)
        
        # Analyze with AI agent
        self.sdk.initialize_agent("research")
        analysis = self._analyze_results(topic, quality_results)
        
        return {
            'topic': topic,
            'search_depth': search_depth,
            'total_sources': len(quality_results),
            'raw_results': quality_results,
            'analysis': analysis
        }
    
    def _deduplicate_results(self, results):
        """Remove duplicate results."""
        seen_urls = set()
        unique_results = []
        
        for result in results:
            url = result.get('url', '')
            if url and url not in seen_urls:
                seen_urls.add(url)
                unique_results.append(result)
        
        return unique_results
    
    def _filter_by_quality(self, results, min_quality=0.6):
        """Filter results by quality score."""
        return [
            result for result in results
            if result.get('quality_score', 0.5) >= min_quality
        ]
    
    def _analyze_results(self, topic, results):
        """Analyze search results with AI agent."""
        results_summary = "\n\n".join([
            f"Source {i+1}:\n"
            f"Title: {result.get('title', 'No title')}\n"
            f"URL: {result.get('url', 'No URL')}\n"
            f"Content: {result.get('content', result.get('snippet', 'No content'))[:300]}..."
            for i, result in enumerate(results[:10])  # Limit to top 10 for analysis
        ])
        
        analysis_prompt = f"""
        Please provide a comprehensive analysis of this research on "{topic}".
        
        Based on the following sources:
        {results_summary}
        
        Provide:
        1. Executive Summary (3-4 sentences)
        2. Key Findings (bullet points)
        3. Current Trends and Developments
        4. Market Analysis (if applicable)
        5. Future Outlook
        6. Source Quality Assessment
        7. Research Gaps Identified
        8. Recommendations for Further Research
        
        Ensure the analysis is objective and cite specific sources where relevant.
        """
        
        return self.sdk.send_message(analysis_prompt)

# Usage
researcher = MultiSourceResearcher(sdk)

# Conduct research with different depths
basic_research = researcher.research_topic("electric vehicle batteries", "basic")
print("Basic Research Results:")
print(basic_research['analysis'][:500] + "...")

deep_research = researcher.research_topic("artificial intelligence in healthcare", "deep")
print("\nDeep Research Results:")
print(deep_research['analysis'][:500] + "...")
```


## Specialized Search Features

### News and Current Events

```python
def search_latest_news(topic, time_filter="week"):
    """Search for latest news on a topic."""
    time_filters = {
        "day": "past 24 hours",
        "week": "past week", 
        "month": "past month"
    }
    
    news_query = f"{topic} news {time_filters.get(time_filter, 'recent')}"
    
    # Search for news
    news_results = web_search.get_latest_news(
        topic=topic,
        max_results=10
    )
    
    # Process with agent
    sdk.initialize_agent("research")
    
    news_summary = "\n".join([
        f"Headline: {article.get('title', 'No title')}\n"
        f"Source: {article.get('source', 'Unknown')}\n"
        f"Published: {article.get('published_date', 'Unknown')}\n"
        f"Summary: {article.get('summary', article.get('snippet', 'No summary'))}\n"
        for article in news_results
    ])
    
    news_analysis = sdk.send_message(f"""
    Please analyze these recent news articles about "{topic}":
    
    {news_summary}
    
    Provide:
    1. Key developments and breaking news
    2. Impact analysis
    3. Trend identification
    4. Credibility assessment of sources
    5. Implications and next steps to watch
    """)
    
    return {
        'topic': topic,
        'time_filter': time_filter,
        'articles': news_results,
        'analysis': news_analysis
    }

# Usage
news_analysis = search_latest_news("artificial intelligence regulation", "week")
print("Latest AI Regulation News:")
print(news_analysis['analysis'])
```


### Academic and Research Sources

```python
def search_academic_sources(topic, source_types=None):
    """Search for academic and research sources."""
    if source_types is None:
        source_types = ['research papers', 'academic studies', 'peer reviewed']
    
    academic_queries = [
        f"{topic} {source_type}" for source_type in source_types
    ]
    
    # Add site-specific searches for academic sources
    academic_sites = [
        "site:arxiv.org",
        "site:scholar.google.com", 
        "site:pubmed.ncbi.nlm.nih.gov",
        "site:ieee.org",
        "site:acm.org"
    ]
    
    all_results = []
    
    for query in academic_queries:
        # General academic search
        results = web_search.search(f"{query} academic research", max_results=5)
        all_results.extend(results)
        
        # Site-specific searches
        for site in academic_sites:
            site_results = web_search.search(f"{query} {site}", max_results=2)
            all_results.extend(site_results)
    
    # Filter and analyze academic sources
    sdk.initialize_agent("research")
    
    academic_analysis = sdk.send_message(f"""
    Please analyze these academic sources on "{topic}":
    
    {json.dumps([{
        'title': r.get('title', ''),
        'url': r.get('url', ''),
        'snippet': r.get('snippet', '')
    } for r in all_results[:15]], indent=2)}
    
    Provide:
    1. Quality and credibility assessment
    2. Key research findings
    3. Methodology analysis
    4. Research gaps identified
    5. Consensus vs. conflicting findings
    6. Recommendations for practitioners
    """)
    
    return {
        'topic': topic,
        'academic_sources': all_results,
        'analysis': academic_analysis
    }

# Usage
academic_research = search_academic_sources("machine learning bias detection")
print("Academic Research Analysis:")
print(academic_research['analysis'])
```


## Web Content Processing

### Content Extraction and Analysis

```python
from blackbird_sdk.utils.web_scraper import WebScraper

class WebContentProcessor:
    def __init__(self, sdk):
        self.sdk = sdk
        self.scraper = WebScraper()
    
    def extract_and_analyze_content(self, urls, analysis_type="summary"):
        """Extract content from URLs and analyze."""
        extracted_content = []
        
        for url in urls:
            try:
                print(f"Extracting content from: {url}")
                content = self.scraper.extract_content(url)
                extracted_content.append({
                    'url': url,
                    'title': content.get('title', 'No title'),
                    'content': content.get('content', ''),
                    'metadata': content.get('metadata', {})
                })
            except Exception as e:
                print(f"Failed to extract from {url}: {e}")
        
        # Analyze content with agent
        self.sdk.initialize_agent("research")
        
        analysis_prompts = {
            "summary": "Provide a comprehensive summary of the key points from all sources.",
            "comparison": "Compare and contrast the different perspectives and findings.",
            "synthesis": "Synthesize the information into key insights and conclusions.",
            "fact_check": "Identify factual claims and assess their credibility."
        }
        
        prompt = analysis_prompts.get(analysis_type, analysis_prompts["summary"])
        
        content_text = "\n\n".join([
            f"Source: {item['title']}\nURL: {item['url']}\n{item['content'][:1000]}..."
            for item in extracted_content
        ])
        
        analysis = self.sdk.send_message(f"""
        {prompt}
        
        Source Content:
        {content_text}
        """)
        
        return {
            'urls': urls,
            'extracted_content': extracted_content,
            'analysis_type': analysis_type,
            'analysis': analysis
        }

# Usage
processor = WebContentProcessor(sdk)

urls = [
    "https://example.com/ai-trends-2024",
    "https://example.com/machine-learning-advances",
    "https://example.com/ai-ethics-guidelines"
]

content_analysis = processor.extract_and_analyze_content(
    urls, 
    analysis_type="synthesis"
)
print("Content Synthesis:")
print(content_analysis['analysis'])
```


### Automated Research Workflows

```python
class AutomatedResearcher:
    def __init__(self, sdk):
        self.sdk = sdk
        self.search_manager = EnhancedSearchManager()
        self.content_processor = WebContentProcessor(sdk)
    
    def comprehensive_research_workflow(self, topic, output_format="report"):
        """Execute a comprehensive research workflow."""
        print(f"🔬 Starting comprehensive research on: {topic}")
        
        workflow_steps = []
        
        # Step 1: Initial search and overview
        print("Step 1: Initial topic search...")
        initial_search = self.search_manager.search(topic, max_results=10)
        workflow_steps.append(("initial_search", initial_search))
        
        # Step 2: News and current developments
        print("Step 2: Current news and developments...")
        news_results = search_latest_news(topic, "month")
        workflow_steps.append(("news_analysis", news_results))
        
        # Step 3: Academic and research sources
        print("Step 3: Academic sources...")
        academic_results = search_academic_sources(topic)
        workflow_steps.append(("academic_research", academic_results))
        
        # Step 4: Deep content analysis
        print("Step 4: Deep content analysis...")
        top_urls = [result.get('url') for result in initial_search[:5] if result.get('url')]
        content_analysis = self.content_processor.extract_and_analyze_content(
            top_urls, 
            "synthesis"
        )
        workflow_steps.append(("content_analysis", content_analysis))
        
        # Step 5: Final synthesis
        print("Step 5: Final synthesis...")
        final_report = self._generate_final_report(topic, workflow_steps, output_format)
        
        return {
            'topic': topic,
            'workflow_steps': workflow_steps,
            'final_report': final_report,
            'metadata': {
                'total_sources': len(initial_search) + len(news_results.get('articles', [])) + len(academic_results.get('academic_sources', [])),
                'research_date': time.time(),
                'output_format': output_format
            }
        }
    
    def _generate_final_report(self, topic, workflow_steps, output_format):
        """Generate final research report."""
        self.sdk.initialize_agent("research")
        
        # Compile all analyses
        all_analyses = []
        for step_name, step_data in workflow_steps:
            if isinstance(step_data, dict) and 'analysis' in step_data:
                all_analyses.append(f"{step_name.upper()}:\n{step_data['analysis']}")
        
        combined_analysis = "\n\n".join(all_analyses)
        
        format_instructions = {
            "report": "Generate a comprehensive research report with executive summary, detailed findings, and recommendations.",
            "briefing": "Create a concise executive briefing with key points and actionable insights.",
            "presentation": "Structure as presentation slides with main points and supporting data.",
            "summary": "Provide a clear, accessible summary for general audiences."
        }
        
        format_instruction = format_instructions.get(output_format, format_instructions["report"])
        
        final_prompt = f"""
        Based on comprehensive research on "{topic}", {format_instruction}
        
        Research Data:
        {combined_analysis}
        
        Structure your response appropriately for the {output_format} format.
        Include citations and source references where applicable.
        """
        
        return self.sdk.send_message(final_prompt)

# Usage
automated_researcher = AutomatedResearcher(sdk)

# Execute comprehensive research workflow
research_results = automated_researcher.comprehensive_research_workflow(
    "sustainable energy transition challenges",
    output_format="report"
)

print("Comprehensive Research Report:")
print(research_results['final_report'])

# Save results
with open(f"research_report_{int(time.time())}.txt", "w") as f:
    f.write(research_results['final_report'])
print("Research report saved to file.")
```


## Integration with Agents

### Search-Enhanced Agents

```python
# Create agent with web search capabilities
from blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability

def create_web_search_function():
    """Create custom web search function for agents."""
    def web_search_tool(query: str, max_results: int = 5) -> dict:
        """Search the web and return results."""
        search_backend = WebSearchBackend()
        results = search_backend.search(query, max_results=max_results)
        
        return {
            'query': query,
            'results_count': len(results),
            'results': results[:max_results]
        }
    
    return web_search_tool

# Create research agent with web search
research_agent = (create_agent("web_researcher", "AI agent with web search capabilities")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""
        You are a research specialist with access to web search capabilities.
        You can search the internet for current information using the web_search_tool function.
        
        When users ask for current information, use the search tool to find up-to-date data.
        Always cite your sources and indicate when information comes from web searches.
    """)
    .with_capabilities([
        AgentCapability.WEB_SEARCH,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.DOCUMENT_CREATION
    ])
    .with_functions([create_web_search_function()])
    .temperature(0.4)
    .build(sdk)
)

# Deploy and test
sdk.deploy_custom_agent(research_agent)

# Test web search integration
response = sdk.send_message_to_custom_agent(
    "web_researcher",
    "What are the latest developments in quantum computing? Please search for current information."
)
print("Web-Enhanced Agent Response:")
print(response)
```


### 6. Function Integrations

# Function Integrations Documentation

## Overview

The Blackbird SDK provides a comprehensive function calling system that enables agents to interact with external tools, APIs, and services automatically based on user queries.

## Core Integration Features

### Calculator Integration

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.integrations.calculator import Calculator

# Initialize SDK and calculator
sdk = BlackbirdSDK(development_mode=True)
calculator = Calculator()

# Initialize finance agent (which has calculator integration)
sdk.initialize_agent("finance")

# Test basic calculations
test_calculations = [
    "15 + 25 * 2",
    "sqrt(144)",
    "sin(pi/2)", 
    "log(100)",
    "2^8",
    "factorial(5)"
]

print("🧮 Testing Calculator Functions:")
for expression in test_calculations:
    try:
        result = calculator.calculate(expression)
        print(f"✅ {expression} = {result}")
    except Exception as e:
        print(f"❌ {expression} failed: {e}")
```


### Advanced Financial Calculations

```python
class FinancialCalculator:
    def __init__(self):
        self.calculator = Calculator()
    
    def compound_interest(self, principal, rate, years, compounds_per_year=1):
        """Calculate compound interest."""
        expression = f"{principal} * (1 + {rate/100}/{compounds_per_year})^({compounds_per_year}*{years})"
        final_amount = self.calculator.calculate(expression)
        interest_earned = final_amount - principal
        
        return {
            "principal": principal,
            "rate": rate,
            "years": years,
            "compounds_per_year": compounds_per_year,
            "final_amount": round(final_amount, 2),
            "interest_earned": round(interest_earned, 2),
            "total_return_percentage": round((interest_earned / principal) * 100, 2)
        }
    
    def loan_payment(self, principal, annual_rate, years):
        """Calculate monthly loan payment."""
        monthly_rate = annual_rate / 100 / 12
        num_payments = years * 12
        
        if monthly_rate == 0:
            return principal / num_payments
        
        expression = f"{principal} * ({monthly_rate} * (1 + {monthly_rate})^{num_payments}) / ((1 + {monthly_rate})^{num_payments} - 1)"
        monthly_payment = self.calculator.calculate(expression)
        
        return {
            "loan_amount": principal,
            "annual_rate": annual_rate,
            "loan_term_years": years,
            "monthly_payment": round(monthly_payment, 2),
            "total_payments": round(monthly_payment * num_payments, 2),
            "total_interest": round(monthly_payment * num_payments - principal, 2)
        }

# Usage with agent integration
fin_calc = FinancialCalculator()

# Test with finance agent
sdk.initialize_agent("finance")

# Agent will automatically use calculator for financial queries
response = sdk.send_message("""
I have $10,000 to invest. If I can get 7% annual return compounded monthly, 
what will it be worth in 10 years? Please calculate: 10000 * (1.07/12)^(12*10)
""")

print("Finance Agent with Calculator:")
print(response)
```


### Calendar Integration

```python
from blackbird_sdk.integrations.calendar import CalendarManager
from datetime import datetime, timedelta

# Initialize calendar manager
calendar = CalendarManager()

# Test calendar operations
def test_calendar_functions():
    """Test calendar integration functions."""
    current_date = datetime.now()
    print(f"📅 Current date: {current_date.strftime('%Y-%m-%d %H:%M')}")
    
    # Calculate future dates
    future_date = current_date + timedelta(days=90)
    print(f"📅 Date in 90 days: {future_date.strftime('%Y-%m-%d')}")
    
    # Calculate business days
    business_days = calendar.calculate_business_days(
        start_date=current_date,
        end_date=future_date
    )
    print(f"📊 Business days in next 90 days: {business_days}")
    
    # Working days calculation
    working_days = calendar.get_working_days_between(
        start_date=current_date.date(),
        end_date=future_date.date()
    )
    print(f"💼 Working days: {working_days}")

test_calendar_functions()
```


### Agent-Integrated Calendar Usage

```python
# Test calendar integration with agents
sdk.initialize_agent("finance")

calendar_queries = [
    "I need to plan my quarterly financial review. Today is the start date, and I want to schedule it for 90 days from now. What date would that be?",
    "How many business days do I have to prepare for a presentation in 30 days?",
    "If I start a project today and need to complete it in 6 months, what's the deadline date?",
    "Calculate the number of working days between now and the end of this year."
]

print("📅 Testing Calendar Integration with Finance Agent:")
for query in calendar_queries:
    print(f"\nQuery: {query}")
    response = sdk.send_message(query)
    print(f"Response: {response}")
```


## Custom Function Creation

### Building Custom Functions

```python
def create_investment_analyzer():
    """Create custom investment analysis functions."""
    
    def analyze_portfolio_risk(allocations: dict, risk_factors: dict = None) -> dict:
        """Analyze portfolio risk based on asset allocations."""
        if risk_factors is None:
            risk_factors = {
                "stocks": 0.8,
                "bonds": 0.3,
                "cash": 0.0,
                "crypto": 1.0,
                "real_estate": 0.6,
                "commodities": 0.7
            }
        
        total_weight = sum(allocations.values())
        if total_weight == 0:
            return {"error": "No allocations provided"}
        
        weighted_risk = sum(
            (weight / total_weight) * risk_factors.get(asset, 0.5)
            for asset, weight in allocations.items()
        )
        
        risk_level = (
            "High" if weighted_risk > 0.7 else
            "Medium" if weighted_risk > 0.4 else
            "Low"
        )
        
        recommendations = []
        if weighted_risk > 0.8:
            recommendations.append("Consider reducing high-risk assets")
        if allocations.get("cash", 0) / total_weight > 0.3:
            recommendations.append("Consider investing excess cash")
        if len(allocations) < 3:
            recommendations.append("Increase diversification across asset classes")
        
        return {
            "overall_risk_score": round(weighted_risk, 3),
            "risk_level": risk_level,
            "asset_breakdown": allocations,
            "total_portfolio_value": total_weight,
            "recommendations": recommendations,
            "diversification_score": len(allocations) / 6.0  # Max 6 asset classes
        }
    
    def calculate_retirement_needs(current_age: int, retirement_age: int, 
                                 current_savings: float, monthly_expenses: float,
                                 inflation_rate: float = 0.03) -> dict:
        """Calculate retirement savings needs."""
        years_to_retirement = retirement_age - current_age
        years_in_retirement = max(85 - retirement_age, 20)  # Assume living to 85
        
        # Calculate future monthly expenses (adjusted for inflation)
        future_monthly_expenses = monthly_expenses * ((1 + inflation_rate) ** years_to_retirement)
        
        # Calculate total retirement needs
        total_retirement_needs = future_monthly_expenses * 12 * years_in_retirement
        
        # Calculate required monthly savings
        if years_to_retirement > 0:
            # Assuming 7% annual return
            monthly_return = 0.07 / 12
            num_payments = years_to_retirement * 12
            
            # Future value of current savings
            future_current_savings = current_savings * ((1 + monthly_return) ** num_payments)
            
            # Additional savings needed
            additional_needed = max(0, total_retirement_needs - future_current_savings)
            
            # Required monthly payment
            if additional_needed > 0 and monthly_return > 0:
                required_monthly_savings = additional_needed * monthly_return / (((1 + monthly_return) ** num_payments) - 1)
            else:
                required_monthly_savings = 0
        else:
            required_monthly_savings = 0
            additional_needed = max(0, total_retirement_needs - current_savings)
        
        return {
            "current_age": current_age,
            "retirement_age": retirement_age,
            "years_to_retirement": years_to_retirement,
            "current_savings": current_savings,
            "current_monthly_expenses": monthly_expenses,
            "future_monthly_expenses": round(future_monthly_expenses, 2),
            "total_retirement_needs": round(total_retirement_needs, 2),
            "required_monthly_savings": round(required_monthly_savings, 2),
            "savings_gap": round(additional_needed, 2),
            "on_track": additional_needed <= current_savings * 0.1  # Within 10%
        }
    
    return analyze_portfolio_risk, calculate_retirement_needs

# Create functions
portfolio_analyzer, retirement_calculator = create_investment_analyzer()

# Test functions directly
portfolio_test = portfolio_analyzer({
    "stocks": 6000,
    "bonds": 3000,
    "cash": 1000
})
print("Portfolio Analysis:")
print(json.dumps(portfolio_test, indent=2))

retirement_test = retirement_calculator(30, 65, 50000, 4000)
print("\nRetirement Analysis:")
print(json.dumps(retirement_test, indent=2))
```


### Creating Agents with Custom Functions

```python
from blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability

# Create financial advisor agent with custom functions
financial_advisor = (create_agent("advanced_financial_advisor", "Advanced financial planning specialist")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""
        You are an advanced financial advisor with access to specialized analysis tools:
        
        Available Functions:
        - analyze_portfolio_risk: Analyze portfolio risk and diversification
        - calculate_retirement_needs: Calculate retirement savings requirements
        
        Use these tools to provide detailed, data-driven financial advice.
        Always explain your calculations and provide clear recommendations.
    """)
    .with_capabilities([
        AgentCapability.CALCULATIONS,
        AgentCapability.DATA_ANALYSIS,
        AgentCapability.FILE_PROCESSING
    ])
    .with_functions([portfolio_analyzer, retirement_calculator])
    .temperature(0.3)
    .max_tokens(4000)
    .instruction("analysis_style", "Provide detailed numerical analysis with explanations")
    .instruction("recommendations", "Include specific, actionable recommendations")
    .build(sdk)
)

# Deploy and test the agent
sdk.deploy_custom_agent(financial_advisor)

# Test with complex financial queries
test_queries = [
    "I'm 35 years old with $75,000 saved for retirement. I spend $5,000 per month and want to retire at 65. Am I on track?",
    "Analyze my portfolio: 70% stocks ($70,000), 20% bonds ($20,000), 10% cash ($10,000). Is this appropriate for a 40-year-old?",
    "I have a portfolio worth $100,000 split between stocks (60%), real estate (25%), and crypto (15%). What's my risk level?"
]

for query in test_queries:
    print(f"\n🔍 Query: {query}")
    response = sdk.send_message_to_custom_agent("advanced_financial_advisor", query)
    print(f"💡 Response: {response}")
```


## API Integrations

### External API Function Wrapper

```python
import requests

class APIFunctionWrapper:
    """Wrapper for external API integrations."""
    
    def __init__(self, base_url, api_key=None):
        self.base_url = base_url
        self.headers = {}
        if api_key:
            self.headers['Authorization'] = f'Bearer {api_key}'
    
    def create_api_function(self, endpoint, method='GET', description=""):
        """Create a function that calls an external API."""
        
        def api_function(params=None, data=None):
            """Generated API function."""
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            
            try:
                if method.upper() == 'GET':
                    response = requests.get(url, params=params, headers=self.headers, timeout=30)
                elif method.upper() == 'POST':
                    response = requests.post(url, json=data, headers=self.headers, timeout=30)
                else:
                    raise ValueError(f"Unsupported method: {method}")
                
                response.raise_for_status()
                return response.json()
                
            except requests.RequestException as e:
                return {"error": f"API call failed: {str(e)}"}
        
        # Set function metadata
        api_function.__name__ = f"api_{endpoint.replace('/', '_').replace('-', '_')}"
        api_function.__doc__ = description or f"Call {endpoint} API endpoint"
        
        return api_function

# Example: Weather API integration
weather_api = APIFunctionWrapper("https://api.weather.example.com")

get_weather = weather_api.create_api_function(
    "weather/current",
    method='GET',
    description="Get current weather for a location"
)

get_forecast = weather_api.create_api_function(
    "weather/forecast",
    method='GET', 
    description="Get weather forecast for a location"
)

# Create agent with API functions
weather_agent = (create_agent("weather_assistant", "Weather information assistant")
    .personality(AgentPersonality.FRIENDLY)
    .system_prompt("""
        You are a weather assistant with access to current weather and forecast data.
        Use the available weather functions to provide accurate, up-to-date information.
    """)
    .with_functions([get_weather, get_forecast])
    .build(sdk)
)
```


## Function Registry Management

### Advanced Function Registry

```python
from blackbird_sdk.integrations.function_registry import FunctionRegistry

class AdvancedFunctionRegistry(FunctionRegistry):
    """Enhanced function registry with categories and metadata."""
    
    def __init__(self):
        super().__init__()
        self.function_categories = {}
        self.function_metadata = {}
    
    def register_function_with_metadata(self, func, category="general", 
                                      description="", usage_examples=None):
        """Register function with additional metadata."""
        self.register_function(func)
        
        func_name = func.__name__
        self.function_categories[func_name] = category
        self.function_metadata[func_name] = {
            "description": description,
            "usage_examples": usage_examples or [],
            "category": category,
            "parameters": self._extract_parameters(func)
        }
    
    def _extract_parameters(self, func):
        """Extract function parameters using inspection."""
        import inspect
        try:
            sig = inspect.signature(func)
            parameters = {}
            for name, param in sig.parameters.items():
                parameters[name] = {
                    "type": str(param.annotation) if param.annotation != inspect.Parameter.empty else "any",
                    "default": param.default if param.default != inspect.Parameter.empty else None,
                    "required": param.default == inspect.Parameter.empty
                }
            return parameters
        except Exception:
            return {}
    
    def get_functions_by_category(self, category):
        """Get all functions in a category."""
        return [
            name for name, cat in self.function_categories.items()
            if cat == category
        ]
    
    def get_function_help(self, func_name):
        """Get comprehensive help for a function."""
        if func_name not in self.functions:
            return None
        
        func = self.functions[func_name]
        metadata = self.function_metadata.get(func_name, {})
        
        help_text = f"""
Function: {func_name}
Category: {metadata.get('category', 'general')}
Description: {metadata.get('description', func.__doc__ or 'No description')}

Parameters:
"""
        
        for param_name, param_info in metadata.get('parameters', {}).items():
            required = "required" if param_info['required'] else "optional"
            default = f" (default: {param_info['default']})" if param_info['default'] is not None else ""
            help_text += f"  - {param_name} ({param_info['type']}, {required}){default}\n"
        
        if metadata.get('usage_examples'):
            help_text += "\nUsage Examples:\n"
            for example in metadata['usage_examples']:
                help_text += f"  - {example}\n"
        
        return help_text.strip()

# Usage
registry = AdvancedFunctionRegistry()

# Register functions with metadata
registry.register_function_with_metadata(
    portfolio_analyzer,
    category="finance",
    description="Analyze portfolio risk and asset allocation",
    usage_examples=[
        "analyze_portfolio_risk({'stocks': 7000, 'bonds': 3000})",
        "analyze_portfolio_risk({'stocks': 5000, 'bonds': 3000, 'cash': 2000})"
    ]
)

registry.register_function_with_metadata(
    retirement_calculator,
    category="finance", 
    description="Calculate retirement savings requirements",
    usage_examples=[
        "calculate_retirement_needs(30, 65, 50000, 4000)",
        "calculate_retirement_needs(25, 60, 25000, 3500, 0.025)"
    ]
)

# Get help for functions
print("Function Help:")
print(registry.get_function_help("analyze_portfolio_risk"))
```


## Automatic Function Selection

### Smart Function Calling

```python
class SmartFunctionCaller:
    """Intelligent function selection based on user queries."""
    
    def __init__(self, sdk, function_registry):
        self.sdk = sdk
        self.registry = function_registry
        self.query_patterns = self._build_query_patterns()
    
    def _build_query_patterns(self):
        """Build patterns to match queries to functions."""
        return {
            "calculate": ["calculator", "math", "arithmetic"],
            "date": ["calendar", "time", "schedule", "when"],
            "risk": ["portfolio_analyzer", "investment", "allocation"],
            "retirement": ["retirement_calculator", "savings", "pension"],
            "weather": ["weather", "forecast", "temperature"],
            "portfolio": ["portfolio_analyzer", "diversification", "assets"]
        }
    
    def analyze_query_intent(self, query):
        """Analyze query to determine appropriate functions."""
        query_lower = query.lower()
        potential_functions = []
        
        # Check for calculation needs
        calc_keywords = ["calculate", "compute", "+", "-", "*", "/", "^", "sqrt", "sin", "cos"]
        if any(keyword in query_lower for keyword in calc_keywords):
            potential_functions.append("calculator")
        
        # Check for date/time needs
        date_keywords = ["date", "when", "calendar", "schedule", "days", "weeks", "months"]
        if any(keyword in query_lower for keyword in date_keywords):
            potential_functions.append("calendar")
        
        # Check for financial analysis needs
        finance_keywords = ["portfolio", "investment", "risk", "allocation", "stocks", "bonds"]
        if any(keyword in query_lower for keyword in finance_keywords):
            potential_functions.append("portfolio_analyzer")
        
        # Check for retirement planning
        retirement_keywords = ["retirement", "retire", "pension", "savings goal"]
        if any(keyword in query_lower for keyword in retirement_keywords):
            potential_functions.append("retirement_calculator")
        
        return potential_functions
    
    def execute_smart_query(self, query):
        """Execute query with automatic function selection."""
        # Analyze query intent
        suggested_functions = self.analyze_query_intent(query)
        
        if not suggested_functions:
            # No specific functions needed, use regular agent
            return self.sdk.send_message(query)
        
        # Build context about available functions
        function_context = "Available functions for this query:\n"
        for func_name in suggested_functions:
            if func_name in ["calculator", "calendar"]:
                function_context += f"- {func_name}: Built-in {func_name} capabilities\n"
            else:
                help_text = self.registry.get_function_help(func_name)
                if help_text:
                    function_context += f"- {func_name}: {help_text.split('Description:')[^1].split('Parameters:')[^0].strip()}\n"
        
        # Enhanced query with function awareness
        enhanced_query = f"""
{function_context}

User Query: {query}

Please use the appropriate functions to answer this query accurately.
"""
        
        return self.sdk.send_message(enhanced_query)

# Usage
smart_caller = SmartFunctionCaller(sdk, registry)

# Test smart function calling
test_queries = [
    "What's 15% of $50,000?",
    "How many business days until Christmas?",
    "I have $60,000 in stocks and $20,000 in bonds. What's my portfolio risk?",
    "I'm 28, want to retire at 62, have $30,000 saved, and spend $3,800/month. Am I on track?"
]

print("🤖 Smart Function Calling Tests:")
for query in test_queries:
    print(f"\nQuery: {query}")
    suggested = smart_caller.analyze_query_intent(query)
    print(f"Suggested functions: {suggested}")
    
    response = smart_caller.execute_smart_query(query)
    print(f"Response: {response[:200]}...")
```


## Function Integration Best Practices

### Error Handling and Validation

```python
class RobustFunctionWrapper:
    """Wrapper for robust function execution with error handling."""
    
    @staticmethod
    def validate_and_execute(func, *args, **kwargs):
        """Execute function with validation and error handling."""
        try:
            # Validate inputs
            validated_args = []
            for arg in args:
                if isinstance(arg, str) and arg.replace('.', '').replace('-', '').isdigit():
                    validated_args.append(float(arg))
                else:
                    validated_args.append(arg)
            
            # Execute function
            result = func(*validated_args, **kwargs)
            
            # Validate output
            if isinstance(result, dict) and 'error' in result:
                return {"success": False, "error": result['error']}
            
            return {"success": True, "result": result}
            
        except Exception as e:
            return {"success": False, "error": f"Function execution failed: {str(e)}"}

# Example usage
def safe_portfolio_analysis(allocations_dict):
    """Safe wrapper for portfolio analysis."""
    try:
        allocations = {}
        if isinstance(allocations_dict, str):
            # Parse string representation
            import ast
            allocations = ast.literal_eval(allocations_dict)
        else:
            allocations = allocations_dict
        
        return RobustFunctionWrapper.validate_and_execute(
            portfolio_analyzer,
            allocations
        )
    except Exception as e:
        return {"success": False, "error": f"Invalid input: {e}"}

# Test error handling
test_result = safe_portfolio_analysis("{'stocks': 7000, 'bonds': 3000}")
print("Safe execution result:")
print(json.dumps(test_result, indent=2))
```

This comprehensive function integration system enables your Blackbird SDK to automatically handle calculations, calendar operations, and complex financial analyses based on user queries, providing a seamless and intelligent user experience.

### 7. Enterprise Features

# Enterprise Features Documentation

## Overview

The Blackbird SDK includes comprehensive enterprise-grade features including advanced licensing, quota management, session controls, audit logging, and security measures designed for large-scale deployments.

## Enterprise Licensing System

### License Types and Tiers

```python
from blackbird_sdk.licensing.enterprise_license import EnterpriseLicenseManager, LicenseConfig

# Initialize enterprise license manager
license_manager = EnterpriseLicenseManager()

# Check current license
license_info = license_manager.get_license_info()
print("Current License Information:")
print(f"License Type: {license_info.get('license_type')}")
print(f"Tier: {license_info.get('tier')}")
print(f"Device Limit: {license_info.get('device_limit')}")
print(f"Expires: {license_info.get('expires_at')}")
print(f"Features: {license_info.get('features')}")
```


### Configurable License Parameters

```python
# Configure custom license limits
from blackbird_sdk.licensing.enterprise_license import configure_license_limits

# Set custom device limits
custom_device_limits = {
    'startup': 3,
    'small_business': 8,
    'enterprise': 25,
    'enterprise_plus': 50
}

# Set custom expiration periods
custom_expiration_periods = {
    'monthly': 1,
    'quarterly': 3,
    'semi_annual': 6,
    'annual': 12,
    'two_year': 24,
    'three_year': 36
}

# Set custom feature sets
custom_feature_sets = {
    'startup': ['core_sdk', 'basic_agents', 'file_upload'],
    'small_business': ['core_sdk', 'basic_agents', 'specialized_agents', 'file_upload', 'function_calling'],
    'enterprise': ['core_sdk', 'basic_agents', 'specialized_agents', 'file_upload', 'function_calling', 'atlastune_finetuning', 'web_search'],
    'enterprise_plus': ['all']
}

# Apply configuration
configure_license_limits(
    device_limits=custom_device_limits,
    expiration_periods=custom_expiration_periods,
    feature_sets=custom_feature_sets
)

print("✅ Custom license configuration applied")
```


### Device Management

```python
# Check device usage
device_usage = license_manager.get_device_usage()
print("Device Usage Information:")
print(f"Total Devices: {device_usage['total_devices']}")
print(f"Device Limit: {device_usage['device_limit']}")
print(f"Current Device ID: {device_usage['current_device_id']}")

# List registered devices
for device in device_usage.get('devices', []):
    print(f"Device: {device.get('device_id', 'Unknown')[:12]}...")
    print(f"  Registered: {device.get('registered_at', 'Unknown')}")
    print(f"  Last Seen: {device.get('last_seen', 'Unknown')}")
    print(f"  Platform: {device.get('platform', 'Unknown')}")
```


### Feature Access Control

```python
# Check feature availability
def check_enterprise_features(sdk):
    """Check what enterprise features are available."""
    features_to_check = [
        'core_sdk',
        'basic_agents', 
        'specialized_agents',
        'file_upload',
        'function_calling',
        'atlastune_finetuning',
        'web_search',
        'enterprise_analytics',
        'priority_support'
    ]
    
    available_features = {}
    for feature in features_to_check:
        available = sdk.is_feature_enabled(feature)
        available_features[feature] = available
        status = "✅ Available" if available else "❌ Not Available"
        print(f"{feature}: {status}")
    
    return available_features

# Check features
sdk = BlackbirdSDK()
features = check_enterprise_features(sdk)
```


## Advanced Session Management

### Enterprise Session Configuration

```python
from blackbird_sdk.session.session_manager import SessionManager
from blackbird_sdk.session.session_types import QuotaType, RateLimitType

# Initialize session manager with enterprise configuration
enterprise_config = {
    'session_timeout': 7200,  # 2 hours
    'max_sessions_per_user': 20,
    'cleanup_interval': 180,  # 3 minutes
    'enable_detailed_logging': True,
    'enable_usage_analytics': True
}

session_manager = SessionManager(config=enterprise_config)

# Create enterprise user session
enterprise_session = session_manager.create_session(
    user_id="enterprise_user_001",
    tier="enterprise",
    metadata={
        "department": "Research & Development",
        "project": "AI Model Development",
        "cost_center": "CC-2024-AI-001",
        "manager": "john.smith@company.com",
        "security_clearance": "level_3"
    }
)

print(f"Enterprise session created: {enterprise_session.session_id}")
```


### Advanced Quota Management

```python
class EnterpriseQuotaManager:
    """Enterprise-grade quota management."""
    
    def __init__(self, session_manager):
        self.session_manager = session_manager
        self.quota_policies = {}
        self.usage_alerts = []
    
    def set_department_quota_policy(self, department, quotas):
        """Set quota policy for a department."""
        self.quota_policies[department] = quotas
        print(f"Quota policy set for {department}")
    
    def apply_quota_policy(self, session_id, department):
        """Apply department quota policy to a session."""
        if department in self.quota_policies:
            policy = self.quota_policies[department]
            
            for quota_type, limit in policy.items():
                try:
                    session = self.session_manager.get_session(session_id)
                    if session and hasattr(session, 'quotas'):
                        if hasattr(QuotaType, quota_type.upper()):
                            quota_enum = getattr(QuotaType, quota_type.upper())
                            if quota_enum in session.quotas:
                                session.quotas[quota_enum].limit = limit
                                print(f"Updated {quota_type} quota to {limit}")
                except Exception as e:
                    print(f"Error applying quota policy: {e}")
    
    def monitor_quota_usage(self, threshold=0.8):
        """Monitor quota usage across all sessions."""
        high_usage_sessions = []
        
        for session_id, session in self.session_manager.sessions.items():
            if hasattr(session, 'quotas'):
                for quota_type, quota in session.quotas.items():
                    usage_percentage = quota.usage_percentage
                    if usage_percentage >= threshold * 100:
                        high_usage_sessions.append({
                            'session_id': session_id,
                            'user_id': session.user_id,
                            'quota_type': quota_type.value,
                            'usage_percentage': usage_percentage,
                            'department': session.metadata.get('department', 'Unknown')
                        })
        
        return high_usage_sessions
    
    def generate_usage_report(self, time_period='daily'):
        """Generate enterprise usage report."""
        report = {
            'report_type': 'enterprise_usage',
            'time_period': time_period,
            'generated_at': time.time(),
            'total_sessions': len(self.session_manager.sessions),
            'active_sessions': sum(1 for s in self.session_manager.sessions.values() if s.is_active),
            'department_breakdown': {},
            'quota_utilization': {},
            'cost_analysis': {}
        }
        
        # Analyze by department
        dept_stats = {}
        for session in self.session_manager.sessions.values():
            dept = session.metadata.get('department', 'Unknown')
            if dept not in dept_stats:
                dept_stats[dept] = {'sessions': 0, 'users': set(), 'quota_usage': {}}
            
            dept_stats[dept]['sessions'] += 1
            dept_stats[dept]['users'].add(session.user_id)
            
            # Aggregate quota usage
            if hasattr(session, 'quotas'):
                for quota_type, quota in session.quotas.items():
                    if quota_type.value not in dept_stats[dept]['quota_usage']:
                        dept_stats[dept]['quota_usage'][quota_type.value] = 0
                    dept_stats[dept]['quota_usage'][quota_type.value] += quota.used
        
        # Convert sets to counts
        for dept, stats in dept_stats.items():
            stats['unique_users'] = len(stats['users'])
            del stats['users']
        
        report['department_breakdown'] = dept_stats
        
        return report

# Usage
quota_manager = EnterpriseQuotaManager(session_manager)

# Set department policies
quota_manager.set_department_quota_policy('R&D', {
    'api_calls': 10000,
    'tokens': 1000000,
    'storage': 10737418240,  # 10GB
    'bandwidth': 107374182400  # 100GB
})

quota_manager.set_department_quota_policy('Marketing', {
    'api_calls': 5000,
    'tokens': 500000,
    'storage': 5368709120,  # 5GB
    'bandwidth': 53687091200  # 50GB
})

# Apply policy to session
quota_manager.apply_quota_policy(
    enterprise_session.session_id, 
    'R&D'
)

# Monitor usage
high_usage = quota_manager.monitor_quota_usage(threshold=0.75)
if high_usage:
    print("High usage sessions detected:")
    for session_info in high_usage:
        print(f"  Session: {session_info['session_id'][:8]}...")
        print(f"  Department: {session_info['department']}")
        print(f"  Usage: {session_info['usage_percentage']:.1f}%")
```


## Enterprise Analytics and Reporting

### Comprehensive Analytics Dashboard

```python
class EnterpriseAnalyticsDashboard:
    """Enterprise analytics and reporting system."""
    
    def __init__(self, sdk):
        self.sdk = sdk
        self.session_manager = sdk.session_manager
        self.metrics_store = {}
        self.reports_generated = []
    
    def collect_system_metrics(self):
        """Collect comprehensive system metrics."""
        import psutil
        import time
        
        # System metrics
        system_metrics = {
            'timestamp': time.time(),
            'cpu_usage': psutil.cpu_percent(interval=1),
            'memory_usage': psutil.virtual_memory().percent,
            'disk_usage': psutil.disk_usage('/').percent,
            'network_io': dict(psutil.net_io_counters()._asdict()),
            'process_count': len(psutil.pids())
        }
        
        # Session metrics
        session_stats = self.session_manager.get_statistics()
        
        # License metrics
        license_info = self.sdk.get_license_info()
        device_usage = self.sdk.get_device_usage()
        
        comprehensive_metrics = {
            'system': system_metrics,
            'sessions': session_stats,
            'license': {
                'type': license_info.get('license_type'),
                'tier': license_info.get('tier'),
                'device_utilization': device_usage['total_devices'] / device_usage['device_limit'] if device_usage['device_limit'] > 0 else 0,
                'features_enabled': len(license_info.get('features', []))
            }
        }
        
        # Store metrics
        self.metrics_store[time.time()] = comprehensive_metrics
        
        return comprehensive_metrics
    
    def generate_executive_summary(self, time_range_hours=24):
        """Generate executive summary report."""
        current_time = time.time()
        start_time = current_time - (time_range_hours * 3600)
        
        # Filter metrics for time range
        relevant_metrics = {
            timestamp: metrics for timestamp, metrics in self.metrics_store.items()
            if timestamp >= start_time
        }
        
        if not relevant_metrics:
            return "No data available for the specified time range."
        
        # Calculate averages and trends
        cpu_values = [m['system']['cpu_usage'] for m in relevant_metrics.values()]
        memory_values = [m['system']['memory_usage'] for m in relevant_metrics.values()]
        session_counts = [m['sessions']['active_sessions'] for m in relevant_metrics.values()]
        
        summary = f"""
EXECUTIVE SUMMARY - BLACKBIRD SDK ENTERPRISE
=============================================
Report Period: Last {time_range_hours} hours
Generated: {datetime.fromtimestamp(current_time).strftime('%Y-%m-%d %H:%M:%S')}

PERFORMANCE OVERVIEW:
- Average CPU Usage: {sum(cpu_values)/len(cpu_values):.1f}%
- Average Memory Usage: {sum(memory_values)/len(memory_values):.1f}%
- Peak Active Sessions: {max(session_counts)}
- Average Active Sessions: {sum(session_counts)/len(session_counts):.1f}

LICENSE UTILIZATION:
- License Tier: {list(relevant_metrics.values())[-1]['license']['tier']}
- Device Utilization: {list(relevant_metrics.values())[-1]['license']['device_utilization']*100:.1f}%
- Features Enabled: {list(relevant_metrics.values())[-1]['license']['features_enabled']}

RECOMMENDATIONS:
"""
        
        # Add recommendations based on metrics
        avg_cpu = sum(cpu_values)/len(cpu_values)
        avg_memory = sum(memory_values)/len(memory_values)
        
        if avg_cpu > 80:
            summary += "- Consider scaling up CPU resources\n"
        if avg_memory > 85:
            summary += "- Memory usage is high, consider increasing RAM\n"
        if max(session_counts) > 50:
            summary += "- High session volume detected, monitor for scaling needs\n"
        
        return summary
    
    def generate_compliance_report(self):
        """Generate compliance and audit report."""
        report = {
            'report_type': 'compliance_audit',
            'generated_at': time.time(),
            'sdk_version': getattr(self.sdk, '__version__', 'Unknown'),
            'license_compliance': self._check_license_compliance(),
            'security_metrics': self._check_security_metrics(),
            'data_handling': self._check_data_handling_compliance(),
            'user_access': self._analyze_user_access_patterns()
        }
        
        return report
    
    def _check_license_compliance(self):
        """Check license compliance status."""
        license_info = self.sdk.get_license_info()
        device_usage = self.sdk.get_device_usage()
        
        compliance_status = {
            'license_valid': license_info.get('license_type') != 'No valid license',
            'within_device_limit': device_usage['total_devices'] <= device_usage['device_limit'],
            'license_expiry_days': self._calculate_days_to_expiry(license_info.get('expires_at')),
            'feature_usage_authorized': True  # Would implement actual check
        }
        
        compliance_status['overall_compliant'] = all([
            compliance_status['license_valid'],
            compliance_status['within_device_limit'],
            compliance_status['license_expiry_days'] > 0
        ])
        
        return compliance_status
    
    def _calculate_days_to_expiry(self, expiry_date_str):
        """Calculate days until license expiry."""
        if not expiry_date_str or expiry_date_str == 'unknown':
            return -1
        
        try:
            from datetime import datetime
            expiry_date = datetime.fromisoformat(expiry_date_str.replace('Z', '+00:00'))
            now = datetime.now(expiry_date.tzinfo)
            delta = expiry_date - now
            return delta.days
        except:
            return -1
    
    def _check_security_metrics(self):
        """Check security-related metrics."""
        return {
            'active_sessions_count': len([s for s in self.session_manager.sessions.values() if s.is_active]),
            'failed_authentication_attempts': 0,  # Would implement actual tracking
            'unusual_access_patterns': False,      # Would implement actual detection
            'data_encryption_enabled': True,      # Would check actual encryption status
            'audit_logging_enabled': True         # Would check actual logging status
        }
    
    def _check_data_handling_compliance(self):
        """Check data handling compliance."""
        return {
            'pii_detection_enabled': True,        # Would implement actual PII detection
            'data_retention_policy_active': True, # Would check actual policy
            'data_anonymization_available': True, # Would check actual capability
            'gdpr_compliance_features': True      # Would check GDPR features
        }
    
    def _analyze_user_access_patterns(self):
        """Analyze user access patterns for anomalies."""
        user_stats = {}
        
        for session in self.session_manager.sessions.values():
            user_id = session.user_id
            if user_id not in user_stats:
                user_stats[user_id] = {
                    'session_count': 0,
                    'departments': set(),
                    'last_activity': 0
                }
            
            user_stats[user_id]['session_count'] += 1
            user_stats[user_id]['departments'].add(session.metadata.get('department', 'Unknown'))
            user_stats[user_id]['last_activity'] = max(
                user_stats[user_id]['last_activity'],
                session.last_activity
            )
        
        # Convert sets to lists for JSON serialization
        for user_id, stats in user_stats.items():
            stats['departments'] = list(stats['departments'])
        
        return {
            'total_users': len(user_stats),
            'users_with_multiple_departments': len([
                u for u in user_stats.values() 
                if len(u['departments']) > 1
            ]),
            'average_sessions_per_user': sum(u['session_count'] for u in user_stats.values()) / len(user_stats) if user_stats else 0,
            'user_details': user_stats
        }

# Usage
analytics = EnterpriseAnalyticsDashboard(sdk)

# Collect metrics periodically
for i in range(5):
    metrics = analytics.collect_system_metrics()
    print(f"Metrics collected at {datetime.fromtimestamp(metrics['timestamp']).strftime('%H:%M:%S')}")
    time.sleep(2)

# Generate executive summary
summary = analytics.generate_executive_summary(time_range_hours=1)
print("\nExecutive Summary:")
print(summary)

# Generate compliance report
compliance = analytics.generate_compliance_report()
print("\nCompliance Report:")
print(json.dumps(compliance, indent=2, default=str))
```


## Security and Audit Features

### Advanced Audit Logging

```python
class EnterpriseAuditLogger:
    """Enterprise-grade audit logging system."""
    
    def __init__(self, log_file_path="enterprise_audit.log"):
        self.log_file_path = log_file_path
        self.audit_events = []
        self.security_events = []
    
    def log_security_event(self, event_type, user_id, details, severity="medium"):
        """Log security-related events."""
        event = {
            'timestamp': time.time(),
            'event_type': 'security',
            'security_event_type': event_type,
            'user_id': user_id,
            'severity': severity,
            'details': details,
            'source_ip': self._get_source_ip(),
            'session_id': self._get_current_session_id()
        }
        
        self.security_events.append(event)
        self._write_to_log(event)
        
        # Alert on high severity events
        if severity == "high":
            self._trigger_security_alert(event)
    
    def log_access_event(self, user_id, resource, action, success=True):
        """Log access events."""
        event = {
            'timestamp': time.time(),
            'event_type': 'access',
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'success': success,
            'source_ip': self._get_source_ip()
        }
        
        self.audit_events.append(event)
        self._write_to_log(event)
    
    def log_data_event(self, user_id, data_type, operation, data_size=0):
        """Log data handling events."""
        event = {
            'timestamp': time.time(),
            'event_type': 'data',
            'user_id': user_id,
            'data_type': data_type,
            'operation': operation,
            'data_size_bytes': data_size,
            'compliance_flags': self._check_compliance_flags(data_type, operation)
        }
        
        self.audit_events.append(event)
        self._write_to_log(event)
    
    def _get_source_ip(self):
        """Get source IP address."""
        # In a real implementation, this would get the actual source IP
        return "127.0.0.1"
    
    def _get_current_session_id(self):
        """Get current session ID."""
        # In a real implementation, this would get the actual session ID
        return "session_123"
    
    def _check_compliance_flags(self, data_type, operation):
        """Check compliance flags for data operations."""
        flags = []
        
        # PII detection
        if data_type in ['user_data', 'personal_info', 'financial_data']:
            flags.append('pii_detected')
        
        # Sensitive operations
        if operation in ['export', 'share', 'external_api_call']:
            flags.append('sensitive_operation')
        
        return flags
    
    def _write_to_log(self, event):
        """Write event to log file."""
        try:
            with open(self.log_file_path, 'a') as f:
                f.write(json.dumps(event) + '\n')
        except Exception as e:
            print(f"Failed to write audit log: {e}")
    
    def _trigger_security_alert(self, event):
        """Trigger security alert for high severity events."""
        alert_message = f"""
SECURITY ALERT: {event['security_event_type']}
Time: {datetime.fromtimestamp(event['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}
User: {event['user_id']}
Severity: {event['severity']}
Details: {event['details']}
"""
        print(alert_message)
        # In production, this would send to security team
    
    def generate_audit_report(self, start_time=None, end_time=None):
        """Generate audit report for specified time range."""
        if start_time is None:
            start_time = time.time() - 86400  # Last 24 hours
        if end_time is None:
            end_time = time.time()
        
        # Filter events by time range
        filtered_events = [
            event for event in self.audit_events
            if start_time <= event['timestamp'] <= end_time
        ]
        
        # Analyze events
        event_summary = {}
        user_activity = {}
        
        for event in filtered_events:
            event_type = event['event_type']
            user_id = event['user_id']
            
            # Count event types
            event_summary[event_type] = event_summary.get(event_type, 0) + 1
            
            # Track user activity
            if user_id not in user_activity:
                user_activity[user_id] = {'events': 0, 'types': set()}
            user_activity[user_id]['events'] += 1
            user_activity[user_id]['types'].add(event_type)
        
        # Convert sets to lists for JSON serialization
        for user_stats in user_activity.values():
            user_stats['types'] = list(user_stats['types'])
        
        return {
            'report_period': {
                'start': datetime.fromtimestamp(start_time).isoformat(),
                'end': datetime.fromtimestamp(end_time).isoformat()
            },
            'total_events': len(filtered_events),
            'event_summary': event_summary,
            'user_activity': user_activity,
            'security_events_count': len([e for e in self.security_events if start_time <= e['timestamp'] <= end_time])
        }

# Usage
audit_logger = EnterpriseAuditLogger()

# Log various events
audit_logger.log_access_event("user123", "financial_data", "read", success=True)
audit_logger.log_security_event("failed_login", "user456", "Multiple failed login attempts", severity="medium")
audit_logger.log_data_event("user123", "financial_data", "export", data_size=1024000)

# Generate audit report
report = audit_logger.generate_audit_report()
print("Audit Report:")
print(json.dumps(report, indent=2))
```


## Enterprise Deployment Features

### Multi-Tenant Support

```python
class EnterpriseTenantManager:
    """Multi-tenant management for enterprise deployments."""
    
    def __init__(self, sdk):
        self.sdk = sdk
        self.tenants = {}
        self.tenant_configs = {}
    
    def create_tenant(self, tenant_id, config):
        """Create a new tenant with specific configuration."""
        self.tenants[tenant_id] = {
            'created_at': time.time(),
            'status': 'active',
            'users': set(),
            'sessions': {},
            'quota_usage': {},
            'metadata': config.get('metadata', {})
        }
        
        self.tenant_configs[tenant_id] = config
        
        print(f"Tenant created: {tenant_id}")
        return self.tenants[tenant_id]
    
    def configure_tenant_isolation(self, tenant_id, isolation_config):
        """Configure tenant isolation settings."""
        if tenant_id not in self.tenants:
            raise ValueError(f"Tenant {tenant_id} not found")
        
        self.tenant_configs[tenant_id]['isolation'] = isolation_config
        
        # Apply isolation settings
        if isolation_config.get('dedicated_resources'):
            self._allocate_dedicated_resources(tenant_id)
        
        if isolation_config.get('network_isolation'):
            self._configure_network_isolation(tenant_id)
        
        if isolation_config.get('data_isolation'):
            self._configure_data_isolation(tenant_id)
    
    def _allocate_dedicated_resources(self, tenant_id):
        """Allocate dedicated resources for tenant."""
        # Implementation would allocate CPU, memory, storage
        print(f"Dedicated resources allocated for tenant {tenant_id}")
    
    def _configure_network_isolation(self, tenant_id):
        """Configure network isolation for tenant."""
        # Implementation would set up network segmentation
        print(f"Network isolation configured for tenant {tenant_id}")
    
    def _configure_data_isolation(self, tenant_id):
        """Configure data isolation for tenant."""
        # Implementation would set up data segregation
        print(f"Data isolation configured for tenant {tenant_id}")
    
    def get_tenant_metrics(self, tenant_id):
        """Get comprehensive metrics for a tenant."""
        if tenant_id not in self.tenants:
            return None
        
        tenant = self.tenants[tenant_id]
        
        return {
            'tenant_id': tenant_id,
            'status': tenant['status'],
            'created_at': tenant['created_at'],
            'user_count': len(tenant['users']),
            'active_sessions': len(tenant['sessions']),
            'quota_usage': tenant['quota_usage'],
            'uptime_days': (time.time() - tenant['created_at']) / 86400
        }

# Usage
tenant_manager = EnterpriseTenantManager(sdk)

# Create tenants
acme_corp_config = {
    'name': 'ACME Corporation',
    'tier': 'enterprise',
    'features': ['all'],
    'metadata': {
        'industry': 'Technology',
        'size': 'Large',
        'compliance_requirements': ['SOX', 'GDPR']
    }
}

startup_config = {
    'name': 'StartupCo',
    'tier': 'professional',
    'features': ['core_sdk', 'basic_agents', 'file_upload'],
    'metadata': {
        'industry': 'FinTech',
        'size': 'Small',
        'compliance_requirements': ['PCI-DSS']
    }
}

tenant_manager.create_tenant('acme_corp', acme_corp_config)
tenant_manager.create_tenant('startup_co', startup_config)

# Configure isolation
tenant_manager.configure_tenant_isolation('acme_corp', {
    'dedicated_resources': True,
    'network_isolation': True,
    'data_isolation': True
})

# Get metrics
acme_metrics = tenant_manager.get_tenant_metrics('acme_corp')
print("ACME Corp Metrics:")
print(json.dumps(acme_metrics, indent=2))
```


### 8. Backend Management

# Backend Management Documentation

## Overview

The Blackbird SDK includes a sophisticated backend management system that automatically handles server deployment, scaling, health monitoring, and resource management across different platforms.

## Core Backend Features

### Automatic Backend Deployment

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.server import BackendManager

# Initialize SDK with automatic backend management
sdk = BlackbirdSDK(development_mode=True)

# Backend is automatically started during SDK initialization
# Check backend status
backend_status = sdk.get_backend_status()
print("Backend Status:")
print(f"  Running: {backend_status['is_running']}")
print(f"  Port: {backend_status['port']}")
print(f"  Health Check: {backend_status['health_check']}")
print(f"  Process ID: {backend_status.get('process_id', 'Unknown')}")
```


### Manual Backend Management

```python
# Get backend manager instance
backend_manager = BackendManager.get_instance()

# Start backend manually
backend_path = r"C:\decompute-app\sdk\blackbird_sdk\backends\windows\decompute.py"
success = backend_manager.start_backend(backend_path, port=5012)

if success:
    print("✅ Backend started successfully")
else:
    print("❌ Failed to start backend")

# Check backend health
health_status = backend_manager.health_check()
print(f"Backend health: {'✅ Healthy' if health_status else '❌ Unhealthy'}")

# Get detailed status
status = backend_manager.get_backend_status()
print("Detailed Backend Status:")
for key, value in status.items():
    print(f"  {key}: {value}")
```


### Platform-Specific Backend Management

```python
from blackbird_sdk.acceleration.platform_manager import PlatformManager

# Initialize platform manager
platform_manager = PlatformManager()

# Get platform information
platform_info = platform_manager.get_platform_info()
print("Platform Information:")
print(f"  OS: {platform_info['platform']}")
print(f"  Processor: {platform_info['processor']}")
print(f"  GPU Type: {platform_info.get('gpu_type', 'None')}")
print(f"  Memory: {platform_info.get('memory_gb', 'Unknown')} GB")
print(f"  CPU Cores: {platform_info.get('cpu_cores', 'Unknown')}")

# Get optimized backend configuration
backend_config = platform_manager.get_optimized_config()
print("\nOptimized Backend Configuration:")
for key, value in backend_config.items():
    print(f"  {key}: {value}")
```


## Backend Health Monitoring

### Comprehensive Health Checks

```python
class BackendHealthMonitor:
    """Comprehensive backend health monitoring system."""
    
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
BACKEND HEALTH REPORT
====================
Generated: {datetime.fromtimestamp(latest_check['timestamp']).strftime('%Y-%m-%d %H:%M:%S')}

CURRENT STATUS:
- Overall Health: {'✅ Healthy' if latest_check['overall_healthy'] else '❌ Unhealthy'}
- Response Time: {latest_check.get('checks', {}).get('connectivity', {}).get('response_time_ms', 'N/A')}ms
- CPU Usage: {latest_check.get('metrics', {}).get('cpu_usage_percent', 'N/A')}%
- Memory Usage: {latest_check.get('metrics', {}).get('memory_usage_percent', 'N/A')}%

24-HOUR TRENDS:
- Uptime: {trends_24h.get('uptime_percentage', 0):.1f}%
- Average Response Time: {trends_24h.get('average_response_time_ms', 0):.0f}ms
- Total Health Checks: {trends_24h.get('total_checks', 0)}
- Issues Detected: {trends_24h.get('unhealthy_checks', 0)}

RECENT ALERTS

<div style="text-align: center">⁂</div>

[^1]: http_client.py
[^2]: logger.py
[^3]: session_manager.py
[^4]: session_types.py
[^5]: decompute.py
[^6]: display_manager.py
[^7]: server.py
[^8]: platform_manager.py
[^9]: response_manager.py
[^10]: agent.py
[^11]: Agent_creation_guide.md
[^12]: agent_manager.py
[^13]: chat_service.py
[^14]: chat_service_streaming.py
[^15]: manager.py
[^16]: templates.py
[^17]: validator.py
[^18]: model_configs.py
[^19]: model_downloader.py
[^20]: model_service.py
[^21]: model_types.py
[^22]: builder.py
[^23]: init.py
[^24]: basic_agent_creation.py
[^25]: init.py
[^26]: paste-27.txt
[^27]: Agent_creation_guide.md```

