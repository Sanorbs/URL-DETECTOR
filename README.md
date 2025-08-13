# 🛡️ Malicious URL Detector

A powerful Flask-based cybersecurity application that uses machine learning to detect and predict malicious URLs in real-time. This tool helps protect users from phishing attacks, malware distribution sites, and other cyber threats.

## ✨ Features

- **🔍 Real-time URL Analysis**: Instantly analyze any URL for security threats
- **🤖 Machine Learning Powered**: Uses Random Forest algorithm for accurate detection
- **📊 Feature Extraction**: Analyzes 20+ security-relevant features from URLs
- **🎯 High Accuracy**: Trained on patterns of malicious and benign URLs
- **💻 Beautiful Web Interface**: Modern, responsive UI with real-time feedback
- **📈 Statistics Tracking**: Monitor detection history and success rates
- **🔄 Model Training**: Retrain the ML model to improve accuracy
- **💾 Persistent Storage**: Saves detection results and model data

## 🚀 Technologies Used

- **Backend**: Python, Flask
- **Machine Learning**: Scikit-learn, Random Forest Classifier
- **Data Processing**: Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Model Persistence**: Joblib
- **URL Parsing**: urllib.parse

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │    │   Flask Backend  │    │  ML Model      │
│   (HTML/CSS/JS) │◄──►│   (app.py)      │◄──►│  (Random Forest)│
└─────────────────┘    └──────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │ Feature Extractor│
                       │ (URL Analysis)   │
                       └──────────────────┘
```

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Modern web browser

## 🛠️ Installation

1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd url-detector
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000`

## 🎯 How It Works

### 1. URL Feature Extraction
The application analyzes URLs by extracting 20+ security-relevant features:

- **Basic Features**: URL length, domain length, path length
- **Protocol Features**: HTTPS/HTTP usage
- **Domain Features**: Subdomain count, suspicious TLDs
- **Path Features**: Path depth, file extensions
- **Security Patterns**: Suspicious words, special characters
- **Entropy**: Randomness measurement

### 2. Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Training Data**: Sample malicious and benign URL patterns
- **Features**: 20+ extracted URL characteristics
- **Output**: Binary classification (Safe/Dangerous) with confidence score

### 3. Real-time Detection
- User inputs URL in web interface
- Backend extracts features and runs ML prediction
- Results displayed with confidence level and detailed analysis
- Statistics updated and stored locally

## 🔧 Usage

### Basic URL Detection
1. Enter a URL in the input field
2. Click "🔍 Detect Threats"
3. View results with confidence level
4. Analyze extracted features

### Model Training
1. Click "🔄 Retrain Model" button
2. Wait for training completion
3. View new accuracy score
4. Model automatically saves

### Statistics
- **Total URLs Scanned**: Cumulative count of analyzed URLs
- **Safe URLs**: Count of URLs classified as safe
- **Dangerous URLs**: Count of URLs classified as malicious

## 📊 Feature Analysis

The application analyzes these URL characteristics:

| Feature | Description | Security Relevance |
|---------|-------------|-------------------|
| `url_length` | Total URL length | Longer URLs may indicate obfuscation |
| `https` | HTTPS protocol usage | Secure protocol preference |
| `suspicious_tld` | Suspicious top-level domains | Free TLDs often used for malicious sites |
| `suspicious_words` | Count of suspicious keywords | Phishing attempts often use banking terms |
| `entropy` | URL randomness measure | High entropy may indicate generated URLs |
| `subdomain_count` | Number of subdomains | Excessive subdomains may be suspicious |

## 🚨 Security Features

- **Suspicious TLD Detection**: Identifies risky domain extensions
- **Keyword Analysis**: Detects phishing-related terms
- **Protocol Validation**: Checks for secure connections
- **Pattern Recognition**: Identifies URL obfuscation techniques
- **Entropy Analysis**: Measures URL randomness

## 📁 Project Structure

```
url-detector/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   └── index.html       # Main web interface
├── malicious_url_model.pkl  # Trained ML model (auto-generated)
└── url_features.csv      # Feature storage (auto-generated)
```

## 🔒 Security Considerations

- **Local Processing**: All URL analysis happens locally
- **No External Calls**: URLs are not visited or accessed
- **Feature-Only Analysis**: Only URL structure is analyzed
- **Privacy Preserving**: No user data is stored or transmitted

## 🧪 Testing the Application

### Test URLs to Try:

**Safe URLs:**
- `https://www.google.com`
- `https://www.github.com`
- `https://www.wikipedia.org`

**Suspicious Patterns:**
- `http://malware.example.tk/login/secure/bank/verify`
- `http://phishing.xyz.com/update/account/password`
- `http://scam.ga.com/credit/card/secure`

## 🚀 Future Enhancements

- **Real-time Threat Intelligence**: Integration with security APIs
- **Advanced ML Models**: Deep learning and ensemble methods
- **Browser Extension**: Chrome/Firefox add-on for real-time protection
- **API Endpoints**: RESTful API for integration with other tools
- **Bulk Analysis**: Multiple URL analysis capabilities
- **Custom Training**: User-defined malicious URL patterns

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This tool is for educational and research purposes. While it can help identify potentially malicious URLs, it should not be the sole method of cybersecurity protection. Always use multiple security layers and stay updated with the latest threats.

## 🆘 Support

If you encounter any issues or have questions:
1. Check the console output for error messages
2. Ensure all dependencies are installed correctly
3. Verify Python version compatibility
4. Check if the Flask server is running on the correct port

---

**Built with ❤️ for cybersecurity education and protection**
# URL-DETECTOR
