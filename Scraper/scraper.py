import urllib2
import re           # for regex matching
#import Course

academicYear = 1314
region = 'ALL'
courseDept = []
a_courseNumber = []
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
            regexDeptAll = re.compile('>([A-Z].......)<')
            for match in regexDeptAll.finditer(line.rstrip()):
                if match:
                    courseDept.extend(match.groups())
        return courseDept

getDepartmentList(region, academicYear, a_term)

numOfDepts = len(courseDept)


#List all classes available for all Departments
def getAllClasses(a_term, courseDept, region, academicYear):
    for termCount in range (0,numOfTerms):
        for courseDeptCount in range(0,numOfDepts):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDept[courseDeptCount] + "&region=" + region
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                regexDept = re.compile(courseDept + '....(\d\d\d).')
                for match in regexDept.finditer(line.rstrip('<')):
                    if match:
                        a_courseNumber.extend(match.groups())
            return a_courseNumber

#getAllClasses(a_term, courseDept, region, academicYear)

numOfCourses = len(a_courseNumber)

print numOfCourses

#List individual listings for all classes in all Departments
def getAllEntries(a_term, a_courseNumber, courseDept, region, academicYear):
    for termCount in range(0,numOfTerms):
        for courseDeptCount in range(0,numOfDepts):
            for courseNumCount in range(0,numOfCourses):

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
