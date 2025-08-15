# RAG and File Upload

The Blackbird SDK provides a robust system for building Retrieval-Augmented Generation (RAG) context from your files. This allows you to chat with your documents, ask questions about your data, and ground your models in your own knowledge base.

## Quickstart: Uploading a File for RAG

The most straightforward way to use the RAG functionality is to upload a single file.

```python
from blackbird_sdk import BlackbirdSDK

# Initialize the SDK
sdk = BlackbirdSDK()

# Initialize an agent
sdk.initialize_agent("general")

# Upload a file for RAG
# This returns a process_id that can be used for fine-tuning later
result = sdk.file_service.upload_for_rag_only("/path/to/your/document.pdf")
print(result)

# Now you can chat with the agent, which will use the document as context
response = sdk.send_message("What is the main topic of the document?")
print(response)
```

## Supported File Types

The SDK supports a wide variety of file types, including:

-   **Documents:** PDF, DOCX, TXT, MD
-   **Spreadsheets:** XLSX, XLS, CSV
-   **Code:** PY, JS, HTML, CSS, JSON, XML, YAML
-   **Audio:** WAV, MP3, M4A, FLAC
-   **Images:** JPG, PNG, GIF, BMP, TIFF (requires OCR)

## The File Service

The `FileService` class is the main entry point for all file-related operations. It handles validation, uploading, and processing of files for RAG.

### Uploading Multiple Files

You can upload multiple files at once to create a unified RAG context.

```python
file_paths = ["/path/to/doc1.pdf", "/path/to/data.csv"]
result = sdk.file_service.upload_files_rag(file_paths)
print(result)

# Chat with the combined knowledge of both documents
response = sdk.send_message("Compare the data in the PDF and the CSV.")
print(response)
```

### Validation

The SDK automatically validates files before uploading, checking for things like file size, type, and readability. You can also manually validate a file:

```python
is_valid, message = sdk.file_service.validate_file("/path/to/your/file.txt")
if is_valid:
    print("File is valid!")
else:
    print(f"Validation failed: {message}")
```

## Combining RAG with Fine-Tuning

You can use the files you upload for RAG as a data source for fine-tuning a model. This creates a powerful workflow where you can ground a model in your data and then further specialize it to your specific tasks.

```python
# 1. Upload a file for RAG, which returns a process_id
result = sdk.file_service.upload_for_rag_only("/path/to/your/document.pdf")
process_id = result["process_id"]

# 2. Use the process_id to start a fine-tuning job
fine_tuning_result = sdk.file_service.start_finetuning(process_id)
print(fine_tuning_result)
```

There is also a convenience method that combines these two steps:

```python
result = sdk.file_service.upload_and_finetune_single_file("/path/to/your/document.pdf")
print(result)
```

## How it Works

When you upload a file, the SDK's data pipeline performs the following steps:

1.  **Parsing:** The file is parsed based on its type (e.g., PDF, DOCX, CSV).
2.  **Text Extraction:** Text and other relevant data (like tables) are extracted.
3.  **Chunking:** The extracted text is divided into smaller, manageable chunks.
4.  **Embedding:** Each chunk is converted into a numerical representation (embedding) using a pre-trained model.
5.  **Indexing:** The embeddings are stored in a searchable index (like FAISS).

When you send a message to the agent, the SDK searches the index for the most relevant chunks of text and provides them to the model as context, allowing it to generate a more accurate and informed response.