import os
import sys
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

path = '/home/kajiyai/kajiyai.pythonanywhere.com/GoalBuddies'  # 例: '/home/kajiyai/GoalBuddies'
if path not in sys.path:
    sys.path.append(path)

sys.path.append('/home/kajiyai/kajiyai.pythonanywhere.com/myenv/lib/python3.9/site-packages')
