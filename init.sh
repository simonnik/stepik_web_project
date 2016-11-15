sudo rm -f /etc/nginx/sites-enabled/web_nginx.conf
sudo ln -s /home/box/web/etc/web_nginx.conf  /etc/nginx/sites-enabled/web_nginx.conf
sudo /etc/init.d/nginx restart
sudo rm -f /etc/gunicorn.d/hello.py
sudo ln -s /home/box/web/etc/hello.py   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start