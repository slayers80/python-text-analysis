# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:42:42 2018

@author: lwang
"""

def canFinish(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
        prereq = {}
        for pair in prerequisites:
            if pair[0] not in prereq:
                prereq[pair[0]] = [pair[1]]
            else:
                prereq[pair[0]].append(pair[1])    
        
        visited = set()
        visiting = {}    
        result = {'isFinishable': True}
        def oneCourse(CourseNum, prereq):        
            
            if CourseNum in prereq:
                for nextCourse in prereq[CourseNum]:
                    if nextCourse not in visited:
                        visited.add(nextCourse)                        
                        visiting[nextCourse] = True
                        oneCourse(nextCourse, prereq)                        
                        visiting.pop(nextCourse)
                    elif nextCourse in visiting:                    
                        result['isFinishable'] = False                      
        
        for i in range(numCourses):
            if i not in visited:
                visited.add(i)                                   
                visiting[i] = True
                oneCourse(i, prereq)                
                visiting.pop(i)
                    
        return result['isFinishable']