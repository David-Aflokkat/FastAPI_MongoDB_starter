# FastAPI_MongoDB_starter

Quick starter for FastAPI connection with a MongoDB database.

-> First you need to create a database on MongoDB website.
you'll get the liknk to your new database:
"mongodb+srv://"user">:"password">@clustertest.egpmhqq.mongodb.netretryWrites=true&w=majority". The "User" and "Password" should be field with the informations you provided at the creation of your database.

-> Then go to Config/dataBase.py and change the link with your informations

-> you need to activate the virtual environnement, to do so execute this command: "./env/scripts/activate"

-> to start the server open the terminal and write the command: "uvicorn main:app --reload"

-> open your browser on http://127.0.0.1:8000/docs you'll find the interface to the database.

ENJOY :D
