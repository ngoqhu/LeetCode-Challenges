# Read from the file file.txt and output the tenth line to stdout.
line=0
while read l; do
    line=$(($line + 1))
    if [[ $line -eq 10 ]]; then
        echo $l;
        exit;
    fi;
done < file.txt
echo "";
