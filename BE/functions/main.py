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
# import os
# from firebase_admin import credentials, initialize_app
# from firebase_functions import https_fn
# from flask import Flask, request, jsonify
# from aiko import LLM
# from werkzeug.middleware.proxy_fix import ProxyFix
# from flask_cors import CORS
# # Initialize Firebase app
# initialize_app()

# # Initialize LLM
# llm = LLM()

# app = Flask(__name__)
# CORS(app)

# @app.route("/", methods=["POST"])
# @https_fn.on_call()
# def handle_chat_request():
#     if request.method != "POST":
#         return jsonify({"error": "Send a POST request"}), 405

#     try:
#         request_json = request.get_json()
#         if not request_json:
#             return jsonify({"error": "Invalid JSON"}), 400

#         user_input = request_json.get("message")
#         if not user_input:
#             return jsonify({"error": "Missing 'message' in request"}), 400

#         response = llm.chat(user_input)
#         return jsonify({"response": response}), 200

#     except Exception as e:
#         print(e)
#         return jsonify({"error": str(e)}), 500

################################################################################
# # Apply ProxyFix middleware
# app.wsgi_app = ProxyFix(
#     app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
# )

# @https_fn.on_request()
# def chat_function(request: https_fn.Request) -> https_fn.Response:
#     return app(request.environ, lambda status, headers, body: (status, headers, [body]))

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


# # import os

# # from flask import Flask, request, jsonify
# # from aiko import LLM
# # from firebase_functions import https_fn


# # llm = LLM()
# # app = Flask(__name__)

# # # @https_fn.on_request()
# # @app.route("/", methods=["POST"])
# # def chat():
# #     # request_json = request.get_json()
# #     # if not request_json:
# #     #     return jsonify({"error": "Invalid JSON"}), 400

# #     # user_input = request_json.get("message")
# #     # if not user_input:
# #     #    return jsonify({"error": "Missing 'message' in request"}), 400

# #     # response = llm.chat(user_input)
# #     # return jsonify({"response": response}), 200


# # if __name__ == "__main__":
# #     app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT")))


# # Copyright 2023 Google Inc. All Rights Reserved.
# #
# # Licensed under the Apache License, Version 2.0 (the "License");
# # you may not use this file except in compliance with the License.
# # You may obtain a copy of the License at
# #
# #      http://www.apache.org/licenses/LICENSE-2.0
# #
# # Unless required by applicable law or agreed to in writing, software
# # distributed under the License is distributed on an "AS IS" BASIS,
# # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# # See the License for the specific language governing permissions and
# # limitations under the License.

# # [START httpflaskexample]
# from firebase_admin import initialize_app, db
# from firebase_functions import https_fn
# import flask

# initialize_app()
# app = flask.Flask(__name__)

# # Build multiple CRUD interfaces:


# @app.get("/widgets")
# @app.get("/widgets/<id>")
# def get_widget(id=None):
#     if id is not None:
#         return db.reference(f"/widgets/{id}").get()
#     else:
#         return db.reference("/widgets").get()


# @app.post("/widgets")
# def add_widget():
#     new_widget = flask.request.get_data(as_text=True)
#     db.reference("/widgets").push(new_widget)
#     return flask.Response(status=201, response="Added widget")


# # Expose Flask app as a single Cloud Function:


# @https_fn.on_request()
# def httpsflaskexample(req: https_fn.Request) -> https_fn.Response:
#     with app.request_context(req.environ):
#         return app.full_dispatch_request()
# # [END httpflaskexample]

# from firebase_admin import initialize_app, db
# from firebase_functions import https_fn
# from flask import Flask, request, jsonify
# from aiko import LLM
# import os
# from flask_cors import CORS
# # Initialize Firebase Admin SDK
# initialize_app()

# # Create a Flask app instance
# app = Flask(__name__)
# CORS(app)
# # Initialize the LLM instance
# llm = LLM()


# @app.route("/chat", methods=["POST"])
# def chat():
#     request_json = request.get_json()
#     user_input = request_json.get("message")
#     response = llm.chat_single_turn(user_input)
#     return jsonify({"response": response}), 200


# @https_fn.on_request()
# def httpsflaskexample(req: https_fn.Request) -> https_fn.Response:
#     with app.request_context(req.environ):
#         return app.full_dispatch_request()
    


    # LOCAL DEV
# port = int(os.environ.get("PORT", 8080))
# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=port)
# The app.run block is not needed for Firebase Functions


from firebase_admin import initialize_app, db
from firebase_functions import https_fn
from flask import Flask, request, jsonify
from aiko import LLM
import os
from flask_cors import CORS, cross_origin
# Initialize Firebase Admin SDK
initialize_app()

# Create a Flask app instance
app = Flask(__name__)
CORS(app,  resources={r"/*": {"origins": "*"}})
# CORS(app)
# Initialize the LLM instance
llm = LLM()



@cross_origin(supports_credentials=True)
@app.route("/chat", methods=["POST"])
def chat():
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'message' in request_json:
        user_input = request_json['message']
    elif request_args and 'name' in request_args:
        user_input = request_args['message']
    else:
        user_input = '${this is system settings, user failed to send the message}'
    # return 'Hello', user_input

    # response = llm.chat(user_input)

    response = llm.chat(user_input)
    resp = flask.jsonify({"response": response})
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp
    # return jsonify({"response": response}), 200


