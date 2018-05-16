set terminal png nocrop enhanced font "helvetica,10" size 640,400
set output "temper.png"

set autoscale
set title "Temperature"
set xlabel "Time"
set ylabel "Temperature (Degrees Celsius)"

set style line 1 lc rgb '#A60628' pt 6 ps 1 lt 1 lw 1
set style line 2 lc rgb '#348ABD' pt 6 ps 1 lt 1 lw 1

set datafile missing "None"
set datafile separator ","
set xdata time
set timefmt "%Y-%m-%dT%H:%M:%S"

plot "temper.log" u 1:2 t "Internal" w lp ls 1, \
     "temper.log" u 1:3 t "External" w lp ls 2
