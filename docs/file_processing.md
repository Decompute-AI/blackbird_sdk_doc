# File Management & Processing Documentation

## Understanding the File Processing Ecosystem

The Blackbird SDK's file processing system represents a comprehensive, enterprise-grade document management and analysis platform that transforms how organizations handle their digital content. Unlike simple file upload utilities, this system provides intelligent content extraction, automated analysis, and seamless integration with AI agents to create powerful document-driven workflows.

**Multi-Format Intelligence**: The file processing system understands the structure and content of dozens of file formats, from traditional documents like PDFs and Word files to complex spreadsheets, presentations, images, and even audio files. Each format is handled by specialized processors that understand the unique characteristics and extract maximum value from the content.

**Contextual Processing**: Rather than treating files as isolated entities, the system integrates file content into conversation contexts, allowing AI agents to reference, analyze, and discuss document contents as naturally as they would discuss any other topic. This creates a seamless experience where documents become part of the conversation flow.

**Enterprise Security and Compliance**: All file processing operations are designed with enterprise security requirements in mind, including content scanning, virus detection, privacy protection, and audit trails that meet compliance requirements for regulated industries.

## Core File Processing Architecture

### 1. File Service Layer (`file_service.py`)

The FileService acts as the central orchestrator for all file-related operations, providing a unified interface for file upload, processing, analysis, and integration with AI agents.

**Intelligent File Detection**: When files are uploaded, the system performs sophisticated analysis to determine file types, content structure, and processing requirements. This goes beyond simple file extension checking to include content-based detection, metadata analysis, and format validation.

**Processing Pipeline Management**: Each file type follows an optimized processing pipeline that includes:

1. **Security Scanning**: Comprehensive virus scanning and malware detection using multiple engines
2. **Content Extraction**: Intelligent text extraction that preserves formatting, structure, and metadata
3. **Quality Assessment**: Analysis of content quality, readability, and completeness
4. **Indexing and Search**: Creation of searchable indexes for fast content retrieval
5. **AI Integration**: Preparation of content for AI agent consumption with appropriate context

**Resource Management**: The file service carefully manages processing resources, ensuring that large files don't overwhelm the system while maintaining responsiveness for all users. This includes intelligent queuing, resource allocation, and processing optimization.

### 2. Document Processing Engine (`document_processor.py`)

The document processing engine handles the complex task of extracting meaningful content from various document formats while preserving structure and context.

**Format-Specific Processors**: Each supported file format has a dedicated processor that understands its unique characteristics:

- **PDF Processor**: Handles both text-based and scanned PDFs, with OCR capabilities for image-based content
- **Office Document Processor**: Extracts content from Word, Excel, and PowerPoint files while preserving formatting and structure
- **Spreadsheet Processor**: Understands data relationships, formulas, and chart content in Excel and CSV files
- **Image Processor**: Performs OCR on images and can analyze visual content for charts, diagrams, and other structured information

**Content Structure Preservation**: The processors maintain document structure, including headings, paragraphs, tables, lists, and other formatting elements that provide context for AI analysis. This ensures that agents understand not just what the content says, but how it's organized and structured.

**Metadata Extraction**: Beyond text content, the system extracts comprehensive metadata including creation dates, author information, document properties, and technical specifications that can be valuable for analysis and compliance purposes.

### 3. OCR and Image Analysis (`ocr_service.py`)

The OCR (Optical Character Recognition) service provides advanced text extraction capabilities for scanned documents and images.

**Multi-Engine OCR**: The system employs multiple OCR engines to ensure maximum accuracy across different types of content:

- **High-Resolution Text**: Optimized for clean, high-resolution scanned documents
- **Low-Quality Sources**: Specialized processing for poor-quality scans, photos of documents, and challenging conditions
- **Multi-Language Support**: Recognition capabilities for dozens of languages with automatic language detection
- **Handwriting Recognition**: Limited support for printed handwriting and form-based content

