import urllib2
import re           # for regex matching
#import Course

academicYear = 1314
region = 'ALL'

courseDept = []
a_courseNumber = []
a_courseTitle = []
a_courseInfo = []
a_term = ['10', '20', '30']
numOfTerms = len(a_term)


#Lists all Departments
def getDepartmentList(region, academicYear, a_term):
    for termCount in range (0,numOfTerms):
        urlAllDept = 'http://classes.deltacollege.edu/classSchedule/departments.cfm?region=' + region + '&term=' + a_term[termCount] + '&year=' + '20' + str(academicYear)

        usock = urllib2.urlopen(urlAllDept)
        data = usock.read()
        usock.close()
        data = [line.strip() for line in data.split('\n') if line.strip()]

        for line in data:
            regexDeptAll = re.compile('>(\w+\s*\w*)<')
            for match in regexDeptAll.finditer(line.rstrip()):

                #Issue with department uniqueness here#
                
                departmentCode = formatWhitespaceForURL(match.groups()[0])
                if departmentCode not in courseDept:
                    courseDept.append(departmentCode)

    return courseDept


# Convert whitespace characters into HTML url readable %20
def formatWhitespaceForURL(item):
    newWord = ""

    for char in item:
        if char == " ":
            char = "%20"
        newWord += char

    return newWord


#List all classes available for all Departments
def getAllClasses(a_term, courseDept, region, academicYear):
    for termCount in range (0,numOfTerms):
        j = 0
        for courseDeptCount in range (1,numOfDept):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + str(courseDept[courseDeptCount]) + "&region=" + region
            print str(termCount) + ":" + str(courseDeptCount) + ":" + urlDept
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                matchFound = 0

                # Grab the number of the course
                regexDept = re.compile('([A-Z| ]{1,12})(\d\d\d)[A-Z|<]')
                for match in regexDept.finditer(line.rstrip()):
                    if match:
                        a_courseNumber.append(match.group(0) + " " + match.group(1))
                        print "Num: " + a_courseNumber[courseDeptCount-1 + j]
                        j += 1
                        matchFound = 1
                
                if matchFound == 1:
                    j -= 1
                
                i = 0
                # Grab the title of the course
                regexName = re.compile('TD VALIGN="TOP">([\w\s]+)')
                for match in regexName.finditer(line.rstrip()):
                    if match:
                        a_courseTitle.append(match.groups())
                        print a_courseTitle[i]
                        i += 1

    return a_courseNumber
    return a_courseTitle



#List individual listings for all classes in all Departments
def getAllEntries(a_term, a_courseNumber, courseDept, region, academicYear):
    for termCount in range(0,numOfTerms):
        for courseDeptCount in range(0,numOfDept):
            for courseNumCount in range(0,numOfCourse):

                # Construct URL
                urlClass = 'http://classes.deltacollege.edu/classSchedule/sections.cfm?term=' + a_term[termCount] + '&academicYear=' + str(academicYear) + '&region=' + region + '&courseId=' + courseDept[courseDeptCount] + '%20%20%20%20' + a_courseNumber[courseNumCount]
                print '\n\n+-------------------------------------------+'
                print courseDept + ' ' + a_courseNumber[courseNumCount]
                if a_term[termCount] == '10':
                    alias = "Summer"
                elif a_term[termCount] == '20':
                    alias = "Fall"
                elif a_term[termCount] == '30':
                    alias = "Spring"
                print alias + ' ' + str(academicYear) + ' ' + region + '\n'

                # Open URL and read HTML
                usock = urllib2.urlopen(urlClass)
                data = usock.read()
                usock.close()

                # Split into multiple lines at newline limiters
                data = [line.strip() for line in data.split('\n') if line.strip()]

                # Iterate the lines and print matches
                for line in data:
                    regex = re.compile('([\d|\*]{5})\s+(\S+)\s+(\S+)\s+(\S+)\s+(\S+|Mtn.\sHouse)\s+(\S+\s+\S+)\s+(\S+,\s+\w)')#\s+<.*?>(\S+)<')
                    for match in regex.finditer(line.rstrip()):
                        if match:
                            print match.groups()

#getAllEntries(a_term, a_courseNumber, courseDept, region, academicYear)

getDepartmentList(region, academicYear, a_term)
numOfDept = len(courseDept)
getAllClasses(a_term, courseDept, region, academicYear)
numOfCourse = len(a_courseNumber)
numOfTitle = len(a_courseTitle)