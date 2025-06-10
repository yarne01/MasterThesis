clear;

echo "Started at $(date +"%d-%m-%y+%T")"
echo ""


mkdir output -p
#rm output/*

cd ../build || exit
make -j 12 || exit
cd ../YARNE || exit

echo ""

# he_only

for VAR in pasta2_3
do
  echo "$VAR Begonnen"
  for app in "_seal"
  #for app in "" "_seal" "_helib"
  do
    file_naam="$VAR$app"_test
    echo "$file_naam Begonnen!" > output/$file_naam.txt;

    rm output/OUTPUT.txt

    ./../build/tests/$file_naam >> output/$file_naam.txt;

    cp output/OUTPUT.txt output/$file_naam.output.txt
  done
  echo "$VAR Eindigt";
done



python3 processingResults.py