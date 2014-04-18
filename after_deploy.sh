sudo ln -s nginx.conf /etc/nginx/conf.d/stackoeverflow.conf 
python manage.py collectstatic
sudo service nginx restart
ln -s uwsgi.ini /etc/uwsgi/apps-enabled/stackoeverflow.ini
/etc/uwsgi/apps-available


