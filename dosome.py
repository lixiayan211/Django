from datetime import datetime as dt
from blog.models import BlogPost


for i in range(10):
    bp = BlogPost(title='post #%d' % i, body='body of post #%d' % i, timestamp=dt.now())
    bp.save()
