:<<doc
启动collectl监视器
创建monitor*文件
与monitor_start.sh文件不同之处在于，这里是以3S为时间间隔
doc

if [ -n "${1}" ]; then
	user="$1"
else
	user="gpadmin"
fi

echo -e "\033[33;49;1m [JPDB2 start] \033[39;49;0m"

ssh ${user}@JPDB2 << eof
echo "******************************************************************************************************************************" >> /tmp/monitor.txt
collectl -scmdn -oT -i3 >> /tmp/monitor.txt &
eof

for k in $(seq 1 6)
do
echo -e "\033[33;49;1m [node${k} start] \033[39;49;0m"
ssh ${user}@node${k} << eof
echo "******************************************************************************************************************************" >> /tmp/monitor${k}.txt
collectl -scmdn -oT -i3 >> /tmp/monitor${k}.txt &
eof
done

echo -e "\033[32;49;1m [monitor started] \033[39;49;0m"
