state=$(ps -eaf | grep ".mac.sh" | grep -v grep | wc -l | tr -d " " | tr -d "\n")
if [ $state -ne  "2" ]
then
	exit 1
fi
while true
do
	if [ $(cat /sgoinfre/goinfre/Perso/correc/upd.txt | tr -d " " | tr -d "\n") = "1" ]
	then
		pkill python &>/dev/null
		sleep 1.5
		python /sgoinfre/goinfre/Perso/correc/APImem.py &
	fi
	sleep 4
done
