#Acknowledgements
#Mat Larribas
#Regexpal.com

import urllib2      # for scraper
import re            # for regex matching
#import Course

academicYear = 1314
region = 'ALL'

#Initialize Arrays
courseDepts = []
courseDeptsList = []
a_courseNumber = []
a_courseTitle = []
a_courseInfo = []
a_term = ['10', '20', '30']

#Grabs all Departments and stores them in courseDeptsList

def getDepartmentList(region, academicYear, a_term):
    #Scrapes  HTML and stores all Departments in the arrray courseDepts
    for termCount in range (0,len(a_term)):
        urlAllDept = 'https://classes.deltacollege.edu/schedule/departments.cfm?region=' + region + '&term=' + a_term[termCount] + '&year=' + '20' + str(academicYear)

        #HTML scraper
        usock = urllib2.urlopen(urlAllDept)
        data = usock.read()
        usock.close()
        data = [line.strip() for line in data.split('\n') if line.strip()]


        #Loop that adds Department to array
        for line in data:
            regexDeptAll = re.compile("dept=(\D*)\">")
            for match in regexDeptAll.finditer(line.rstrip()):
                if match.groups() not in courseDepts:
                    courseDepts.append(match.groups())

    #Extracting strings from tuples
    for item in courseDepts:
        for x in item:
            courseDeptsList.append(x)

    return courseDeptsList


#Get all classes available for all Departments
def getAllClasses(a_term, region, academicYear, courseDeptsList):
    for termCount in range (0,len(a_term)):
        for element in range (0,len(courseDeptsList)):
            urlDept = "https://classes.deltacollege.edu/schedule/courses.cfm?term=" + a_term[termCount] + '&year=20' + str(academicYear) + "&region=" + region + '&dept=' + urllib2.quote(courseDeptsList[element])
            print urlDept
            print "Attempting Term"+ a_term[termCount] + " for department " + courseDeptsList[element]

            #HTML Scraper again
            try:
                usock = urllib2.urlopen(urlDept)
                data = usock.read()
                usock.close()
                data = [line.strip() for line in data.split('\n') if line.strip()]

                #Course ID
                for line in data:
                    regexDept = re.compile('course=([A-Z| ]{1,12}\d\d\d[A-Z]|[A-Z| ]{1,12}\d\d\d)')
                    for match in regexDept.finditer(line.rstrip()):
                        if match not in a_courseNumber:
                            a_courseNumber.append(match.groups())
                            #print "Found" + courseDeptsList[line] + " : " + a_courseNumber[line]


                #Course Name List
                regexName=re.compile(';">(\D*)</td>')
                for match in regexName.finditer(line.rstrip()):
                    if match not in a_courseTitle:
                        a_courseTitle.append(match.groups())

            except IOError:
                print "HTML Error"

    return a_courseNumber
    return a_courseTitle


#Get individual listings for all classes in all Departments

def getAllEntries(a_term, a_courseNumber, courseDepts, region, academicYear):
    for termCount in range(0,len(a_term)):
        for courseDeptsCount in range(0,len(courseDepts)):
            for courseNumCount in range(0,numOfCourse):

                # Construct URL
                urlClass = 'https://classes.deltacollege.edu/schedule/sections.cfm?term=' + a_term[termCount] + '&academicYear=' + str(academicYear) + '&region=' + region + '&courseId=' + courseDepts[courseDeptsCount] + '%20%20%20%20' + a_courseNumber[courseNumCount]
                print '\n\n+-------------------------------------------+'
                print courseDepts + ' ' + a_courseNumber[courseNumCount]
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

getDepartmentList(region, academicYear, a_term)
print "\n\n"
print "getDepartmentList Ended \n\n"
getAllClasses(a_term, region, academicYear, courseDeptsList)
numOfCourse = len(a_courseNumber)
numOfTitle = len(a_courseTitle)
print "There are "+numOfCourse + " courses"
print "There are "+numOfTitle+" course titles"
print a_courseNumber[0]
print a_courseTitle[0]
#getAllEntries(a_term, a_courseNumber, courseDepts, region, academicYear)


