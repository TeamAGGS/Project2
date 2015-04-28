# Project2- Report
## Data Collection

## Anonymization

## Tables

## Data

## Data Samples

## Feature Detection
### Events
### Issues
We generate a set of derived features from the raw data using VB scripting in MS Excel. The code can be found by opening the Excel spreadsheet in developer mode. This macro enabled spreadsheet can be found at:

https://github.com/TeamAGGS/Project2/blob/master/Data-with-Features/issues_team1.xlsm

Similarly there are macro enabled spreadsheets for Team2 and Team3.

### Milestones
### Pull-requests

## Feature Detection Results
### Events
### Issues
Following features related to issues and issue-labels were found using VB scripting:
- Resolution Time in hours
- Issue start time in Date format
- Issue closing time in Date format
- Frequency of the usage of each issue labels

### Milestones
### Pull-requests

## Bad smell detector
### Events
### Issues
We imported these spreadsheets containing original data and features in Tableau for our further analysis. Tableau produces a family of interactive data visualization products focused on extracting and representing some patterns in the data. A fancy state of the art visualization can be created in a matter of seconds with simple drag-and-drop.

A very nice YouTube video give a short demo on how to create dashboards for Twitter data.

https://www.youtube.com/watch?v=uWIhdlnkEOM

We used similar methods to analyze our data and created dashboards for the same. Our Tableau file (ProjectReview.twb) can be found at https://github.com/TeamAGGS/Project2/tree/master/code

### Milestones
### Pull-requests

## Bad smell results
### Events
### Issues
We further categorize bad smells related to issues into three high-level questions.
#### What was the contribution of each user from project inception to completion?
##### Team1
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team1/Dashboard%201.jpg">

- From the first figure it’s interesting to see approx. 48% issues were unassigned. Who was accountable for these issues? *Were these issues created just for the sake of it?*
- The second figure shows the effort (number of issues they worked on) put in by each user (per week) as the semester went along. It can be seen that most of the work was done between the weeks 8-11 of the year 2015. Even during this period of high activity, user4 chose to be a silent member of the team. It would seem user4 worked on their 7 issues during the weeks 7-9, and then resigned from the organization.
- It can also be seen that the organization scrambled at the end to finish the project as they didn’t care about assigning issues to anyone.
- One more observation is shown in the top part of the figure in the figure below. In an academic project like this, it is expected from team members to take the role of mentorship (scrum master) at least once. However, from the figure below it seems that 

##### Team2
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team2/Dashboard%201.jpg">

- Given the high number of issues created in this repository, it’s safe to say that both the users worked on almost the same number of issues (first part of the figure above). Few issues were left unassigned which can be mapped to the phase when the team started documenting their results.
- From the second part of the figure it can be seen that although user2 contributed more hours/week to the project, user1 also had significant contribution. However, there is a period of two weeks (week 8-10) where we don’t see any contributions by user1.

##### Team3
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team3/Dashboard%201.jpg">

- To scrutinize this repository is a challenge in itself since it provides too less useful data. *It’s difficult to understand how much effort was put in by each member of the organization since almost all the issues are unassigned.*
- In the figure above, the effort level shows a spike around the time of mid-report submission and dormants to almost zero around week-12 and regains strength around the time of final submission. *We still don’t know who was sitting idle at this point while someone else was slogging all the way through.*
- There is a smattering of contributions made by user2 around submission deadlines.

#### How much process was followed throughout the project?
##### Team1
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team1/Dashboard%202.jpg">

- From the second part of the figure above, it can be seen that the members scrambled to finish work whenever a deadline approached. Issues were assigned and closed within an hour.
- Moreover, it would seem as if the members were keen on following the process of creating milestones, putting issues to a milestone and assigning issues to other members during the start of the project, but stopped doing this around the time of submissions, and scrambled to finish the work without giving attention to process. Here we see more than 50% of issues not being part of any milestone, and almost all of those issues were closed within less than an hour. *Were they just utility issues?*

##### Team2
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team2/Dashboard%202.jpg">

