# ARTI RASA Extended

Extending a RASA chatbot with chatGPT

![cool chatbot image goes here](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmiro.medium.com%2Fmax%2F2340%2F0*qYjiu3m00IWQBr2-.jpg&f=1&nofb=1&ipt=81728de2e459cd7766263c607a671fb1e415bf9b1545f7f666ef90fdfcda17e7&ipo=images)

Run a RASA chatbot and a RASA action server and let yourself be quizzed on basic infosec topics. Forwards generic queries to ChatGPT.
Requires a valid auth token for the openAI platform.

# Installation

```
pip install -r requirements.txt
```

# Basic Usage

From the root directory of the repo:
Provide your openAI API key by creating a .env file with the following format:

```
OPENAI_KEY=sk-abcdefghij.......
```

Launch the actions server (port 5055)
```
rasa run actions
```

Run the main rasa application (port 5005)
```
rasa run -m models --enable-api --cors "*"
```

Run the webpage serving the webinterface for the chatbot (port 8080)
```
python main.py
```

Open http://localhost:8080 with your browser and start chatting.
