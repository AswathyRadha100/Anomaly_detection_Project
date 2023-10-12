--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#                                                                                                                                                                                                           #
# Anomaly Detection Project
#                                           
#                                                                                                                                                                                                           #  
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Description** 

###     This project revolves around a comprehensive examination of curriculum access patterns within the educational program at Codeup. The objective is to address several key questions and uncover valuable insights from the data to optimize the educational experience and ensure compliance with access policies.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## **Project Goal** 

###  The main goals of the project are
  - &#9733; Analyze curriculum access patterns within the Codeup 
  - &#9733; Identify lessons that consistently attract high traffic across multiple cohorts for each program
  - &#9733; Investigate cohort behavior to find instances where a cohort significantly deviates from the norm in accessing specific lessons
  - &#9733; Examine the engagement of students, particularly those who access the curriculum infrequently during their active periods
  - &#9733; Detect and investigate any signs of suspicious activity, such as unauthorized access, web scraping, or suspicious IP addresses 
  - &#9733; Verify compliance with access policies that restrict students and alumni from accessing both web development and data science curriculums

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Initial Thoughts**

### In the initial phases, anticipated identifying specific lessons that consistently attract high traffic across multiple cohorts,likely that some students exhibit low curriculum access during their active periods,suspected unauthorized access, web scraping, and the presence of suspicious IP addresses that needs investigation.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **The Plan**
- &#9733; Acquire data from curriculum_logs using acquire.py
- &#9733; Prepare data using prepare.py
- &#9733; Explore data to find anomalies 
  
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Data Dictionary** 



| Column Name | Data Type | Definition                                      |
|-------------|-----------|-------------------------------------------------|
| date        | object    | Date when the access occurred.                  |
| time        | object    | Time of day when the access occurred.           |
| path        | object    | URL or path accessed by the user.               |
| user_id     | int64     | Unique identifier of the user.                 |
| cohort_id   | float64   | Identifier of the user's cohort.               |
| ip          | object    | IP address of the user's device.               |
| id          | float64   | Identifier associated with the cohort.         |
| name        | object    | Name or label of the cohort.                   |
| slack       | object    | Slack-related information for the cohort.     |
| start_date  | object    | Start date of the cohort.                      |
| end_date    | object    | End date of the cohort.                        |
| created_at  | object    | Date and time when the record was created.    |
| updated_at  | object    | Date and time when the record was updated.    |
| deleted_at  | object    | Indicates if the record has been deleted (null if not deleted). |
| program_id  | float64   | Identifier of the educational program associated with the cohort. |


-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Steps to Reproduce** 

## Ordered List:
     1. Clone this repo.
     2. Acquire the data. 
     3. Run data prepare. 
     4. Explore data using provided notebooks.
     5. Replicate the Anomaly Detection Project process using the provided instructions.
     

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Recommendations**

## Actionable recommendations based on project's insights:
- &#9733; Review and enhance access controls and restrictions to prevent unauthorized access to curriculum paths
- &#9733; Investigate the suspicious activity during off-peak hours to identify potential web scraping activities and take appropriate measures
- &#9733; Continuous Monitoring

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


## **Takeaways and Conclusions**

Takeaways: Monitoring and analyzing data access can provide insights into user behavior and potential issues. Access restrictions should be strictly enforced to maintain data security and program integrity.

In conclusion, this project has revealed various patterns and potential issues related to data access and curriculum usage. It's essential to address these issues to ensure program integrity and data security.
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------