- From the top part of the figure below, it can be seen that the user2 took the role of “Team Lead” who was responsible for creating and assigning issues.
- From the figure above it can also be observed that the team had planned milestones and had added issues to milestones. The team also spent most of the time in the first milestone “Add ALL resources to Paper Comparison RepGrid”. It will be interesting to see approx. how many weeks were spent in achieving this milestone.
- The effort put in issues within a milestone are almost equal which is sign of good planning and execution. Also the effort put in core issues are more than the effort put in utility issues like report writing and documentation which is another good sign of effort distribution.
- There are very few issues that weren’t part of any milestone.

##### Team3
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team3/Dashboard%202.jpg">

- The first part of the figure above shows how many issues were created by users throughout the timeline of the project. It is clear from the figure above that user1 was the “Team Lead” of this organization. *The other two members have scattered contributions as far as taking charge of things is concerned.*
- The second part of the figure above partitions issues in their milestones and shows how much effort in hours was put in those issues. *Milestone V1 is quite interesting because it contains issues from the earlier phases of the project to the issues that were created during and after the Beta Launch.* 
- The milestone where all the testing was done (System test …) has very few issues assigned and very less effort was put in those issues. *Therefore, not a lot of effort was put into testing which goes against the benchmark laid out by Brooks.*

#### How frequently were each issue labels used?
##### Team1
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team1/Dashboard%203.jpg">

- It can be seen from the figure above that the frequency of usage of issue labels is skewed.
- The issue label “task” seems a filler label which could have been assigned any other issue label such as generate script or training or bug.
- The presence of issue label “team discussion” doesn’t make much sense in a repository. Did the team discuss through comments in the issues marked as team discussion? Or is there a link to their Skype or Hangout meetings in those issues?
- However, it’s good to find that the issue labels “bug”, “enhancement”, “generate script”, “Training” and “Testing” were used almost equally. It shows that the team followed a process similar to generate script → bug → enhancement → Training → Testing.

##### Team2
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team2/Dashboard%203.jpg">

- Most of issues have either label “Dead end”, “Writing” or “Step-4: Dimension added” assigned to them. This gives an indication that this is the repository of the Management track group where most of the issues involved documentation. 
- The high frequency of the label “Dead end” indicates that the team struggled to find relevant papers, and often they found themselves reading papers that weren’t of much use to them.
- Very less frequency of other issue labels is a concern. However, going by the name of those issue labels, it seems the team had a good process cycle (Our process → Step 0 → Step 1 → Step 2 → Step 3 → Step 4 → Writing), and they also kept a few things on hold (label = If time) for future.
- Overall, the team did a good job as far as mechanics of issues and effort is concerned.

##### Team3
<img src="https://github.com/TeamAGGS/Project2/blob/master/Figures/Team3/Dashboard%203.jpg">

- The figure above shows the frequency of usage of each issue labels. If we assume that the issue labels “design”, “develop” and “enhancement” relate to planning and coding phase of software development, and issue label “bug” and “test” relate to the testing phase, we see *approximately 70% of the occurrence of issue labels relate to the planning and coding phase, and only 10% belong to the testing phase.*
- However, we do see a software development life-cycle of Design → Develop  → Test  → Solved in this repository.
- The issue label “Solved” seems redundant since the closing of the issue itself indicates that the feature has been tested and is solved.

### Milestones
### Pull-requests

## Early warning
### Events
### Issues
The visualizations generated from Tableau were used to find some trends early in the life-cycle of the project which could be become a major problem later in the life-cycle. They are described in the "Early warning results" section.
### Milestones
### Pull-requests

## Early warning results
### Events
### Issues
- There is a major accountability issue early in the life-cycle in Team3. If we lookat the figure in the section **What was the contribution of each user from project inception to completion?** for Team3, we see almost all the issues in the early days weren't assigned to anyone.
- Also, in Team1, we observe that the user3 was responsible for most of the effort made towards the project in the first four weeks. This eventually turned out te be bad for the team as the user3 decided to dessert them later in the project.

### Milestones
### Pull-requests
