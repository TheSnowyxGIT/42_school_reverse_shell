state=$(ps -eaf | grep "mem.sh" | grep -v grep | wc -l | tr -d " " | tr -d "\n")
if [ $state -ne  "2" ]
then
	exit 1
fi
while true
do
	touch /sgoinfre/goinfre/Perso/correc/l/$USER
	sleep 60
done
