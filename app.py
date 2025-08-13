from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os
from urllib.parse import urlparse
import re
import requests
from datetime import datetime
import json

app = Flask(__name__)

# Global variables
model = None
model_path = 'malicious_url_model.pkl'
features_path = 'url_features.csv'

class URLFeatureExtractor:
    """Extract features from URLs for malicious detection"""
    
    def __init__(self):
        self.suspicious_words = [
            'login', 'signin', 'bank', 'secure', 'account', 'update', 'verify',
            'password', 'credit', 'card', 'paypal', 'ebay', 'amazon', 'google',
            'facebook', 'twitter', 'instagram', 'youtube', 'netflix', 'spotify'
        ]
        
        self.suspicious_tlds = [
            '.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', '.club', '.online'
        ]
    
    def extract_features(self, url):
        """Extract all features from a URL"""
        try:
            parsed = urlparse(url)
            
            features = {}
            
            # Basic URL features
            features['url_length'] = len(url)
            features['domain_length'] = len(parsed.netloc)
            features['path_length'] = len(parsed.path)
            features['query_length'] = len(parsed.query)
            
            # Protocol features
            features['https'] = 1 if parsed.scheme == 'https' else 0
            features['http'] = 1 if parsed.scheme == 'http' else 0
            
            # Domain features
            features['subdomain_count'] = len(parsed.netloc.split('.')) - 1
            features['has_subdomain'] = 1 if len(parsed.netloc.split('.')) > 2 else 0
            
            # TLD features
            features['suspicious_tld'] = 1 if any(tld in parsed.netloc for tld in self.suspicious_tlds) else 0
            
            # Path features
            features['path_depth'] = len([x for x in parsed.path.split('/') if x])
            features['has_file_extension'] = 1 if '.' in parsed.path.split('/')[-1] else 0
            
            # Query features
            features['query_count'] = len(parsed.query.split('&')) if parsed.query else 0
            features['has_parameters'] = 1 if parsed.query else 0
            
            # Suspicious patterns
            features['suspicious_words'] = sum(1 for word in self.suspicious_words if word.lower() in url.lower())
            features['digit_count'] = sum(c.isdigit() for c in url)
            features['special_char_count'] = sum(1 for c in url if c in '!@#$%^&*()_+-=[]{}|;:,.<>?')
            
            # URL structure features
            features['has_redirect'] = 1 if 'redirect' in url.lower() or 'go' in url.lower() else 0
            features['has_shortener'] = 1 if any(short in url.lower() for short in ['bit.ly', 'tinyurl', 'goo.gl']) else 0
            
            # Entropy (randomness measure)
            features['entropy'] = self._calculate_entropy(url)
            
            return features
            
        except Exception as e:
            print(f"Error extracting features: {e}")
            return None
    
    def _calculate_entropy(self, text):
        """Calculate Shannon entropy of text"""
        if not text:
            return 0
        
        prob = [float(text.count(c)) / len(text) for c in set(text)]
        entropy = -sum(p * np.log2(p) for p in prob if p > 0)
        return entropy

def load_or_create_model():
    """Load existing model or create a new one"""
    global model
    
    if os.path.exists(model_path):
        try:
            model = joblib.load(model_path)
            print("Model loaded successfully")
            return True
        except Exception as e:
            print(f"Error loading model: {e}")
    
    # Create a new model if none exists
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    print("New model created")
    return False

