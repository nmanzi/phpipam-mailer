#!/bin/bash
now=$(date +%m%d%H%M%S)
fancydate=$(date)
curl http://localhost/phpipam/site/admin/exportGenerateXLS.php > /tmp/IPAM$now.xls
/usr/local/bin/mailer.py "<YOUREMAILHERE>" "PHP IPAM Export" "Generated $fancydate" "/tmp/IPAM$now.xls" "IPAM-$now.xls"
rm /tmp/IPAM$now.xls
