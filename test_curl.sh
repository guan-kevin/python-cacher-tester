curl -o curl_output.txt https://www.example.com

if [[ ! -z "$(diff curl_output.txt example.txt)" ]]; then
	echo "Failed: curl -o curl_output.txt https://www.example.com"
	exit 1
fi

rm -rf another_dir && mkdir another_dir
curl https://www.example.com > another_dir/index.html

if [[ ! -z "$(diff another_dir/index.html example.txt)" ]]; then
	echo "Failed: curl https://www.example.com > another_dir/index.html"
	exit 1
fi
