sudo rm -f /etc/nginx/sites-enabled/web_nginx.conf
sudo ln -s /home/box/web/etc/web_nginx.conf  /etc/nginx/sites-enabled/web_nginx.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
#sudo /etc/init.d/mysql start