zbx_host=""
width=829

result=$(wget --save-cookies=cookies.txt --keep-session-cookies --post-data "name=admin&password=aBHYGEW9bUBvUgIxnIn4&enter=Enter" -O - -q http://127.0.0.1:8008/zabbix/index.php?login=1 | grep window.location)

if [ "$result" ]
then
      echo "Authenticated successfully, getting graph"
        wget --load-cookies=cookies.txt -O chart.jpg -q "$zbx_host/chart2.php?graphid=$3&width=$width"
    fi
