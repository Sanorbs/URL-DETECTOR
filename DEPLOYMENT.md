# 🚀 Deployment Guide - Malicious URL Detector

This guide will help you deploy your Flask application to various free hosting platforms.

## 📋 Prerequisites

- GitHub account (free)
- Python 3.7+ installed locally
- Git installed locally

## 🎯 **Option 1: Render (Recommended - Easiest)**

### Step 1: Prepare Your Code
1. **Push to GitHub** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 2: Deploy on Render
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure the service:
   - **Name**: `malicious-url-detector`
   - **Environment**: `Python 3.11`
   - **Build Command**: `pip install -r requirements-prod.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

### Step 3: Environment Variables (Optional)
Add these in Render dashboard:
- `FLASK_ENV`: `production`
- `SECRET_KEY`: `your-secret-key-here`

### Step 4: Deploy
Click "Create Web Service" and wait for deployment!

**Your app will be available at**: `https://your-app-name.onrender.com`

---

## 🌐 **Option 2: Railway**

### Step 1: Deploy on Railway
1. Go to [railway.app](https://railway.app) and sign up
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Railway will auto-detect it's a Python app

### Step 2: Configure
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`

**Your app will be available at**: `https://your-app-name.railway.app`

---

## 🐍 **Option 3: PythonAnywhere**

### Step 1: Sign Up
1. Go to [pythonanywhere.com](https://pythonanywhere.com)
2. Create a free account

### Step 2: Upload Code
1. Go to "Files" tab
2. Upload your project files or clone from GitHub
3. Go to "Web" tab → "Add a new web app"

### Step 3: Configure
1. Choose "Flask" framework
2. Set Python version to 3.9
3. Set source code directory to your project folder
4. Set WSGI configuration file to point to your app

**Your app will be available at**: `https://yourusername.pythonanywhere.com`

---

## 🚀 **Option 4: Heroku (Paid but Popular)**

### Step 1: Install Heroku CLI
```bash
# Windows
winget install --id=Heroku.HerokuCLI

# macOS
brew tap heroku/brew && brew install heroku
```

### Step 2: Deploy
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

---

## 🔧 **Production Configuration**

### Update app.py for Production
```python
if __name__ == '__main__':
    # Load or create model on startup
    load_or_create_model()
    
    # Train model if it's new
    if model is not None and not os.path.exists(model_path):
        train_model()
    
    # Production settings
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
```

### Environment Variables
Create a `.env` file for local development:
```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-here
```

---

## 📱 **Mobile App Deployment**

### Option 1: PWA (Progressive Web App)
Your app already works on mobile! Just add a manifest file:

```json
{
  "name": "Malicious URL Detector",
  "short_name": "URL Detector",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#667eea",
  "theme_color": "#764ba2"
}
```

### Option 2: Flutter Web
Convert to Flutter for native mobile apps.

---

## 🚨 **Important Notes**

### Free Tier Limitations
- **Render**: Sleeps after 15 minutes inactivity
- **Railway**: $5 monthly credit limit
- **PythonAnywhere**: Limited CPU and storage
- **Heroku**: No free tier

### Performance Tips
1. **Model Caching**: Models are loaded once and cached
2. **Feature Extraction**: Optimized for speed
3. **Static Assets**: CSS/JS are minified and cached

### Security Considerations
- ✅ All processing is local
- ✅ No external API calls
- ✅ HTTPS enforced on all platforms
- ⚠️ Update dependencies regularly

---

## 🔍 **Testing Your Deployment**

### Test URLs
- **Safe**: `https://www.google.com`
- **Suspicious**: `http://malware.example.tk/login/secure/bank/verify`

### Health Check
Visit `/status` endpoint to verify model is loaded.

---

## 🆘 **Troubleshooting**

### Common Issues
1. **Build Fails**: Check Python version compatibility
2. **App Won't Start**: Verify start command
3. **Model Loading Error**: Check file paths
4. **Memory Issues**: Reduce worker count in gunicorn.conf.py
5. **Scikit-learn Build Error**: Use Python 3.11 and requirements-prod.txt

### Scikit-learn Build Error Fix
If you encounter this error:
```
Cython.Compiler.Errors.CompileError: sklearn/linear_model/_cd_fast.pyx
```

**Solution:**
1. Use Python 3.11 (not 3.13)
2. Use `requirements-prod.txt` instead of `requirements.txt`
3. Ensure all deployment files are updated

### Getting Help
- Check platform-specific logs
- Verify all files are committed to Git
- Test locally with `gunicorn app:app`

---

## 🎉 **Success!**

Once deployed, your app will be:
- ✅ Accessible worldwide
- ✅ HTTPS secured
- ✅ Mobile responsive
- ✅ Production ready

**Share your deployed app**: `https://your-app-name.onrender.com`

---

*Need help? Check the platform-specific documentation or create an issue in your repository.*
