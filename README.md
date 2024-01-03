# The AI Brain Project

The AI Brain Project is a Python program that demonstrates how to use OpenAI's GPT-3 language model to upload your brain to the cloud. The program asks the user for a name and generates random actions every 5 seconds, along with a random sentence using the GPT-3 model based on certain context. The program also allows the user to load custom context from a file. Think of it as [HLE](https://en.wikipedia.org/wiki/UltraHLE) for [brain emulation/mind uploading](https://en.wikipedia.org/wiki/Mind_uploading).

## Installation

To install the program, follow these steps:

Clone the repository:

```
git clone https://github.com/yourusername/ai-brain-project.git
```

Install the required Python packages:

```
pip install -r requirements.txt
```

Set up your OpenAI API key and name using the OpenAI Secret Manager. See the section on "Using the OpenAI Secret Manager" for more information.

Run the program:

```
python main.py
```

## Usage

When you run the program, it will ask you for a name. Enter your name and press Enter. The program will then start generating actions and GPT-3 sentences every 5 seconds.

You can also load custom context from a file by placing a file named custom-context.txt in the same directory as main.py. The program will automatically load the context from the file if it exists.

Using the OpenAI Secret Manager
To keep your OpenAI API key and name secure, you can use the OpenAI Secret Manager to store them securely. To do this, follow these steps:

Create an account on the OpenAI website if you haven't already done so.

Log in to the OpenAI website and go to the "API keys" page.

Click "Generate new API key" to create a new API key.

Install the openai_secret_manager Python package:

```
pip install openai_secret_manager
```

Import the openai_secret_manager module in your Python code:

```
import openai_secret_manager
```

Use the openai_secret_manager.get_secret function to retrieve your API key and name (already in the code):

```
secrets = openai_secret_manager.get_secret("my_app_name")
openai.api_key = secrets["api_key"]
name = secrets["name"]
```

In the OpenAI Secret Manager, create a new secret with the name my_app_name and your API key and name as the values. You can also add other keys if needed.

Creating a new secret in the OpenAI Secret Manager

Save the secret in the OpenAI Secret Manager.

## License

The AI Brain Project is licensed under the MIT License. See the LICENSE file for more information.

## Possible future impementations (for people who would like to contrib!)

* An semi-decentralized API for the AI using GUN-DB?
* A ROBLOX Metaverse based on the API?
