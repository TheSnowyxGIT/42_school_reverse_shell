while true
do 
	if [ $(cat /sgoinfre/goinfre/Perso/correc/test/upd.txt | tr -d " " | tr -d "\n") = "1" ]
	then
		pkill python >/dev/null 2>/dev/null &
		sleep 1.5
		python /sgoinfre/goinfre/Perso/correc/APImem.py &
	fi
    sleep 4
done
