import numpy as np
import matplotlib.pyplot as plt
emp_id=np.array([101,102,103,104,105,106,107,108,109,110,111,112,113,114,115])
department=np.array(["IT","HR","IT","SALES","FINANCE","IT","SALES","HR","FINANCE","IT","SALES","FINANCE","HR","IT","SALES"])
working_days=np.array([22,21,23,20,22,21,23,22,20,24,21,22,23,20,24])
present_days=np.array([21,19,22,18,21,20,22,20,18,23,19,21,22,19,23])
projects_completed=np.array([5,3,7,4,6,5,8,3,4,7,5,6,4,8,7])
working_hours=np.array([176,160,190,150,172,165,195,155,162,188,158,170,160,192,185])
performance_score=np.array([82,68,91,72,85,78,94,65,70,89,76,83,71,96,88])
attendance_emp=(present_days/working_days)*100
print("Attendance Percentage For Every Employee:",(attendance_emp))
print(np.round(attendance_emp))
emp_attendance_90=(emp_id[attendance_emp<90])
print("Employees Attendance Is Below 90%:",(emp_attendance_90))
emp_attendance_95=(emp_id[attendance_emp>95])
print("Employees Attendance Is Above 95%:",(emp_attendance_95))
avg=(attendance_emp.mean())
print("Average Attendance Percentage:",(avg))
print("Employees Attendance Is Below Company Average:",(emp_id[attendance_emp<avg]))
projects_completed_hours=(projects_completed/working_hours)
print("Projects Completed Per Working Hours:",(projects_completed_hours))
working_hours_project=(working_hours/projects_completed)
print("Working Hours Per Project:",(working_hours_project))
print("Employees Who Completed More Than 6 Projects:",(emp_id[projects_completed>6]))
print("Employees Who Worked More Than 180 Hours:",(emp_id[working_hours>180]))
print("Employees Completed 5 Projects & Worked 170 Hours:",(emp_id[(projects_completed>5)&(working_hours>170)]))
avg=(performance_score.mean())
print("Average Performance Score:",(avg))
print("Employees Whose Performance Above Average:",(emp_id[(performance_score>avg)]))
highest_performance=np.max(performance_score)
print("Highest Performance Score:",(highest_performance))
lowest_performance=np.min(performance_score)
print("Lowest Performance Score:",(lowest_performance))
print("Median Performance Score:",np.median(performance_score))
print("Standard Deviation Of Performance Scores:",np.std(performance_score))
performance=np.where(performance_score>85,"Excellent",np.where(performance_score>70,"Good","Needs Improvement"))
print("Employees Performance Category:",(performance))
attendance=np.where(attendance_emp>95,"Excellent Attendance",np.where(attendance_emp>85,"Good Attendance","Poor Attendance"))
print("Employees Attendance Category:",(attendance))
emp=(performance_score>85)&(attendance_emp>95)
print("Employees Are High Performance But Have Low Attendance:",(emp_id[emp]))
emp_workload=(working_hours>180)&(performance_score<80)
attendance_emp=(present_days/working_days)*100
print("Employees High Workload But Low Performance:",(emp_id[emp_workload]))
emp_productivity=(projects_completed>7)&(performance_score>85)
print("Employees High Productivity:",(emp_id[emp_productivity]))
emp_management=(attendance_emp<90)|(performance_score<70)
print("Employees Need Management Attention:",(emp_id[emp_management]))
print("Attendance Percentage To Two Decimal:",np.round(attendance_emp,2))
print("Projects-Per-Hour To Three Decimal Places:",np.round(projects_completed_hours,3))
print("Square Root Of Performance Scores:",np.sqrt(performance_score))
print("Square Root Of Performance Scores Use Power:",np.power(performance_score,2))
print("Employees Performance & Company Average:",np.abs(performance_score-avg))

print("\n===========FINAL MANAGEMENT REPORT===========")
attendance_emp=(present_days/working_days)*100
projects_completed_hours=(projects_completed/working_hours)
working_hours_project=(working_hours/projects_completed)
performance=np.where(performance_score>85,"Excellent",np.where(performance_score>70,"Good","Needs Improvement"))
attendance=np.where(attendance_emp>95,"Excellent Attendance",np.where(attendance_emp>85,"Good Attendance","Poor Attendance"))

print("Employee ID|Department|Attendance%|""Projects|Hours|Projects/Hour|Performance")
for i in range(len(emp_id)):
    print(emp_id[i],"|", department[i],"|", attendance_emp[i],"|", projects_completed_hours[i],"|", working_hours_project[i],"|", performance[i],"|", attendance[i])
    
count_excellent=np.sum(performance=="Excellent")
count_good=np.sum(performance=="Good")
count_needs_improvement=np.sum(performance=="Needs Improvement")
print("Excellent Category:",count_excellent)
print("Good Category:",count_good)
print("Needs Improvement Category:",count_needs_improvement)

below_90=np.sum(emp_attendance_90<90)
print("Attendance Below 90%:",below_90)

performance_score_employee=projects_completed>=7
performance_score_employee_completed_more=np.mean(performance_score[performance_score_employee])
print("Performance Score Employees Completed 7 More:",(performance_score_employee))
print(round(performance_score_employee_completed_more,2))

plt.plot(department,performance_score,marker='o',linestyle='--',label='Employee Productivity')
plt.xlabel("Department")
plt.ylabel("Performance Score")
plt.title("Employee Productivity")
plt.legend()
plt.show()

plt.bar(department,projects_completed,color='y')
plt.title("Employee Completed Projects")
plt.xlabel("Department")
plt.ylabel("Projects Completed")
plt.show()

plt.pie(emp_id,department=department)
plt.show()














