1. # Description
   - ## Research Question
      - ### Our project is an analysis on the current state of public education in the country. Particularly, this project aims to answer the question: Are there enough teachers to support the rate of growth of the number of students in public schools in the country? An additional question this paper hopes to answer is how the rate of teacher’s salaries relate to the amount of teachers employed in public schools. With this supporting research question we aim to find possible factors relating to teacher’s employment so that we may find possible solutions to the problem.
   - ## Background 
      - ### “There may be changes to the curriculum or even to the physical condition of our classrooms and schools, but the condition of the teachers is the most important and should be given priority. Our teachers are still overburdened with redundant clerical work that gets worse every day. Class sizes can reach as high as 50 to 55, and yet we expect our teachers to teach better,” 
      ### \- TDC chairman Benjo Basas said in a separate statement.
	
      ### Education is vital to painting a brighter future for the youth, although the majority of children in the Philippines have access to education or have been educated, the question of quality still remains. The quality of education can detrimentally be influenced by the ratio between students and teachers. A teacher with too many students is unable to properly tend to all of them, which adversely affects the teachers’ well-being and the students’ learning experience and academic performance.

   - ## Hypotheses
      - ### For whether there are enough teachers to support the rate of growth of the number of students, we hypothesize that There is a statistically significant relationship between the amount of teachers and the amount of students enrolled in the Philippines.
         - ### Null Hypothesis: There is no significant relationship between the amount of teachers and the amount of students in the Philippines.
         - ### Alternative Hypothesis: There exists a statistically significant relationship between the amount of teachers and the amount of students in the Philippines.
      - ### As for how the rate of change of teacher’s salaries relate to the amount of teachers employed, we hypothesize that there is a direct correlation between the rate of growth of the salaries of teachers and the amount of teachers employed.
         - ### Null hypothesis: There is no relationship between the salaries of teachers and the amount of teachers employed in the Philippines.
         - ### Alternative Hypothesis: There exists a statistically significant relationship between the salaries of teachers and the amount of teachers employed in the Philippines.
2. # Data Set 
   - ## Sources
      - ### Original data set can be found [here](https://www.deped.gov.ph/alternative-learning-system/resources/facts-and-figures/datasets/). The pre-processed data google sheet can be found [here](https://docs.google.com/spreadsheets/d/1cBuVQqX7rkTXdTVc2JC6s8txDGckQg25vXUqh52-Bo8/edit?usp=sharing).
   - ## Description
      - ### The following data sets obtained are from the official datasets provided by the Department of Education. They have readily available data up to the School Year 2020-2021, which is the latest and available data used for the study.
      - ### The first data set contains the amount of Public School teachers in the Philippines. It is subdivided by what academic year the teachers taught in and it is further classified by what level of education they teach, namely: Elementary, Junior High School, and Senior High School, and what region they are located in. 
      - ### The second data set is the data containing the enrolment of students in the country. It includes enrollment data from private, public, and state universities and colleges (SUCs) and Local Universities and Colleges (LUCs), The data is also subdivided by the academic year the students were enrolled in, and further classified into the region the students are located in, their birth sex, their grade level, and in the case of Senior High School students, their strand.
         1. ### For the purpose of this study, only the data on Public School enrollees will be collected and considered as part of the data set. The enrollees for the Senior High School students are also combined by their grade level and not their specific strand.
         2. ### With DepEd’s special education program (Sped), an additional grade level is considered, labeled as Non-Grade. These are learners with special needs which require them not to be included in the regular class setup. They are also clustered by their level of education (Non-Grade Elementary and Non-Grade Junior High).

   - ## Data Set Size
      - ### The data set containing the enrollment data has 111,337,379 participants, ranging from AY 2016-2017 up to AY 2020-2021. Specifically, 21,398,088 were enrolled in AY 2016-2017, ranging from Kindergarten to Senior Highschool. Furthermore, 22,096,820 were enrolled in AY 2017-2018, 22,557,139 in AY 2018-2019, 22,572,923 in AY 2019-2020, and finally, 22,712,409 in AY 2020-2021.
      - ### For the data set containing the number of teachers in the country, there were a total of 4,000,702 participants, spread throughout AY 2016-2017 up to AY 2020-2021. Specifically, there were 724,005 in AY 2016-2017, 755,573 in AY 2017-2018, 808,089 in AY 2018-2019, 836,193 in AY 2019-2020, and finally, 876,842 in AY 2020-2021.
   - ## Pre-Processing
     - ### The data set for the enrollment data was arranged according to four criterias which contained the number of enrollees for each. They are grouped according to school year, region, grade level and birth sex. There were 2482 samples obtained from this.
     - ### A similar data set was obtained for the number of public school teachers, which lacks the birth sex criteria, thus there are only three criterias to group each sample. The data made available for teachers only categorizes them according to the level of education (Elementary, Junior High School, Senior High School), and not their specific grade level, which means there are only three different groups for this. A total of 255 samples were obtained using this criteria.

### References:
1. Bollozos, W. (2023, August 29). 'Glaring' teacher shortage on school opening day needs 'strategic' solutions — lawmaker. https://www.philstar.com/headlines/2023/08/29/2292294/glaring-teacher-shortage-school-opening-day-needs-strategic-solutions-lawmaker#:~:text=While%20DepEd%20in%20recent%20years,to%20have%20large%20class%20sizes.
2. Gumban, E. (2023, August 30). Teachers lament worsening education system. https://www.philstar.com/headlines/2023/08/30/2292411/teachers-lament-worsening-education-system
3. Inero, A., Galang, A., Dela Cruz, A., Dela Cruz, R. (2021, June 30). INVESTIGATING STUDENT-TEACHER RATIO AS A FACTOR IN READING PERFORMANCE: THE CASE OF THE PHILIPPINES. https://journal.uin-alauddin.ac.id/index.php/Eternal/article/view/20876
4. Rabago-Mingoa, T. (2017, June). Filipino teachers’ stress levels and coping strategies. https://www.dlsu.edu.ph/wp-content/uploads/pdf/conferences/research-congress-proceedings/2017/LLI/LLI-I-020.pdf