def train_model():
    """Train the model with sample data"""
    global model
    
    # Create sample training data (in real scenario, you'd use actual malicious/benign URLs)
    sample_urls = [
        # Benign URLs
        "https://www.google.com",
        "https://www.github.com",
        "https://www.stackoverflow.com",
        "https://www.wikipedia.org",
        "https://www.microsoft.com",
        "https://www.apple.com",
        "https://www.amazon.com",
        "https://www.netflix.com",
        "https://www.spotify.com",
        "https://www.youtube.com",
        
        # Malicious URLs (examples - these are patterns, not real malicious URLs)
        "http://malware.example.tk/login/secure/bank/verify",
        "http://phishing.xyz.com/update/account/password",
        "http://scam.ga.com/credit/card/secure",
        "http://fake.cf.com/paypal/ebay/amazon",
        "http://suspicious.ml.com/google/facebook/twitter",
        "http://dangerous.gq.com/instagram/youtube/netflix",
        "http://malicious.top.com/spotify/account/verify",
        "http://harmful.club.com/login/signin/secure",
        "http://risky.online.com/bank/credit/update",
        "http://threat.xyz.com/password/account/secure"
    ]
    
    # Labels: 0 for benign, 1 for malicious
    labels = [0] * 10 + [1] * 10
    
    # Extract features
    extractor = URLFeatureExtractor()
    features_list = []
    
    for url in sample_urls:
        features = extractor.extract_features(url)
        if features:
            features_list.append(list(features.values()))
    
    # Convert to numpy array
    X = np.array(features_list)
    y = np.array(labels)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train model
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"Model trained with accuracy: {accuracy:.2f}")
    
    # Save model
    joblib.dump(model, model_path)
    
    return accuracy

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_url():
    """Detect if a URL is malicious"""
    try:
        data = request.get_json()
        url = data.get('url', '').strip()
        
        if not url:
            return jsonify({'error': 'URL is required'}), 400
        
        # Check if model is loaded
        if model is None:
            print("ERROR: Model is None in detect_url")
            return jsonify({'error': 'Model not loaded'}), 500
        
        print(f"Model type: {type(model)}")
        print(f"Model loaded: {model is not None}")
        
        # Extract features
        extractor = URLFeatureExtractor()
        features = extractor.extract_features(url)
        
        if features is None:
            return jsonify({'error': 'Invalid URL format'}), 400
        
        # Prepare features for prediction
        feature_values = list(features.values())
        feature_array = np.array(feature_values).reshape(1, -1)
        
        print(f"Feature array shape: {feature_array.shape}")
        print(f"Feature values: {feature_values}")
        
        # Make prediction
        try:
            prediction = model.predict(feature_array)[0]
            probability = model.predict_proba(feature_array)[0]
            
            result = {
                'url': url,
                'is_malicious': bool(prediction),
                'confidence': float(max(probability)),
                'features': features,
                'timestamp': datetime.now().isoformat()
            }
            
            # Save to features file for future training
            save_features_to_csv(url, features, prediction)
            
            return jsonify(result)
            
        except Exception as pred_error:
            print(f"Prediction error: {pred_error}")
            return jsonify({'error': f'Prediction failed: {str(pred_error)}'}), 500
            
    except Exception as e:
        print(f"General error in detect_url: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train():
    """Train the model"""
    try:
        # Force retrain by removing old model
        if os.path.exists(model_path):
            os.remove(model_path)
            print("Removed old model for retraining")
        
        accuracy = train_model()
        return jsonify({
            'message': 'Model trained successfully',
            'accuracy': accuracy
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/force-retrain', methods=['POST'])
def force_retrain():
    """Force retrain the model (useful for version conflicts)"""
    try:
        global model
        
        # Remove old model
        if os.path.exists(model_path):
            os.remove(model_path)
            print("Removed old model for forced retraining")
        
        # Reset model variable
        model = None
        
        # Create and train new model
        load_or_create_model()
        accuracy = train_model()
        
        return jsonify({
            'message': 'Model force retrained successfully',
            'accuracy': accuracy,
            'status': 'ready'
        })
        
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/status')
def status():
    """Get model status"""
    return jsonify({
        'model_loaded': model is not None,
        'model_path': model_path,
        'features_path': features_path
    })

@app.route('/startup')
def startup():
    """Initialize the application and train model if needed"""
    try:
        global model
        
        # Always retrain model in production to avoid version conflicts
        if os.environ.get('FLASK_ENV') == 'production':
            # Remove old model to force retraining
            if os.path.exists(model_path):
                os.remove(model_path)
                print("Removed old model for retraining")
        
        # Load or create model if not exists
        if model is None:
            load_or_create_model()
        
        # Train model if it doesn't exist
        if not os.path.exists(model_path):
            accuracy = train_model()
            return jsonify({
                'message': 'Application started successfully',
                'model_trained': True,
                'accuracy': accuracy,
                'status': 'ready'
            })
        else:
            return jsonify({
                'message': 'Application started successfully',
                'model_trained': True,
                'accuracy': 'Model already exists',
                'status': 'ready'
            })
            
    except Exception as e:
        return jsonify({
            'error': str(e),
            'status': 'error'
        }), 500

@app.route('/health')
def health():
    """Simple health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'model_loaded': model is not None
    })

def save_features_to_csv(url, features, label):
    """Save extracted features to CSV for future training"""
    try:
        data = {
            'url': [url],
            'label': [label],
            'timestamp': [datetime.now().isoformat()]
        }
        
        # Add features
        for key, value in features.items():
            data[key] = [value]
        
        df = pd.DataFrame(data)
        
        if os.path.exists(features_path):
            df.to_csv(features_path, mode='a', header=False, index=False)
        else:
            df.to_csv(features_path, index=False)
            
    except Exception as e:
        print(f"Error saving features: {e}")

if __name__ == '__main__':
    # Load or create model on startup
    load_or_create_model()
    
    # Train model if it's new (only in development)
    if os.environ.get('FLASK_ENV') == 'development':
        if model is not None and not os.path.exists(model_path):
            train_model()
    
    # Production settings
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(debug=debug_mode, host='0.0.0.0', port=port)
