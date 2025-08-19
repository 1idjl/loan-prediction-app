import pkg_resources
import sys

# لیست کتابخانه‌های مورد نظر
libraries = ['streamlit', 'pandas', 'pycaret']

# بررسی نسخه هر کتابخانه
for lib in libraries:
    try:
        version = pkg_resources.get_distribution(lib).version
        print(f"{lib}: {version}")
    except pkg_resources.DistributionNotFound:
        print(f"{lib}: Not installed")