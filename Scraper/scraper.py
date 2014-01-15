import urllib2
import re           # for regex matching
#import Course

academicYear = 1314
region = 'ALL'

courseDept = []
"""courseDeptSummer = []
courseDeptFall = []
courseDeptSpring = []"""

a_courseNumber = []
"""a_courseNumberSummer = []
a_courseNumberFall = []
a_courseNumberSpring = []"""

a_courseTitle = []
"""a_courseTitleSummer = []
a_courseTitleFall = []
a_courseTitleSpring = []"""

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
            regexDeptAll = re.compile('>([A-Z].......)<')
            for match in regexDeptAll.finditer(line.rstrip()):
                #Issue with department uniqueness here#
                if match.groups() not in courseDept:
                    print match.groups()
                    courseDept.extend(match.groups())

                    #TERM DEBUG
                    """if a_term[termCount] == '10':
                        courseDeptSummer.extend(match.groups())
                    elif a_term[termCount] == '20':
                        courseDeptFall.extend(match.groups())
                    elif a_term[termCount] == '30':
                        courseDeptSpring.extend(match.groups())"""

    return courseDept
    """return courseDeptSummer
    return courseDeptFall
    return courseDeptSpring"""

getDepartmentList(region, academicYear, a_term)

numOfDept = len(courseDept)
"""numOfDeptSummer = len(courseDeptSummer)
numOfDeptSpring = len(courseDeptSpring)
numOfDeptFall = len(courseDeptFall)"""

"""print numOfDeptSummer
print numOfDeptSpring
print numOfDeptFall"""
print numOfDept



#List all classes available for all Departments
def getAllClasses(a_term, courseDept, courseDeptFall, courseDeptSpring, region, academicYear):
    for termCount in range (0,numOfTerms):
        for courseDeptCount in range (0,numOfDept):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDept[courseDeptCount] + "&region=" + region
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                regexDept = re.compile('[A-Z| ]{1,12}\d\d\d[A-Z|<]')
                for match in regexDept.finditer(line.rstrip()):
                    if match:
                        a_courseNumber.extend(match.groups())
                regexName = re.compile('TD VALIGN="TOP">.({1,100})')
                for match in regexName.finditer(line.rstrip()):
                    if match:
                        a_courseTitle.extend(match.groups())

    return a_courseNumber
    return a_courseTitle

    """for termCount in range (0,numOfTerms):
        for courseDeptCount in range (0,numOfDeptSummer):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDeptSummer[courseDeptCount] + "&region=" + region
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                regexDept = re.compile('[A-Z| ]{1,12}\d\d\d[A-Z|<]')
                for match in regexDept.finditer(line.rstrip()):
                    if match:
                        a_courseNumberSummer.extend(match.groups())
                regexName = re.compile('TD VALIGN="TOP">.({1,100})')
                for match in regexName.finditer(line.rstrip()):
                    if match:
                        a_courseTitleSummer.extend(match.groups())

    return a_courseNumberSummer
    return a_courseTitleSummer


    for termCount in range (0,numOfTerms):
        for courseDeptCount in range (0,numOfDeptFall):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDeptFall[courseDeptCount] + "&region=" + region
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                regexDept = re.compile('[A-Z| ]{1,12}\d\d\d[A-Z|<]')
                for match in regexDept.finditer(line.rstrip()):
                    if match:
                        a_courseNumberFall.extend(match.groups())
                regexName = re.compile('TD VALIGN="TOP">.({1,100})')
                for match in regexName.finditer(line.rstrip()):
                    if match:
                        a_courseTitleFall.extend(match.groups())


    return a_courseNumberFall
    return a_courseTitleFall



    for termCount in range (0,numOfTerms):
        for courseDeptCountSpring in range (0,numOfDeptSpring):
            urlDept = 'http://classes.deltacollege.edu/classSchedule/courses.cfm?term=' + a_term[termCount] + '&year=' + '20' + str(academicYear) + '&dept=' + courseDeptSpring[courseDeptCountSpring] + "&region=" + region
            usock = urllib2.urlopen(urlDept)
            data = usock.read()
            usock.close()
            data = [line.strip() for line in data.split('\n') if line.strip()]

            for line in data:
                regexDept = re.compile('[A-Z| ]{1,12}\d\d\d[A-Z|<]')
                for match in regexDept.finditer(line.rstrip()):
                    if match:
                        a_courseNumberSpring.extend(match.groups())
                regexName = re.compile('TD VALIGN="TOP">.({1,100})')
                for match in regexName.finditer(line.rstrip()):
                    if match:
                        a_courseTitleSpring.extend(match.groups())




    return a_courseNumberSpring
    return a_courseTitleSpring"""




#getAllClasses(a_term, courseDeptSummer, courseDeptFall, courseDeptSpring, region, academicYear)

"""numOfCourseSummer = len(a_courseNumberSummer)
numOfCourseFall = len(a_courseNumberFall)
numOfCourseSpring = len(a_courseNumberSpring)"""

numOfCourse = len(a_courseNumber)

"""numOfTitleSummer = len(a_courseTitleSummer)
numOfTitleFall = len(a_courseTitleFall)
numOfTitleSpring = len(a_courseTitleSpring)"""

numOfTitle = len(a_courseTitle)

"""print numOfCourseSummer
print numOfCourseFall
print numOfCourseSpring

print numOfTitleSummer
print numOfTitleFall
print numOfTitleSpring"""

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
