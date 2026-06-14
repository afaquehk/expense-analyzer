# PythonAnywhere Deployment Guide - Step by Step

Complete guide to deploy SplitLedger to PythonAnywhere for FREE!

---

## 📋 **Before You Start:**

You need:
- ✅ GitHub account (already have: afaquehk/expense-analyzer)
- ✅ Email address for PythonAnywhere account
- ⏱️ 20-30 minutes

---

## 🚀 **Step 1: Create PythonAnywhere Account**

### 1.1 Sign Up
1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Choose username (e.g., `afaquehk`)
3. Enter your email
4. Create password
5. Click "Register"
6. Verify your email

**Your site will be:** `https://afaquehk.pythonanywhere.com`

---

## 💻 **Step 2: Clone Your Repository**

### 2.1 Open Bash Console
1. Login to PythonAnywhere
2. Click **"Consoles"** in top menu
3. Click **"Bash"** (under "Start a new console")

### 2.2 Clone Your Repo
Copy and paste these commands one by one:

```bash
# Clone your repository
git clone https://github.com/afaquehk/expense-analyzer.git

# Go into the directory
cd expense-analyzer

# Check files are there
ls -la
```

You should see all your files!

---

## 🐍 **Step 3: Set Up Virtual Environment**

Still in the Bash console:

```bash
# Create virtual environment with Python 3.10
mkvirtualenv --python=/usr/bin/python3.10 splitledger

# You should see (splitledger) in your prompt now

# Install all dependencies
pip install -r requirements.txt

# Wait for installation to complete (2-3 minutes)
```

**Important:** If you see any errors about `mysqlclient`, that's normal on PythonAnywhere. We'll handle it next.

---

## 🗄️ **Step 4: Set Up MySQL Database**

### 4.1 Initialize MySQL
1. Click **"Databases"** tab in top menu
2. Click **"Initialize MySQL"**
3. Set a MySQL password (save this!)
4. Click **"Initialize MySQL"**

### 4.2 Create Database
Scroll down to "Create Database":
1. Database name: `afaquehk$splitledger` (replace afaquehk with your username)
2. Click **"Create"**

### 4.3 Note Your Database Details
You'll need these:
- **Host:** `afaquehk.mysql.pythonanywhere-services.com`
- **Database name:** `afaquehk$splitledger`
- **Username:** `afaquehk` (your PythonAnywhere username)
- **Password:** (what you just set)

---

## ⚙️ **Step 5: Configure Django Settings**

### 5.1 Update Settings for Production

Back in Bash console:

```bash
# Go to project directory
cd ~/expense-analyzer

# Create production settings file
nano splitledger/production_settings.py
```

Paste this content (replace USERNAME with yours):

```python
from .settings import *

# SECURITY WARNING: keep the secret key used in production secret!
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'change-this-to-a-real-secret-key')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['USERNAME.pythonanywhere.com']

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'USERNAME$splitledger',
        'USER': 'USERNAME',
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': 'USERNAME.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files
STATIC_ROOT = '/home/USERNAME/expense-analyzer/staticfiles'
MEDIA_ROOT = '/home/USERNAME/expense-analyzer/media'
```

**Press:**
- `Ctrl+O` to save
- `Enter` to confirm
- `Ctrl+X` to exit

### 5.2 Collect Static Files

```bash
# Set Django settings module
export DJANGO_SETTINGS_MODULE=splitledger.production_settings

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create superuser
python manage.py createsuperuser
```

Follow prompts to create admin account.

---

## 🌐 **Step 6: Configure Web App**

### 6.1 Create Web App
1. Click **"Web"** tab in top menu
2. Click **"Add a new web app"**
3. Click **"Next"** (for your free domain)
4. Select **"Manual configuration"** (NOT Django wizard!)
5. Select **"Python 3.10"**
6. Click **"Next"**

### 6.2 Configure Virtual Environment
Scroll to **"Virtualenv"** section:
1. Enter: `/home/USERNAME/.virtualenvs/splitledger`
   (Replace USERNAME with yours)
2. Click the checkmark ✓

### 6.3 Configure WSGI File
1. In **"Code"** section, click **WSGI configuration file** link
2. **Delete everything** in the file
3. Paste this (replace USERNAME):

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/USERNAME/expense-analyzer'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variables
os.environ['DJANGO_SETTINGS_MODULE'] = 'splitledger.production_settings'
os.environ['DB_PASSWORD'] = 'YOUR_MYSQL_PASSWORD'  # Replace with your MySQL password
os.environ['SECRET_KEY'] = 'your-secret-key-here'  # Generate a new one!

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Important:** 
- Replace `USERNAME` with your PythonAnywhere username
- Replace `YOUR_MYSQL_PASSWORD` with your MySQL password
- Replace `your-secret-key-here` with a random string