**Image Content Analysis**: Beyond text extraction, the system can analyze visual elements in images:

- **Chart and Graph Recognition**: Identification and data extraction from charts, graphs, and diagrams
- **Table Detection**: Recognition of tabular data in images with structure preservation
- **Layout Analysis**: Understanding of document layout, columns, and reading order

**Quality Enhancement**: The system includes image preprocessing capabilities that can improve OCR accuracy:

- **Noise Reduction**: Removal of scanning artifacts and background noise
- **Contrast Enhancement**: Optimization of image contrast for better text recognition
- **Skew Correction**: Automatic correction of document rotation and skew

### 4. Content Analysis and Intelligence (`content_analyzer.py`)

The content analysis system provides advanced understanding of document content beyond simple text extraction.

**Semantic Analysis**: The system understands the meaning and context of document content, including:

- **Topic Classification**: Automatic categorization of documents by subject matter
- **Entity Recognition**: Identification of people, places, organizations, dates, and other important entities
- **Sentiment Analysis**: Understanding of tone and sentiment in written content
- **Key Concept Extraction**: Identification of main themes and important concepts

**Data Structure Recognition**: For documents containing structured data, the system can identify and extract:

- **Tables and Spreadsheets**: Recognition of tabular data with column headers and relationships
- **Forms and Fields**: Identification of form structures and field values
- **Lists and Hierarchies**: Understanding of document organization and information hierarchy
- **References and Citations**: Recognition of bibliographic references and citation patterns

**Content Relationships**: The system can identify relationships between different parts of documents and between multiple documents, enabling sophisticated cross-referencing and analysis capabilities.

### 5. Integration with AI Agents (`agent_integration.py`)

The file processing system is deeply integrated with the AI agent framework, allowing agents to seamlessly work with document content.

**Context Integration**: When files are processed, their content becomes available to AI agents as conversation context. This means agents can reference file contents, answer questions about documents, and perform analysis based on uploaded materials.

**Specialized Processing Instructions**: Different agent types can request specialized processing of the same file:

- **Financial Agents**: Focus on numerical data, financial metrics, and quantitative analysis
- **Legal Agents**: Emphasize contract terms, legal language, and compliance aspects
- **Research Agents**: Prioritize citations, methodology, and factual content
- **Technical Agents**: Focus on specifications, procedures, and technical details

**Multi-Document Analysis**: Agents can work with multiple documents simultaneously, performing comparative analysis, synthesis, and cross-referencing across entire document collections.

## Advanced File Processing Features

### Batch Processing and Automation

The system supports sophisticated batch processing capabilities for handling large document collections efficiently.

**Automated Workflows**: Organizations can set up automated workflows that process documents according to predefined rules:

- **Document Classification**: Automatic sorting of documents into categories
- **Content Extraction**: Bulk extraction of specific data points from document collections
- **Quality Control**: Automated checking for completeness, accuracy, and compliance
- **Report Generation**: Creation of summary reports and analysis documents

**Processing Queues**: Large file processing operations are managed through intelligent queuing systems that:

- **Prioritize Urgent Content**: Important documents can be processed with higher priority
- **Optimize Resource Usage**: Batch processing is scheduled to maximize system efficiency
- **Provide Progress Tracking**: Real-time updates on processing status and completion estimates
- **Handle Failures Gracefully**: Automatic retry and error recovery for failed processing operations

### Security and Compliance Features

**Content Scanning and Filtering**: All uploaded files undergo comprehensive security scanning:

- **Malware Detection**: Multi-engine virus and malware scanning
- **Content Policy Enforcement**: Checking for inappropriate or prohibited content
- **Privacy Protection**: Detection and handling of personally identifiable information (PII)
- **Intellectual Property Scanning**: Identification of potentially sensitive or proprietary content

**Audit and Compliance**: The system maintains detailed audit trails for all file operations:

