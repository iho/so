sudo ln -s /etc/nginx/conf.d/stackoeverflow.conf nginx.conf
python manage.py collectstatic
sudo service nginx restart

