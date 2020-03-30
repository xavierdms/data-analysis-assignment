### LICEcap GIF Walkthrough:

![alt text](https://github.com/xavierdms/data-analysis-assignment/blob/master/walkthrough.gif "LICEcap GIF Walkthrough")

### Design Diary:

The thing I struggled with the most was how to analyze individual scores and improvement and how to represent that in graphs. I tried a lot of ways of splitting up the scores, as I had originally planned to base most of the project on the differences between groups of students by grade on the pre test. Using average scores of different groups or sections was easier to represent, but the analysis part was still lacking. 

Another difficulty was with graphing any line of best fit. I tried a number of ways including using different libraries and couldn't figure it out. My guess is that the inputs/values I was trying to use for that just weren't the ones I should be using and so the output didn't make sense. 

Part of the difficulties came from lack of familiarity and experience with data analysis and statistics as a whole. Combined with learning how to use pandas, even though overall it's pretty accessible and it's not difficult to find answers on how to do most simple things, it ended up being a lot more time consuming than it needed to be. But again, a big part of the issue was not even knowing what to search for or having trouble thinking through to come up with a solution or approach.

I ended up only doing side by side comparisons of various averages according to some of the minimum requirement prompts (scores on the test and the final course grade,  pre and post tests, differences in grades between instructors and terms).

The only thing that I really completed as I intended to was the script to calculate test scores. It was definitely an exercise in iteration through arrays using Python, which I hadn't done much before. What took some time with that was figuring out how to look at the right cells and how to count right answers by comparing them to the KEY row in the dataset. I thought it would be easier to just calculate the score as a fraction of right answers over total questions, and convert it to a percentage to make it easier to compare to percent grades in the class.