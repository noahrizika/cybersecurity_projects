# check arguments
if [ "$#" -ne 1 ]; then
	echo "Usage: $O <destination_ip>"
	exit 1
fi

# use ping to routetrace, store in temp file
touch .routetrace_temp.out
echo "starting routetracing..."

for i in {1..25}; do
	ping $@ -c 1 -t $i | grep -oP "^From ([\d\.]*)" | grep -oP "([\d\.]*)" >> .routetrace_temp.out
done

cat .routetrace_temp.out
echo "end of routetracing"

rm .routetrace_temp.out