**Save the file** (click "Save" button at top)

### 6.4 Configure Static Files
Scroll to **"Static files"** section:

Click **"Enter URL"** and add:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/USERNAME/expense-analyzer/staticfiles` |
| `/media/` | `/home/USERNAME/expense-analyzer/media` |

(Replace USERNAME with yours)

---

## 🎉 **Step 7: Launch Your Site!**

### 7.1 Reload Web App
1. Scroll to top of Web tab
2. Click big green **"Reload"** button
3. Wait 10 seconds

### 7.2 Visit Your Site!
Go to: **https://USERNAME.pythonanywhere.com**

(Replace USERNAME with your PythonAnywhere username)

**You should see your site live!** 🎊

---

## ✅ **Step 8: Test Everything**

1. **Homepage** — Should redirect to login
2. **Register** — Create a test account
3. **Create Group** — Add a test group
4. **Add Expense** — Test expense creation
5. **View Balances** — Check calculations
6. **Admin Panel** — Visit `/admin/` with superuser

---

## 🔧 **Step 9: Troubleshooting**

### If you see "Something went wrong"

**Check Error Log:**
1. Web tab → Log files
2. Click **"error.log"**
3. Scroll to bottom
4. Fix any errors shown

**Common Issues:**

#### 1. Database Connection Error
- Check MySQL password in WSGI file
- Verify database name matches: `USERNAME$splitledger`

#### 2. Static Files Not Loading
- Run: `python manage.py collectstatic` in Bash
- Check static files paths in Web tab

#### 3. Import Errors
- Make sure virtualenv is activated: `workon splitledger`
- Reinstall requirements: `pip install -r requirements.txt`

#### 4. ModuleNotFoundError
- Check sys.path in WSGI file includes project directory
- Verify virtualenv path is correct

---

## 🔄 **Step 10: Update Your Site (Future Changes)**

When you make changes to your code:

```bash
# In Bash console
cd ~/expense-analyzer

# Pull latest changes from GitHub
git pull origin main

# If models changed, run migrations
workon splitledger
python manage.py migrate

# If static files changed
python manage.py collectstatic --noinput

# Go to Web tab and click "Reload"
```

---

## 🎨 **Step 11: Custom Domain (Optional)**

Want to use your own domain instead of `username.pythonanywhere.com`?

1. **Upgrade to paid plan** ($5/month)
2. Web tab → Add custom domain
3. Update DNS settings at your domain registrar
4. Add domain to `ALLOWED_HOSTS` in settings

---

## 📊 **Quick Reference Commands**

```bash
# Activate virtual environment
workon splitledger

# Go to project
cd ~/expense-analyzer

# Pull updates
git pull origin main

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Open Django shell
python manage.py shell

# Check logs
tail -f /var/log/USERNAME.pythonanywhere.com.error.log
```

---

## 🆘 **Getting Help**

If stuck:

1. **Check error logs** (Web tab → error.log)
2. **PythonAnywhere forums:** https://www.pythonanywhere.com/forums/
3. **PythonAnywhere help:** https://help.pythonanywhere.com/
4. **Django docs:** https://docs.djangoproject.com/

---

## ✨ **Success Checklist**

- [ ] Created PythonAnywhere account
- [ ] Cloned repository
- [ ] Set up virtual environment
- [ ] Created MySQL database
- [ ] Configured Django settings
- [ ] Ran migrations
- [ ] Collected static files
- [ ] Configured web app
- [ ] Set up WSGI file
- [ ] Configured static files
- [ ] Reloaded web app
- [ ] Site is live!
- [ ] Tested all features
- [ ] Created admin account

---

## 🎉 **Congratulations!**

Your SplitLedger app is now **LIVE ON THE INTERNET!**

Share your site: **https://USERNAME.pythonanywhere.com**

---

**Deployment Date:** _______________  
**Site URL:** https://_____________.pythonanywhere.com  
**Status:** 🟢 Live

---

## 📱 **What's Next?**

- Share the link with friends and family
- Add real expenses and test features
- Try CSV import with sample files
- Customize the theme if you want
- Consider upgrading for custom domain

**Your app is production-ready!** 🚀
