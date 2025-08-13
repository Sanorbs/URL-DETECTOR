"""
Configuration settings for Malicious URL Detector
"""

import os

class Config:
    """Base configuration class"""
    
    # Flask Configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))
    
    # Model Configuration
    MODEL_PATH = os.environ.get('MODEL_PATH', 'malicious_url_model.pkl')
    FEATURES_PATH = os.environ.get('FEATURES_PATH', 'url_features.csv')
    
    # Security Configuration
    MAX_URL_LENGTH = int(os.environ.get('MAX_URL_LENGTH', 2048))
    
    # Machine Learning Configuration
    RANDOM_STATE = int(os.environ.get('RANDOM_STATE', 42))
    TEST_SIZE = float(os.environ.get('TEST_SIZE', 0.2))
    N_ESTIMATORS = int(os.environ.get('N_ESTIMATORS', 100))
    
    # Suspicious TLDs (Top Level Domains)
    SUSPICIOUS_TLDS = [
        '.tk', '.ml', '.ga', '.cf', '.gq', '.xyz', '.top', 
        '.club', '.online', '.site', '.web', '.tech', '.space'
    ]
    
    # Suspicious keywords commonly used in phishing
    SUSPICIOUS_WORDS = [
        'login', 'signin', 'bank', 'secure', 'account', 'update', 'verify',
        'password', 'credit', 'card', 'paypal', 'ebay', 'amazon', 'google',
        'facebook', 'twitter', 'instagram', 'youtube', 'netflix', 'spotify',
        'microsoft', 'apple', 'netflix', 'chase', 'wells', 'fargo', 'citibank'
    ]
    
    # URL shortener services
    URL_SHORTENERS = [
        'bit.ly', 'tinyurl', 'goo.gl', 't.co', 'is.gd', 'v.gd', 'ow.ly',
        'short.to', 'BudURL.com', 'ping.fm', 'tr.im', 'snipurl.com'
    ]

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    TESTING = False

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    TESTING = False
    
    # Override with production values
    SECRET_KEY = os.environ.get('SECRET_KEY')  # Must be set in production

class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    DEBUG = True
    MODEL_PATH = 'test_model.pkl'
    FEATURES_PATH = 'test_features.csv'

# Configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
