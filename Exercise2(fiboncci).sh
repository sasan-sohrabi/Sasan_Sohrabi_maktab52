
# Program for Fibonacci Series
   
# Input fo N
echo "Input of N for Fibonacci Series"
read N
  
# First Number of the Fibonacci Series
a=0
  
# Second Number of the Fibonacci Series
b=1 

rm -f Fibonacci.txt

echo "The Fibonacci series for $N is: " >> "Fibonacci.txt"
for (( i=0; i<$N; i++ ))
do
    echo "$a " >> "Fibonacci.txt"
    fn=$((a + b))
    a=$b
    b=$fn
done
