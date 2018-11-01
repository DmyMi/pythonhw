1. Create structure for department:
    * There are 3 types of employee: developer, designer and manager
    * Each employee has: first name, second name, salary, experiance (years)
    * Eachdesigner, developer or manager can have higher managers
    * Each designer has effectivness coefficient(0-1)
    * Each manager has team of developers and designers.
    * Department should have list of managers(which have their own teams)
    * Department should be able to give salary (for each employee message: `"@firstName@ @secondName@: got salary: @salaryValue@"`)
    * Each employee gets the salary, defined in field Salary. If experiance of employee is > 2 years, he gets bonus + 200$, if experiance is > 5 years, he gets salary*1.2 + bonus 500
    * Each designer gets the salary = salary*effCoeff
    * Each manager gets salary +
        1. 200$ if his team has >5 members
        2. 300$ if his team has >10 members
        3. salary*1.1 if more than half of team members are developers.
    * Redefine string representation for employee as follows: `"@firstName@ @secondName@, manager:@manager secondName@, experiance:@experiance@"`
