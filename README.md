# Langchain API Project
# Essay-x-Poem-Writer-Using-LLAMA-3

## Project Overview
This project implements a simple API server using FastAPI to interact with a language model from LangChain (LLAMA3) and a Streamlit-based GUI for generating essays and poems.

# Required
you need to install ollama and also need to download llama3 Model for running it

## Features
- Generate well-formatted essays on a given topic using LLAMA3.
- Generate well-formatted poems on a given topic using LLAMA3.
- Easy-to-use web interface with Streamlit.
- Simple API routes for essay and poem generation.

## Installation

### Prerequisites
- Python 3.8 or higher
- FastAPI
- Uvicorn
- Streamlit
- Requests
- Dotenv
- LangChain
- LangChain Community LLMS
- LangServe

### Setup
1. Clone the repository:
    ```sh
    git clone https://github.com/Rishurajgautam24/Essay-x-Poem-Writer-Using-LLAMA-3.git
    cd Essay-x-Poem-Writer-Using-LLAMA-3
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and add your LangChain API key:
    ```plaintext
    LANGCHAIN_API_KEY=your_api_key_here
    ```

## Running the Project

### Start the API Server
1. Run the FastAPI server:
    ```sh
    python api.py
    ```

### Start the Streamlit GUI
1. Run the Streamlit application:
    ```sh
    streamlit run gui.py
    ```

## Usage

### Essay Generation
1. Open the Streamlit GUI in your web browser.
2. Select the "Essay writer" option from the sidebar.
3. Enter a topic for the essay and press Enter.
4. The generated essay will be displayed on the page.

### Poem Generation
1. Open the Streamlit GUI in your web browser.
2. Select the "Poem writer" option from the sidebar.
3. Enter a topic for the poem and press Enter.
4. The generated poem will be displayed on the page.

## API Endpoints

### Essay Endpoint
- **URL**: `/essay/invoke`
- **Method**: `POST`
- **Payload**: 
    ```json
    {
        "input": {"topic": "your_topic_here"}
    }
    ```
- **Response**:
    ```json
    {
        "output": "Generated essay text"
    }
    ```

### Poem Endpoint
- **URL**: `/poem/invoke`
- **Method**: `POST`
- **Payload**: 
    ```json
    {
        "input": {"topic": "your_topic_here"}
    }
    ```
- **Response**:
    ```json
    {
        "output": "Generated poem text"
    }
    ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your improvements.


## Authors
- Rishu Raj Gautam


## Contact
For any inquiries, please contact [Rishujob24@gmail.com].

