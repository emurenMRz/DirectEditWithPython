#!/bin/sh

# Specify your mydns account information.
id=<Your MyDNS.JP ID>
pwd=<Your MyDNS.JP Password>
domain=<Your Domain>
email=<Your E-mail>

# Specify the absolute path to "dns01.py".
#  - If you use a relative path, the script will not be able to find it when you run renew.
hook_script=<Absolute path to "dns01.py">

# If you want to change the path of the executable...
certbot_path=certbot
python_path=python

# Run certbot for the first time (you can "certbot renew" the next time)
cd `dirname $0`
${certbot_path} certonly --manual --preferred-challenges=dns \
--manual-auth-hook "${python_path} ${hook_script} REGIST ${id} ${pwd}" \
--manual-cleanup-hook "${python_path} ${hook_script} DELETE ${id} ${pwd}" \
-d ${domain} -d *.${domain} \
--server https://acme-v02.api.letsencrypt.org/directory \
--agree-tos -m ${email} --key-type rsa
#--manual-public-ip-logging-ok
