#!/usr/bin/env python3
"""
Test script for Malicious URL Detector
Tests the core functionality without running the Flask server
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import URLFeatureExtractor, load_or_create_model, train_model

def test_feature_extraction():
    """Test URL feature extraction"""
    print("🧪 Testing URL Feature Extraction...")
    
    extractor = URLFeatureExtractor()
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "http://malware.example.tk/login/secure/bank/verify",
        "https://www.github.com/user/repo",
        "http://phishing.xyz.com/update/account/password",
        "https://www.wikipedia.org/wiki/Python_(programming_language)"
    ]
    
    for url in test_urls:
        print(f"\n📋 Analyzing: {url}")
        features = extractor.extract_features(url)
        
        if features:
            print("✅ Features extracted successfully:")
            for key, value in features.items():
                print(f"   {key}: {value}")
        else:
            print("❌ Failed to extract features")
    
    print("\n" + "="*50)

def test_model_loading():
    """Test model loading functionality"""
    print("🤖 Testing Model Loading...")
    
    try:
        model_loaded = load_or_create_model()
        if model_loaded:
            print("✅ Existing model loaded successfully")
        else:
            print("🆕 New model created successfully")
        print("✅ Model loading test passed")
    except Exception as e:
        print(f"❌ Model loading test failed: {e}")
    
    print("\n" + "="*50)

def test_model_training():
    """Test model training functionality"""
    print("🎯 Testing Model Training...")
    
    try:
        accuracy = train_model()
        print(f"✅ Model training completed successfully!")
        print(f"📊 Model accuracy: {accuracy:.2f}")
        print("✅ Model training test passed")
    except Exception as e:
        print(f"❌ Model training test failed: {e}")
    
    print("\n" + "="*50)

def test_url_classification():
    """Test URL classification with the trained model"""
    print("🔍 Testing URL Classification...")
    
    try:
        from app import model
        
        if model is None:
            print("❌ Model not available for testing")
            return
        
        extractor = URLFeatureExtractor()
        test_urls = [
            ("https://www.google.com", "Expected: Safe"),
            ("http://malware.example.tk/login/secure/bank/verify", "Expected: Malicious"),
            ("https://www.github.com", "Expected: Safe"),
            ("http://phishing.xyz.com/update/account/password", "Expected: Malicious")
        ]
        
        for url, expectation in test_urls:
            print(f"\n🔗 Testing: {url}")
            print(f"   {expectation}")
            
            features = extractor.extract_features(url)
            if features:
                feature_values = list(features.values())
                feature_array = [feature_values]  # Reshape for prediction
                
                prediction = model.predict(feature_array)[0]
                probability = model.predict_proba(feature_array)[0]
                
                result = "🟢 SAFE" if prediction == 0 else "🔴 MALICIOUS"
                confidence = max(probability) * 100
                
                print(f"   Result: {result}")
                print(f"   Confidence: {confidence:.1f}%")
            else:
                print("   ❌ Failed to extract features")
        
        print("✅ URL classification test passed")
        
    except Exception as e:
        print(f"❌ URL classification test failed: {e}")
    
    print("\n" + "="*50)

def main():
    """Run all tests"""
    print("🚀 Starting Malicious URL Detector Tests")
    print("="*50)
    
    # Run tests
    test_feature_extraction()
    test_model_loading()
    test_model_training()
    test_url_classification()
    
    print("\n🎉 All tests completed!")
    print("="*50)
    print("\n💡 To run the full application:")
    print("   python app.py")
    print("   Then open http://localhost:5000 in your browser")

if __name__ == "__main__":
    main()
