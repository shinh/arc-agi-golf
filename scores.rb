# these scores are from https://docs.google.com/spreadsheets/d/e/2PACX-1vQ7RUqwrtwRD2EJbgMRrccAHkwUQZgFe2fsROCR1WV5LA1naxL0pU2grjQpcWC2HU3chdGwIOUpeuoK/pubhtml#gid=1427788625
# a bit awkard to copy from that sheet since read online mode
a=File.read("scores.txt").lines.to_a
best= 400.times.map{|i|(a[i*2].split("\t").map(&:to_i)[2..-1]-[0]*100).min}

ours=400.times.map{|i|
  File.size("submissions/task%03d.py"%(i+1))
}
z=1.upto(400).zip(best, ours)
z.sort_by{|n,b,o|1.0*o/b}.each{|a|p a}
puts "[task#, best from spreadsheet, ours]"
