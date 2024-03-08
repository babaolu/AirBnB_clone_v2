#!/usr/bin/env bash
# Sets up web server

mkdir -p "/data/web_static/releases/test"
mkdir -p "/data/web_static/shared"
echo "Testing fake file" > "/data/web_static/releases/test/index.html"

serv_name=$(hostname)
sym_path=/data/web_static/current
if [ -e "$sym_path" ]
then
	rm -rf "$sym_path"
fi
ln -s /data/web_static/releases/test/ "$sym_path"

sudo chown -R ubuntu:ubuntu /data/

red_val="location /redirect_me {\n\
                return 301 https://www.youtube.com/watch?v=QH2-TGU1wu4;\n\
        }"

add_static="location /hbnb_static {\n\
	    	alias /data/web_static/current;\n\
	}"

add_val="error_page 404 /404-def.html;\n\
        location = /404-def.html {\n\
                root /var/www/html;\n\
                internal;\n\
        }"

echo -e "server {\n\
        listen 80 default_server;\n\
        listen [::]:80 default_server;\n\
        root /var/www/html;\n\
        index index.html index.htm index.nginx-debian.html;\n\
        server_name _;\n\
        location / {\n\
                try_files \$uri \$uri/ =404;\n\
        }\n\
        $red_val \n
	$add_static \n
        $add_val \n

        add_header X-Served-By $serv_name;
}" > /etc/nginx/sites-available/default
run_at_port=$(lsof -i :80 | \
sed -n '2{s/^[[:space:]]*\([^[:space:]]*\).*/\1/p}')
if [ -n "$run_at_port" ]
then
        sudo pkill "$run_at_port"
fi
sudo service nginx restart
