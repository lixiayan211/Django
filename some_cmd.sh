
sudo ln -s ~/home/leo/www/mysite/mysite_nginx.conf /etc/nginx/sites-enabled/



# create a directory for the vassals
sudo mkdir /etc/uwsgi
sudo mkdir /etc/uwsgi/vassals
# symlink from the default config directory to your config file
sudo ln -s /home/leo/www/mysite/mysite_uwsgi.ini /etc/uwsgi/vassals/




