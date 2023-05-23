wget -O wget_output.txt https://www.example.com

if [[ ! -z "$(diff wget_output.txt example.txt)" ]]; then
	echo "Failed: wget -O wget_output.txt https://www.example.com"
	exit 1
fi

rm -rf another_dir && mkdir another_dir
wget -P another_dir https://www.example.com

if [[ ! -z "$(diff another_dir/index.html example.txt)" ]]; then
	echo "Failed: wget -P another_dir https://www.example.com"
	exit 1
fi
