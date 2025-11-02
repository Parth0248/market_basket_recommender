@echo off
echo ==================================================
echo Market Basket Recommendation System - Setup
echo CMPE 256 - San Jose State University
echo ==================================================
echo.

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo Dependencies installed successfully!
echo.

REM Train the model
echo Training recommendation model...
python recommender.py

echo.
echo Model trained successfully!
echo.

REM Start the server
echo Starting FastAPI server...
echo.
echo ==================================================
echo Server will be available at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo ==================================================
echo.

python app.py