- **Access Logging**: Complete records of who accessed what files when
- **Processing History**: Detailed logs of all processing operations performed on each file
- **Content Modification Tracking**: Records of any changes or modifications to file content
- **Retention Management**: Automated enforcement of document retention policies

**Data Protection**: Files and their content are protected through multiple layers of security:

- **Encryption at Rest**: All stored files are encrypted using enterprise-grade encryption
- **Secure Transmission**: File uploads and downloads use encrypted connections
- **Access Control**: Fine-grained permissions control who can access which files
- **Geographic Controls**: Options for controlling where file data is stored and processed

### Performance Optimization and Scalability

**Intelligent Caching**: The system implements multiple levels of caching to improve performance:

- **Content Caching**: Frequently accessed file content is cached for immediate retrieval
- **Processing Result Caching**: Results of expensive processing operations are cached to avoid redundant work
- **Metadata Caching**: File metadata and properties are cached for quick access
- **Thumbnail and Preview Caching**: Visual previews are generated and cached for quick display

**Scalable Processing**: The file processing system is designed to scale with organizational needs:

- **Horizontal Scaling**: Processing can be distributed across multiple servers
- **Load Balancing**: File processing requests are distributed to optimize resource usage
- **Resource Allocation**: Processing resources are dynamically allocated based on demand
- **Queue Management**: Intelligent queuing ensures fair resource allocation and optimal throughput

**Optimization Techniques**: Various optimization techniques ensure efficient processing:

- **Format-Specific Optimization**: Each file type is processed using the most efficient methods
- **Progressive Processing**: Large files can be processed incrementally for faster initial access
- **Parallel Processing**: Multiple aspects of files can be processed simultaneously
- **Adaptive Processing**: Processing parameters are adjusted based on file characteristics and system load

This comprehensive file processing system transforms how organizations handle their document workflows, providing intelligent automation, enterprise-grade security, and seamless integration with AI-powered analysis capabilities.

Next, you will find working code examples demonstrating how to upload a single file, process multiple files together, and orchestrate batch directory processing. Simply copy and paste these examples into your application—no changes required.

## Supported File Types

### Document Formats

- **Text Files**: .txt, .json
- **PDF**: .pdf
- **Microsoft Office**: .docx, .xlsx, .xls
- **Audio**: .wav, .m4a, .mp3
- **Code**: .py, .js

### File Processing Features

```python
from blackbird_sdk import BlackbirdSDK
from blackbird_sdk.data_pipeline.file_service import FileService
# Initialize SDK with file processing capabilitiessdk = BlackbirdSDK(development_mode=True)
sdk.initialize_agent("finance")  # Use finance agent for document analysis# Get file servicefile_service = FileService()
```

## Single File Processing

### Basic File Upload and Analysis

```python
# Process a single PDF documentfile_path = r"C:\Users\Administrator\Downloads\AWS2024 SEC\annual_report.pdf"# Method 1: Direct file processing with agentresponse = sdk.chat_service.send_message_with_files(
    message="Please analyze this SEC filing and provide key financial insights",
    files=[file_path],
    options={'agent': 'finance', 'model': 'unsloth/Qwen3-1.7B-bnb-4bit'}
)
print("Analysis Results:")
print(response)
```

### Advanced File Processing

```python
# Process with specific instructionsprocessing_instructions = """Please analyze this document and provide:1. Executive summary2. Key financial metrics3. Risk factors identified4. Recommendations for investors5. Comparison with industry standards"""response = sdk.chat_service.send_message_with_files(
    message=processing_instructions,
    files=[file_path],
    options={
        'agent': 'finance',
        'model': 'unsloth/Qwen3-1.7B-bnb-4bit',
        'temperature': 0.3,  # More focused analysis        'max_tokens': 4000   # Longer responses    }
)
```

### File Type Specific Processing

