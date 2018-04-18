'''
Name: Tom Nguyen
Professor: Dr. Marie A. Roch
Class: CS 550
Date: April 12,2018

Assignment  4- backtrack.py

05 constraint satisfaction - slide 22
'''

from csp_lib.backtrack_util import (first_unassigned_variable, 
                                    unordered_domain_values,
                                    no_inference)

def backtracking_search(csp,
                        select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values,
                        inference=no_inference):
    """backtracking_search
    Given a constraint satisfaction problem (CSP),
    a function handle for selecting variables, 
    a function handle for selecting elements of a domain,
    and a set of inferences, solve the CSP using backtrack search
    """
    
    # See Figure 6.5] of your book for details

    def backtrack(assignment):#def backtrack(assignment, CSP):
        """Attempt to backtrack search with current assignment
        Returns None if there is no solution.  Otherwise, the
        csp should be in a goal state.
        
        05 constraint satisfaction - slide 22
        """
        assignment_counter = 0
        csp_counter = 0
        for a in assignment:
            assignment_counter = assignment_counter + 1
        for b in csp.variables:
            csp_counter = csp_counter+1
        if assignment_counter == csp_counter:#if all variables assigned, return assignment
            return assignment
        variable = first_unassigned_variable(assignment,csp)#var = select_unassigned_variable(CSP, assignment)
        for x in unordered_domain_values(variable,assignment,csp):#for each value in order_domain_values(var, assignment, csp):
            nconflicts=csp.nconflicts(variable,x,assignment)
            if nconflicts==0:#if value consistent with assignment:
                csp.assign(variable,x,assignment)#assignment.add({var = value})
                remove = csp.suppose(variable,x)#Start accumulating inferences from assuming var=value.
                result = backtrack(assignment)#result = backtrack(assignment, CSP)
                if result is None:
                    csp.restore(remove)# restore assignment to its state at top of loop and try next value
                else:
                    return result#if result != failure, return result
        csp.unassign(variable,assignment)#assignment.remove({var = value}, inferences)
        return None

    # Call with empty assignments, variables accessed
    # through dynamic scoping (variables in outer
    # scope can be accessed in Python)
    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result
