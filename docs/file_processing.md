# File Upload and Processing

The File Service provides a straightforward way to upload and process files using the SDK. It handles file validation, uploading, and provides utilities for inspecting file properties.

## Supported File Types

The following file extensions are supported for upload:

- **Documents**: `.pdf`, `.docx`, `.xls`, `.xlsx`
- **Text**: `.txt`, `.json`
- **Code**: `.py`, `.js`
- **Audio**: `.wav`, `.mp3`, `.m4a`

You can programmatically retrieve this list:

```python
# Assuming 'sdk' is an initialized SDK instance with a file_service attribute
supported_types = sdk.file_service.get_supported_extensions()
print(supported_types)
# Output: ['.docx', '.js', '.json', '.m4a', '.mp3', '.pdf', '.py', '.txt', '.xls', '.xlsx', '.wav'] (sorted)
```

## Core Functionality

### File Validation

Before uploading, the SDK performs several validation checks on each file:
- **Existence**: Ensures the file exists at the specified path.
- **File Type**: Verifies that the file extension is in the list of supported types.
- **File Size**: Checks that the file does not exceed the maximum allowed size.
- **Readability**: Confirms that the file can be opened and read.

If any of these checks fail, a `FileProcessingError` is raised with a descriptive message.

### Getting File Information

You can retrieve detailed information about a local file before uploading it using `get_file_info()`.

```python
from blackbird_sdk.utils.errors import FileProcessingError

# Assuming 'sdk' is an initialized SDK instance
try:
    file_info = sdk.file_service.get_file_info("path/to/your/document.pdf")
    print(file_info)
except FileProcessingError as e:
    print(f"Error: {e}")

# Example Output:
# {
#     'path': '.../path/to/your/document.pdf',
#     'name': 'document.pdf',
#     'extension': '.pdf',
#     'size_bytes': 123456,
#     'size_mb': 0.12,
#     'mime_type': 'application/pdf',
#     'is_supported': True,
#     'created': 1678886400.0,
#     'modified': 1678886400.0
# }
```

## Uploading Files

### Uploading a Single File

Use the `upload_single_file()` method to process a single document.

```python
# Assuming 'sdk' is an initialized SDK instance
file_to_upload = "path/to/your/report.docx"

try:
    # The 'agent_type' and other parameters can be specified.
    # Default values are used if not provided.
    upload_result = sdk.file_service.upload_single_file(
        file_path=file_to_upload,
        agent_type="finance"
    )
    print("Upload successful:")
    print(upload_result)
except FileProcessingError as e:
    print(f"Upload failed: {e}")
```

### Uploading Multiple Files

Use the `upload_multiple_files()` method to process several documents in a single request. This is more efficient than uploading them one by one.

```python
# Assuming 'sdk' is an initialized SDK instance
files_to_upload = [
    "path/to/your/report.docx",
    "path/to/your/data.xlsx",
    "path/to/your/notes.txt"
]

try:
    # The method validates all files before starting the upload.
    upload_result = sdk.file_service.upload_multiple_files(
        file_paths=files_to_upload,
        agent_type="research"
    )
    print("Batch upload successful:")
    print(upload_result)
except FileProcessingError as e:
    print(f"Batch upload failed: {e}")
```