```python
def process_by_file_type(file_path):
    """Process file based on its type."""    file_extension = Path(file_path).suffix.lower()
    if file_extension == '.pdf':
        return process_pdf_document(file_path)
    elif file_extension in ['.xlsx', '.csv']:
        return process_spreadsheet(file_path)
    elif file_extension == '.docx':
        return process_word_document(file_path)
    elif file_extension in ['.jpg', '.png']:
        return process_image(file_path)
    else:
        return f"Unsupported file type: {file_extension}"def process_pdf_document(file_path):
    """Specialized PDF processing."""    message = """    Please analyze this PDF document and provide:    - Document structure and sections    - Key information extracted    - Summary of main points    - Any data tables or figures identified    """    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={'agent': 'research'}
    )
def process_spreadsheet(file_path):
    """Specialized spreadsheet processing."""    message = """    Please analyze this spreadsheet and provide:    - Data summary and statistics    - Key trends and patterns    - Any anomalies or notable findings    - Recommendations based on the data    """    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={'agent': 'finance'}
    )
# Usagefile_path = "financial_data.xlsx"result = process_by_file_type(file_path)
print(result)
```

## Multiple File Processing

### Batch File Processing

```python
# Process multiple files simultaneouslyfile_paths = [
    r"C:\Users\Administrator\Downloads\AWS2024 SEC\annual_report.pdf",
    r"C:\Users\Administrator\Downloads\Amazon SEC Filing 2023\quarterly_report.pdf"]
# Compare multiple documentscomparison_message = """Please compare these SEC filings and provide:1. Key differences in financial performance2. Changes in business strategy3. Risk factor evolution4. Investment recommendation based on comparison"""response = sdk.chat_service.send_message_with_files(
    message=comparison_message,
    files=file_paths,
    options={
        'agent': 'finance',
        'model': 'unsloth/Qwen3-1.7B-bnb-4bit',
        'temperature': 0.2  # More consistent analysis    }
)
print("Comparative Analysis:")
print(response)
```

### Directory Processing

```python
import os
from pathlib import Path
def process_directory(directory_path, file_extensions=None):
    """Process all files in a directory."""    if file_extensions is None:
        file_extensions = ['.pdf', '.docx', '.xlsx', '.txt']
    files_to_process = []
    # Find all supported files    for file_path in Path(directory_path).rglob('*'):
        if file_path.suffix.lower() in file_extensions:
            files_to_process.append(str(file_path))
    print(f"Found {len(files_to_process)} files to process")
    # Process files in batches    batch_size = 5    results = []
    for i in range(0, len(files_to_process), batch_size):
        batch = files_to_process[i:i+batch_size]
        batch_message = f"""        Please analyze this batch of documents ({len(batch)} files) and provide:        1. Summary of each document        2. Common themes across documents        3. Key insights from the collection        4. Overall conclusions        """        batch_result = sdk.chat_service.send_message_with_files(
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
# Usagedirectory_path = r"C:\Users\Administrator\Downloads\financial_documents"results = process_directory(directory_path)
for result in results:
    print(f"\n--- Batch {result['batch_number']} ---")
    print(f"Files: {[Path(f).name for f in result['files']]}")
    print(f"Analysis: {result['analysis'][:200]}...")
```

## Advanced File Processing

### OCR and Image Processing

```python
def process_scanned_document(file_path):
    """Process scanned documents with OCR."""    message = """    This appears to be a scanned document. Please:    1. Extract all text using OCR    2. Identify the document type and structure    3. Extract key information and data    4. Provide a summary of contents    """    return sdk.chat_service.send_message_with_files(
        message=message,
        files=[file_path],
        options={
            'agent': 'research',
            'enable_ocr': True  # Enable OCR processing        }
    )
# Process image with textimage_path = "scanned_invoice.jpg"result = process_scanned_document(image_path)
print(result)
```

### Structured Data Extraction

