#!/usr/bin/env python3
"""
Startup script for Malicious URL Detector
Initializes the ML model before starting the Flask application
"""

import os
import sys
from app import load_or_create_model, train_model, model_path

def initialize_model():
    """Initialize the machine learning model"""
    print("🚀 Initializing Malicious URL Detector...")
    
    try:
        # Load or create model
        print("📊 Loading/Creating ML model...")
        model_loaded = load_or_create_model()
        
        if model_loaded:
            print("✅ Model loaded successfully")
        else:
            print("🆕 New model created")
        
        # Train model if it doesn't exist
        if not os.path.exists(model_path):
            print("🎯 Training new model...")
            accuracy = train_model()
            print(f"✅ Model trained with accuracy: {accuracy:.2f}")
        else:
            print("✅ Model already exists and trained")
        
        print("🎉 Application ready!")
        return True
        
    except Exception as e:
        print(f"❌ Error during initialization: {e}")
        return False

if __name__ == "__main__":
    success = initialize_model()
    if success:
        print("🚀 Starting Flask application...")
        # Import and run the Flask app
        from app import app
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        print("❌ Failed to initialize application")
        sys.exit(1)
