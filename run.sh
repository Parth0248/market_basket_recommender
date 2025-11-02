#!/bin/bash

echo "=================================================="
echo "Market Basket Recommendation System - Setup"
echo "CMPE 256 - San José State University"
echo "=================================================="
echo ""

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source .venv/Scripts/activate

# Install dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "✅ Dependencies installed successfully!"
echo ""

# Train the model
echo "🧠 Training recommendation model..."
python recommender.py

echo ""
echo "✅ Model trained successfully!"
echo ""

# Start the server
echo "🚀 Starting FastAPI server..."
echo ""
echo "=================================================="
echo "Server will be available at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo "=================================================="
echo ""

python app.py
