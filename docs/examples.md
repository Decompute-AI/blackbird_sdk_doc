# Blackbird SDK Examples

This document provides a collection of practical, copy-paste-ready examples for common use cases of the Blackbird SDK.

## Fine-Tuning Examples

### Example 1: Fine-Tuning from a Wikipedia Article

This example demonstrates how to fine-tune a model using the content of a single Wikipedia page.

```python
from blackbird_sdk.tuning import FineTuner

tuner = FineTuner()

urls = ["https://en.wikipedia.org/wiki/Python_(programming_language)"]

version_id = tuner.create_fine_tuned_model(urls=urls)
print(f"Started fine-tuning job with version ID: {version_id}")

tuner.wait_for_version(version_id)
print("Fine-tuning complete!")

model, tokenizer = tuner.load_fine_tuned_model(version_id)

prompt = "### Instruction:\nWhat are the key features of Python?\n\n### Response:\n"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens=150)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Example 2: Fine-Tuning with Custom Data and Configuration

This example shows how to use your own data and a custom configuration to fine-tune a model.

```python
from blackbird_sdk.tuning import FineTuner, FineTuningConfig

# Custom configuration
config = FineTuningConfig(
    base_model="unsloth/mistral-7b-bnb-4bit",
    num_epochs=5,
    learning_rate=2e-5,
)

# Custom data
custom_data = [
    {
        "instruction": "Translate the following English text to French: 'Hello, how are you?'",
        "input": "",
        "output": "Bonjour, comment ça va?"
    },
    {
        "instruction": "Translate the following English text to French: 'I am learning to use the Blackbird SDK.'",
        "input": "",
        "output": "J'apprends à utiliser le Blackbird SDK."
    }
]

tuner = FineTuner(config=config)

version_id = tuner.create_fine_tuned_model(custom_data=custom_data)
print(f"Started fine-tuning job with version ID: {version_id}")

tuner.wait_for_version(version_id)
print("Fine-tuning complete!")
```

## RAG Examples

### Example 3: Chatting with a PDF

This example demonstrates how to upload a PDF and ask questions about its content.

```python
from blackbird_sdk import BlackbirdSDK

 sdk = BlackbirdSDK()
sdk.initialize_agent("general")

result = sdk.file_service.upload_for_rag_only("/path/to/your/annual_report.pdf")

response = sdk.send_message("What were the total revenues last year?")
print(response)
```

### Example 4: Analyzing Data from Multiple Files

This example shows how to upload a CSV file and a DOCX file to create a combined RAG context.

```python
from blackbird_sdk import BlackbirdSDK

sdk = BlackbirdSDK()
sdk.initialize_agent("general")

file_paths = ["/path/to/sales_data.csv", "/path/to/marketing_plan.docx"]
result = sdk.file_service.upload_files_rag(file_paths)

response = sdk.send_message("Based on the sales data and the marketing plan, what is our projected revenue for the next quarter?")
print(response)
```

## Combined RAG and Fine-Tuning Example

### Example 5: Creating a Specialized Chatbot

This example demonstrates the full power of the SDK by combining RAG and fine-tuning to create a chatbot that is an expert on a specific topic.

```python
from blackbird_sdk import BlackbirdSDK

sdk = BlackbirdSDK()
sdk.initialize_agent("general")

# 1. Upload a document to use as the knowledge base
# This will also serve as the data for fine-tuning
result = sdk.file_service.upload_and_finetune__single_file("/path/to/your/product_documentation.pdf")
process_id = result["process_id"]

print(f"Fine-tuning job started with process ID: {process_id}")

# You can monitor the fine-tuning job or wait for it to complete

# 2. Once the fine-tuning is complete, you can load the specialized model
# (The SDK will handle this automatically in a future version)

# 3. Chat with your specialized chatbot
response = sdk.send_message("How do I reset the password for my device?")
print(response)
```
