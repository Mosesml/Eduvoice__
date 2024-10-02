# EduVoice_
Chatbot with LangChain and Ollama
This repository contains a chatbot implementation using LangChain and Ollama, an open-source large language model (LLM). Follow the steps below to set up your environment and run the chatbot.

# Prerequisites
Python 3.7 or higher
pip (Python package installer)
A virtual environment tool (e.g., venv)


# Installation
1. Clone the Repository
First, clone this repository to your local machine:

git clone https://github.com/Mosesml/EduVoice_.git
cd your-repository


# 2. Create and Activate a Virtual Environment
Create a virtual environment to manage project dependencies:

python3 -m venv chatbot-env
Activate the virtual environment:

On macOS/Linux:

source chatbot-env/bin/activate

# 3. Install Dependencies
Install the required Python packages using pip:

pip install langchain langchain-ollama ollama

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project’s coding standards and includes appropriate documentation.

Feel free to adjust the details according to your specific setup or project needs.






# EduVoice
EduVoice is a web application designed to convert speech transcripts into organized notes. This project includes a frontend interface and a backend API. The frontend allows users to upload a PDF transcript, while the backend processes the PDF and generates summarized notes.

# Prerequisites
Ensure you have the following installed:

Python 3.12 or later
Node.js 
Installation
Backend Setup
Clone the Repository

git clone https://github.com/yourusername/eduvoice.git
cd eduvoice


Create a Virtual Environment

python -m venv venv
Activate the Virtual Environment

On macOS/Linux:

source venv/bin/activate

Install Required Python Packages

pip install -r requirements.txt
Download NLTK Data

Run the following Python command to download the necessary NLTK data:

python -c "import nltk; nltk.download('punkt')"
