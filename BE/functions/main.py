# Welcome to Cloud Functions for Firebase for Python!
# To get started, simply uncomment the below code or create your own.
# Deploy with `firebase deploy`
# import * as functions from "firebase-functions"
# import * as admin from "firebase-admin"
# admin.initialize_app()


# @https_fn.on_request()
# def on_request_example(req: https_fn.Request) -> https_fn.Response:
#     return https_fn.Response("Hello world!")
#######################################################
import firebase_admin
from firebase_admin import credentials
from firebase_functions import https_fn
from flask import Flask, request, jsonify
from aiko import LLM

# Initialize Firebase app
firebase_admin.initialize_app()

# Initialize LLM
llm = LLM()

def create_app():
    app = Flask(__name__)

    @app.route("/chat", methods=["POST"])
    def handle_chat_request():
        if request.method != "POST":
            return jsonify({"error": "Send a POST request"}), 405
        
        try:
            request_json = request.get_json()
            if not request_json:
                return jsonify({"error": "Invalid JSON"}), 400
            
            user_input = request_json.get("message")
            if not user_input:
                return jsonify({"error": "Missing 'message' in request"}), 400
            
            response = llm.chat_single_turn(user_input)
            return jsonify({"response": response}), 200
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return app

@https_fn.on_request()
def chat_function(request: https_fn.Request) -> https_fn.Response:
    app = create_app()
    return app(request.environ, lambda status, headers, body: (status, headers, [body]))

# # The Cloud Functions for Firebase SDK to create Cloud Functions and set up triggers.
# from firebase_functions import firestore_fn, https_fn

# # The Firebase Admin SDK to access Cloud Firestore.
# from firebase_admin import initialize_app, firestore
# import google.cloud.firestore

# app = initialize_app()


# @https_fn.on_request()
# def addmessage(req: https_fn.Request) -> https_fn.Response:
#     """Take the text parameter passed to this HTTP endpoint and insert it into
#     a new document in the messages collection."""
#     # Grab the text parameter.
#     original = req.args.get("text")
#     if original is None:
#         return https_fn.Response("No text parameter provided", status=400)

#     firestore_client: google.cloud.firestore.Client = firestore.client()

#     # Push the new message into Cloud Firestore using the Firebase Admin SDK.
#     _, doc_ref = firestore_client.collection("messages").add({"original": original})

#     # Send back a message that we've successfully written the message
#     return https_fn.Response(f"Message with ID {doc_ref.id} added.")


# @firestore_fn.on_document_created(document="messages/{pushId}")
# def makeuppercase(event: firestore_fn.Event[firestore_fn.DocumentSnapshot | None]) -> None:
#     """Listens for new documents to be added to /messages. If the document has
#     an "original" field, creates an "uppercase" field containg the contents of
#     "original" in upper case."""

#     # Get the value of "original" if it exists.
#     if event.data is None:
#         return
#     try:
#         original = event.data.get("original")
#     except KeyError:
#         # No "original" field, so do nothing.
#         return

#     # Set the "uppercase" field.
#     print(f"Uppercasing {event.params['pushId']}: {original}")
#     upper = original.upper()
#     event.data.reference.update({"uppercase": upper})
