import os
from flask import Flask, render_template, request, session, jsonify, redirect, url_for
from flask.sessions import SecureCookieSessionInterface
from datetime import timedelta
import uuid
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import AshAI and extract_user_name from the original app.py (copy the relevant classes and functions here)
# ... (AshAI, AdvancedSessionState, etc. go here, unchanged except for session storage)

# For brevity, only the Flask integration and session logic is shown here. In the real file, copy all AshAI logic from your CLI app.py.

from app import AshAI, extract_user_name  # If you modularize, otherwise copy-paste the classes here

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', str(uuid.uuid4()))
app.permanent_session_lifetime = timedelta(days=7)

# Helper to get or create AshAI in session

def get_ash():
    if 'ash' not in session:
        session['ash'] = {}
        session['history'] = []
    return session['ash']

def get_history():
    return session.get('history', [])

def set_history(history):
    session['history'] = history

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", history=get_history())

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get('message', '').strip()
    if not user_input:
        return jsonify({'error': 'Empty message'}), 400
    # Load AshAI from session or create new
    if 'ash_ai' not in session:
        session['ash_ai'] = None  # Placeholder for AshAI object
    # For stateless demo, create new AshAI each time (or use pickle for real session persistence)
    ash = AshAI()
    # Restore conversation history
    for speaker, msg in get_history():
        if speaker == 'user':
            ash.session.conversation_history.append(('user', msg))
        else:
            ash.session.conversation_history.append(('ash', msg))
    # Name detection
    detected_name = extract_user_name(user_input)
    if detected_name and not ash.session.user_profile.name:
        ash.session.update_user_profile(detected_name)
        ash_reply = f"Nice to meet you, {detected_name}. I'm Ash, and I'm genuinely glad you're here."
    else:
        ash_reply = ash.generate_response(user_input)
    # Update session history
    history = get_history()
    history.append(('user', user_input))
    history.append(('ash', ash_reply))
    set_history(history[-20:])  # Keep last 20
    return jsonify({'reply': ash_reply})

@app.route("/reset", methods=["POST"])
def reset():
    session.pop('history', None)
    session.pop('ash_ai', None)
    return jsonify({'result': 'reset'})

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
