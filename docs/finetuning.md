
# Fine-Tuning with Blackbird SDK

The Blackbird SDK provides a powerful and flexible fine-tuning system that allows you to adapt pre-trained models to your specific needs. This guide will walk you through the process of preparing data, running fine-tuning jobs, and using your custom models.

## Quickstart: Fine-Tuning from URLs

The easiest way to get started is by providing a list of URLs. The SDK will automatically scrape the content, process it into a suitable format, and use it to fine-tune a model.

```python
from blackbird_sdk.tuning import FineTuner

# Initialize the fine-tuner
tuner = FineTuner()

# List of URLs to use for fine-tuning
urls = [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/Machine_learning",
]

# Start the fine-tuning job
version_id = tuner.create_fine_tuned_model(urls=urls)
print(f"Started fine-tuning job with version ID: {version_id}")

# Wait for the job to complete
tuner.wait_for_version(version_id)
print("Fine-tuning complete!")

# Load the fine-tuned model
model, tokenizer = tuner.load_fine_tuned_model(version_id)
```

## Preparing Your Data

You can also provide your own custom data for fine-tuning. The SDK supports a simple JSON format with "instruction", "input", and "output" fields.

### Custom Data Format

Your data should be a list of dictionaries, where each dictionary represents a single training example.

```json
[
    {
        "instruction": "Explain quantum computing in simple terms.",
        "input": "",
        "output": "Quantum computing is a revolutionary type of computing that uses the principles of quantum mechanics to process information. Unlike classical computers that use bits (0s and 1s), quantum computers use qubits, which can be both 0 and 1 at the same time."
    },
    {
        "instruction": "Summarize the main benefits of renewable energy.",
        "input": "Renewable energy sources like solar and wind power are crucial for a sustainable future.",
        "output": "The main benefits of renewable energy include reducing carbon emissions, improving air quality, and creating new jobs in the green economy."
    }
]
```

### Fine-Tuning with Custom Data

```python
from blackbird_sdk.tuning import FineTuner

# Your custom data
custom_data = [
    {
        "instruction": "What is the capital of France?",
        "input": "",
        "output": "The capital of France is Paris."
    }
]

tuner = FineTuner()
version_id = tuner.create_fine_tuned_model(custom_data=custom_data)
print(f"Started fine-tuning with custom data. Version ID: {version_id}")

tuner.wait_for_version(version_id)
print("Fine-tuning complete!")
```

## The Fine-Tuning Process

The `FineTuner` class manages the entire fine-tuning workflow. Here's a breakdown of the key components and steps involved:

### Configuration (`FineTuningConfig`)

The `FineTuningConfig` dataclass allows you to customize various aspects of the training process, such as the base model, learning rate, and number of epochs.

```python
from blackbird_sdk.tuning import FineTuningConfig, FineTuner

# Create a custom configuration
config = FineTuningConfig(
    base_model="unsloth/llama-3-8b-bnb-4bit",
    num_epochs=3,
    learning_rate=1e-4,
    batch_size=4,
)

# Initialize the tuner with the custom config
tuner = FineTuner(config=config)
```

### Starting a Fine-Tuning Job

The `create_fine_tuned_model` method kicks off the fine-tuning process in the background. It returns a `version_id` that you can use to track the job and load the model later.

### Monitoring Progress

You can monitor the progress of a fine-tuning job using a callback function.

```python
def progress_callback(job_id, progress, message):
    print(f"Job {job_id}: {progress:.2f}% complete - {message}")

version_id = tuner.create_fine_tuned_model(
    urls=urls,
    progress_callback=progress_callback
)
```

You can also get the status of a job at any time using the `get_job_status` method.

```python
status = tuner.get_job_status(job_id)
print(status)
```

## Using Your Fine-Tuned Model

Once a fine-tuning job is complete, you can easily load your model for inference.

### Loading a Model

Use the `load_fine_tuned_model` method with the `version_id` of the model you want to use.

```python
model, tokenizer = tuner.load_fine_tuned_model(version_id)
```

If you don't provide a `version_id`, the method will load the latest available model.

### Generating Text

```python
prompt = "### Instruction:
Explain the significance of the internet.

### Response:
"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Managing Models

The `FineTuner` includes a `ModelVersionManager` that handles storing, versioning, and cleaning up your fine-tuned models.

### Listing Models

You can list all available fine-tuned models:

```python
models = tuner.list_fine_tuned_models()
for model in models:
    print(f"Version ID: {model['version_id']}, Base Model: {model['base_model']}")
```

### Deleting Models

To save space, you can delete models you no longer need:

```python
tuner.delete_fine_tuned_model(version_id)
```

The `ModelVersionManager` also automatically cleans up old models based on age and number of versions.

## Advanced Topics

### Atlas Integration

The SDK also includes an integration with the "Atlas" fine-tuning service, which provides more advanced capabilities for managing and deploying models. The `AtlasService` class in `tuning/atlas_service.py` is the main entry point for this functionality.

### Supported Models

The fine-tuning module is optimized for use with `unsloth` and supports a variety of models, including:

-   `unsloth/Qwen3-1.7B-bnb-4bit`
-   `unsloth/llama-3-8b-bnb-4bit`
-   `unsloth/mistral-7b-bnb-4bit`

You can change the base model by setting the `base_model` attribute in the `FineTuningConfig`.
