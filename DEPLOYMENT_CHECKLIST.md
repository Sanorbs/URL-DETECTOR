# 🚀 Quick Deployment Checklist

## ✅ **Pre-Deployment Checklist**

- [ ] All files committed to Git
- [ ] `requirements.txt` includes `gunicorn`
- [ ] `app.py` has production settings
- [ ] Test locally with `gunicorn app:app`

## 🎯 **Render Deployment (Recommended)**

### Step 1: GitHub Setup
```bash
git add .
git commit -m "Ready for deployment"
git push origin main
```

### Step 2: Render Setup
1. Go to [render.com](https://render.com)
2. Sign up with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository

### Step 3: Configuration
- **Name**: `malicious-url-detector`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app`
- **Plan**: Free

### Step 4: Deploy
Click "Create Web Service" and wait!

**Your URL**: `https://your-app-name.onrender.com`

## 🔧 **Alternative Platforms**

### Railway
- Build: `pip install -r requirements.txt`
- Start: `gunicorn app:app`

### PythonAnywhere
- Framework: Flask
- Python: 3.9
- WSGI: Point to app.py

## 🧪 **Post-Deployment Testing**

- [ ] App loads without errors
- [ ] URL detection works
- [ ] Model training works
- [ ] Mobile responsive
- [ ] HTTPS working

## 🆘 **Common Issues**

| Issue | Solution |
|-------|----------|
| Build fails | Check Python version (3.9+) |
| App won't start | Verify start command |
| Model error | Check file paths |
| Memory issues | Reduce gunicorn workers |

## 📱 **Mobile Testing**

- Test on phone browser
- Check PWA functionality
- Verify responsive design

---

**Need help?** Check `DEPLOYMENT.md` for detailed instructions!