```python
def extract_structured_data(file_path, schema):
    """Extract structured data according to a schema."""    schema_prompt = f"""    Please extract data from this document according to this schema:    {json.dumps(schema, indent=2)}    Return the extracted data in JSON format matching the schema structure.    """    return sdk.chat_service.send_message_with_files(
        message=schema_prompt,
        files=[file_path],
        options={'agent': 'research'}
    )
# Define extraction schemafinancial_schema = {
    "company_name": "string",
    "reporting_period": "string",
    "revenue": "number",
    "net_income": "number",
    "total_assets": "number",
    "key_metrics": {
        "gross_margin": "percentage",
        "operating_margin": "percentage",
        "debt_to_equity": "ratio"    },
    "risk_factors": ["array of strings"]
}
# Extract structured datafile_path = "annual_report.pdf"extracted_data = extract_structured_data(file_path, financial_schema)
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
        """Organize files by their content type."""        categories = {
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
        """Classify file content."""        classification_message = """        Please classify this document into one of these categories:        - financial: Financial reports, statements, analysis        - legal: Contracts, legal documents, compliance        - technical: Technical specifications, code, manuals        - research: Research papers, studies, analysis        - other: General documents        Respond with just the category name.        """        response = self.sdk.chat_service.send_message_with_files(
            message=classification_message,
            files=[file_path],
            options={'agent': 'general'}
        )
        return response.strip().lower()
# Usageorganizer = FileOrganizer(sdk)
files = [
    "annual_report.pdf",
    "contract.docx",
    "api_documentation.pdf",
    "research_paper.pdf"]
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
        """Add a processing step to the pipeline."""        self.processing_steps.append({
            'name': step_name,
            'agent': agent_type,
            'instructions': instructions
        })
    def process_file(self, file_path):
        """Process file through the pipeline."""        results = {}
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
# Create processing pipelinepipeline = FileProcessingPipeline(sdk)
# Add processing stepspipeline.add_step(
    'content_extraction',
    'general',
    'Extract and summarize the main content of this document.')
pipeline.add_step(
    'financial_analysis',
    'finance',
    'Analyze any financial data or metrics in this document.')
pipeline.add_step(
    'risk_assessment',
    'legal',
    'Identify any risks, compliance issues, or legal concerns.')
# Process file through pipelinefile_path = "company_report.pdf"results = pipeline.process_file(file_path)
for step_name, result in results.items():
    print(f"\n--- {step_name.upper()} ---")
    print(result[:300] + "..." if len(result) > 300 else result)
```

## Integration with Agents

### Specialized Document Agents

```python
# Create specialized document analysis agentfrom blackbird_sdk.creation.builder import create_agent
from blackbird_sdk.creation.types import AgentPersonality, AgentCapability
document_analyzer = (create_agent("document_analyzer", "Specialized document analysis agent")
    .personality(AgentPersonality.ANALYTICAL)
    .system_prompt("""        You are a document analysis specialist with expertise in:        - Extracting key information from various document types        - Identifying document structure and organization        - Summarizing complex documents        - Finding specific data points and metrics        - Comparing multiple documents        Always provide structured, detailed analysis.    """)
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
# Deploy and use the specialized agentsdk.deploy_custom_agent(document_analyzer)
# Use for complex document analysiscomplex_analysis = sdk.send_message_to_custom_agent(
    "document_analyzer",
    "Please provide a comprehensive analysis of the uploaded documents.")
```

### File Processing with Custom Functions

```python
def extract_financial_metrics(file_path):
    """Custom function to extract financial metrics."""    # This would integrate with specialized libraries    # like pandas, openpyxl, or pdfplumber    return {
        "revenue": "1.2B",
        "net_income": "150M",
        "growth_rate": "15%"    }
# Create agent with custom file processing functionsfile_agent = (create_agent("file_processor", "Advanced file processing agent")
    .with_functions([extract_financial_metrics])
    .system_prompt("""        You have access to specialized file processing functions.        Use these tools to provide detailed analysis of uploaded documents.    """)
    .build(sdk)
)
```
