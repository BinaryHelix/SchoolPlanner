import urllib2
import re           # for regex matching
#import Course

term = 20
academicYear = 1314
region = 'ALL'
courseDept = 'MATH'
a_courseNumber = ['001','002','003']
a_term = ['10', '20', '30']

#List classes available
"""for termCount in range (0,3):
    urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDept + "&region=" + region
    print '\n\n+-------------------------------------------+\n'
    if a_term[termCount] == '10':
        alias = "Summer"
    elif a_term[termCount] == '20':
        alias = "Fall"
    elif a_term[termCount] == '30':
        alias = "Spring"
    print alias + ' ' + str(academicYear) + ' ' + region + '\n'
    print urlDept #DEBUG
    print '\n\n'

    usock = urllib2.urlopen(urlDept)
    data = usock.read()
    usock.close()
    data = [line.strip() for line in data.split('\n') if line.strip()]

    for line in data:
            regexDept = re.compile('MATH....\d\d\d.')
            regexDept.translate(None, '<')
            for match in regexDept.finditer(line.rstrip()):
                if match:
                    print match.groups()"""

#List individual listings for all classes in a department
def getClassList(a_term, a_courseNumber, courseDept, region, academicYear):
    for termCount in range(0,3):
        for courseNumCount in range(0,3):
            # Construct URL
            urlClass = 'http://classes.deltacollege.edu/classSchedule/sections.cfm?term=' + a_term[termCount] + '&academicYear=' + str(academicYear) + '&region=' + region + '&courseId=' + courseDept + '%20%20%20%20' + a_courseNumber[courseNumCount]
            print '\n\n+-------------------------------------------+\n'
            print courseDept + ' ' + a_courseNumber[courseNumCount] + '\n'
            if a_term[termCount] == '10':
                alias = "Summer"
            elif a_term[termCount] == '20':
                alias = "Fall"
            elif a_term[termCount] == '30':
                alias = "Spring"
            print alias + ' ' + str(academicYear) + ' ' + region + '\n'
            print urlClass #DEBUG
            print '\n\n'

            # Open URL and read HTML
            usock = urllib2.urlopen(urlClass)
            data = usock.read()
            usock.close()

            # Split into multiple lines at newline limiters
            data = [line.strip() for line in data.split('\n') if line.strip()]

            # Iterate the lines and print matches
            for line in data:
                regex = re.compile('([\d|\*]{5})\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+\s+\S+)\s+(\S+,\s+\w)')#\s+<.*?>(\S+)<')
                for match in regex.finditer(line.rstrip()):
                    if match:
                        print match.groups()





getClassList(a_term, a_courseNumber, courseDept, region, academicYear)