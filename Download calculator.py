# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

def convert_seconds(number_of_seconds):
    h = int(number_of_seconds / 3600)
    m = int((number_of_seconds % 3600) / 60)
    s = (number_of_seconds % 3600) % 60
    a = ' hours'
    b = ' minutes'
    c = ' seconds'
    if h == 1:
        a= a[:-1]
    if m == 1:
        b= b[:-1]
    if s == 1:
        c= c[:-1]
    return str(h) + a + ', ' + str(m) + b + ', ' + str(s) + c

def download_time(filesize, ufile, speed, uspeed):
    units = ["k", "M", "G", "T", "Y", "Z"] #using the posn of a unit in the list as the power of 1024.0 so I avoid implementing multiple if-structures.
    fsize_kb = filesize * (1024.0 ** units.index(ufile[0]))
    if ufile[1] == 'B':
        fsize_kb = fsize_kb * 8
        
    bandin_kb = speed * (1024.0 ** units.index(uspeed[0]))
    if uspeed[1] == 'B':
        bandin_kb = bandin_kb * 8
    
    totalsec = fsize_kb / bandin_kb
    return convert_seconds(totalsec)


print (download_time(1024,'kB', 1, 'MB'))
#>>> 0 hours, 0 minutes, 1 second

print (download_time(1024,'kB', 1, 'Mb'))
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print (download_time(13,'GB', 5.6, 'MB'))
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print (download_time(13,'GB', 5.6, 'Mb'))
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print (download_time(10,'MB', 2, 'kB'))
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print (download_time(10,'MB', 2, 'kb'))
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable
