# Instllation Insructions
## Hugging Face
1) Create an account
2) Go to settigns and generate API token
3) In project, create .env file
4) Create an environment variable named  "HUGGINGFACE_API_TOKEN" and paste in the API token 

## Project Installation
1) clone repo
2) python -m venv env
4) source env/bin/activate
5) pip install transformers
6) pip install datasets
7) pip install python-dotenv
8) pip install torch
9) Run: python3 assignment4.py

If you are an unforunate error, please check the logs. Most likely it is asking to donwgrade numpy.
To do so, run: pip install --force-reinstall -v "numpy<2" , then run the script again.