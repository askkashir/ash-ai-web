# Ash AI Flask Web App

A modern, professional AI chat app built with Flask and Google Gemini.

## Running Locally

1. Clone the repo and enter the folder:
   ```bash
   git clone <your-repo-url>
   cd ash-web
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with:
   ```
   FLASK_SECRET_KEY=your-secret-key
   GOOGLE_API_KEY=your-google-api-key
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open [http://localhost:5000](http://localhost:5000) in your browser.

## Environment Variables
- `FLASK_SECRET_KEY`: Secret key for Flask sessions
- `GOOGLE_API_KEY`: Your Google Gemini API key
- `PORT`: (Optional, set by Railway/Heroku/Render)

## Deployment (Railway/Heroku/Render)
- Push your code to GitHub
- Connect your repo to Railway/Heroku/Render
- Set the required environment variables in the platform dashboard
- The app will start with `web: python app.py` (see Procfile)
- The app will use the correct port automatically

## Notes
- Do NOT commit your `.env` or `venv/` folder
- All dependencies are in `requirements.txt`
- The app is ready for both local and cloud deployment
