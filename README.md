# Welcome to my fastAPI project!
This API is being developed as a centralized source for performing CRUD operations on my school-related information, including study, course, and grade data. I am doing this for fun, as I really enjoy making API's.

----------------------------------------------
The .env file should have the content of and be at the root.
POSTGRES_USER=""
POSTGRES_PASSWORD=""
POSTGRES_SERVER=""
POSTGRES_DB=""

I used a local PostgreSQL 16 database myself, and if someone wants to use my API they just have to make an instance of a database and add the info to an .env file.

-----------------------------------------------
Prerequisites:
Make sure you have python and pip installed on your computer. You can verify by running the commands: <br>
`python --version`<br>
`pip --version`

The steps to take for cloning the project
1. Clone the repository:<br>
  `git clone https://github.com/sandraliv/fastAPI-ferilskra.git `<br>
  2. I recommend creating a virtual environemtn which isolates the project dependencies to avoid conflict with your own global packages.<br>
  `python -m venv .venv `<br>
  `source .venv/bin/activate` #On macOS/Linuz<br>
  `.venv\Scripts\activate` #Windows<br>
2. Use pip to install the packages listed in requirements.txt<br>
`pip install -r requirements.txt`<br>
3. And to run the application on a server<br>
`uvicorn main:app --reload`<br>

After starting the server, you can access the SwaggerUI on http://127.0.0.1:8000/docs#/
