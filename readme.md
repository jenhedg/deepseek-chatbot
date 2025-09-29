# 🤖 DeepSeek Chatbot: Python + Streamlit App
## About

The **DeepSeek Chatbot** is a beginner-friendly project designed to teach the fundamentals of an AI development ecosystem. This application is local chatbot powered by a DeepSeek model and served via a Streamlit UI.

### 🛠️ Key Technologies

| Tool | Purpose |
| :--- | :--- |
| **Python** | Core application logic and scripting. |
| **Streamlit** | Creating the local development server and interactive user interface. |
| **GPT4ALL** | Providing a simplified local API server to serve the DeepSeek model. |
| **DeepSeek-R1-Distill-Qwen-1.5B** | The core large language model (LLM) that powers the chatbot. |

-----

## Prerequisites

Ensure the following tools and resources are available before starting the installation:

  * **Python**: Version $\geq 3.10$ recommended.
  * **Pip**: Python's package installer.
  * **GPT4ALL**: The application and model management tool.
  * **Model**: The **DeepSeek-R1-Distill-Qwen-1.5B** model file.
  * **Code Editor**: E.g., [VSCode](https://code.visualstudio.com/).

-----

## Installation and Setup

Follow these steps to set up the project environment and run the chatbot.

### 1\. Set up the Virtual Environment

It's best practice to use a **virtual environment** to manage project dependencies.

```bash
# Create the virtual environment (named 'venv')
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows (Command Prompt):
venv\Scripts\activate
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1
```

### 2\. Install Python Dependencies

With the virtual environment active, install all required packages listed in `requirements.txt`.

```bash
pip install -r requirements.txt
```

### 3\. Configure the Model

This application uses the **DeepSeek-R1-Distill-Qwen-1.5B** model, which must be managed by the GPT4ALL application.

1.  **Download GPT4ALL**: Install the desktop application from the [GPT4ALL documentation site](https://docs.gpt4all.io/index.html).
2.  **Download the Model**:
      * Open the GPT4ALL application.
      * Navigate to the model downloads.
      * Search for and download the `DeepSeek-R1-Distill-Qwen-1.5B` model.
      * *Note: Ensure the model file is saved in the default GPT4ALL model directory or update the model path in your application's configuration file (e.g., `config.py` or similar).*

-----

## Running the Application

Once the environment is set up and the model is configured, you can launch the Streamlit app.

```bash
streamlit run app.py
```

The app will automatically open in your default web browser (usually at `http://localhost:8501`).
