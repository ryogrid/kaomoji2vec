require 'oj'

#(0..1787).each{ |num|  
(176..2956).each{ |num|
  if num % 2 == 0
    next
  end
  fidx = sprintf("%04d", num)
  `unzip #{fidx}.zip`
  Dir.foreach(fidx) { |fname|
    if fname == "." || fname == ".."
      next
    end
    open(fidx + "/" + fname) { |f|
      f.each_line{ |line|
        obj = Oj.load(line)
        puts obj["content"]
      }
    }
  }
  `rm -r #{fidx}`
}
