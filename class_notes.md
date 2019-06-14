# Notes taken in class

## 2019-01-22

Next week:

- Have the structure of your paper written out
- Write Methods section completely
  - Don't wander around, just tell the reader what is important to the hypothesis
  - This is a place for subtle oddities in your work (a fish died so it wasn't balanced, or whatever)
  - Come up with subsections, each should probably have a few paragraphs

## 2019-01-29

When he reviews our papers, Jerry will look for how the ideas in our methods relate to our hypothesis.

## 2019-02-19

Four paragraphs in an introduction

1. Hook / funnel - about 2 steps away from the main point
2. Talk about all the awesome stuff that's been done (noble failure at the end)
3. "To address this question, what we need is...", then brief description of study system & how it can be used to address the noble failure, lead up to next paragraph
4. Introduce the hypothesis or hypotheses: "In this study, we address this question by addressing the following hypotheses."

Could be fewer or more paragraphs, but this ^ generally works well.

There should probably be about 10-15 citations within the introduction.

Make sure to transition between paragraphs.

**Think about the title this week.**

Don't come on Thursday.

## 2019-02-26

### Purpose of the discussion

What do I think matters most about my work?

Tell the reader the 4 things that I think are most important about my work. These should deliver to the people that are targeted in your funnel in the intro.

We'll then keep the 3 most important things. *Don't* talk about every single implication / everything that comes to mind. These 3 things should be roughly equally weighty.

**This week**:

- Find 3 papers I love & figure out why
- Bring the 4 most important implications

## 2019-03-05

Funnel starts wide to get more readers, discussion is the payoff for those readers.

Ask: what is the value added from discussion over results?

- Put in context of other studies (Like Smith et al, we find; This connects studies [X, Y, Z], we did something that other studies didn't do)
- Next steps (it's still a problem that many tools aren't usable, maybe put it in a docker?)
- Call to action
- Explanation
  - Pattern (we found y, what are the x's that cause it?)
- Implications

Cool if you can mix a few of the above types of points.

(Don't apologize for problems in your study)

**Next week**:

- We'll eat pizza together
- Discussion is due in 2 weeks

## 2019-03-19

### Title

- First recruiting pitch for your paper
- "Cast a broad net with your title"
  - Try to start more broad; the journal will ask you to change it if they want
- Different title ploys
  - Brief question & answer
  - Action title (what's the verb?) (instead of "Effects of X on Y")
  - Check out the conventions (length & nature) of titles in the journal
- Does the title of papers affect impact factor / citations?

### Abstract

- Shortened version of your paper, order should be consistent with sections of your paper (like one sentence per section)
- Keywords are there to help people find your work. Who do you want to find & read your paper?

### Cover letter

- "Speed dating" / cold contact with the editor
- Tell them:
  - The paper isn't being considered elsewhere
  - A summary of the interesting findings in the paper
  - People who might be good reviewers (qualifications, names, & "none of these researchers is aware of this work")

#### Dr. Piccolo

- Formalities
- High level intro, context in the field
- Reviewers - Jeff Leek, Evan Johnson, Guy at Yale

### Next week

- Finish discussion
- Work on title, abstract

## 2019-05-08 - Meeting with Dr. Piccolo

- Change every "genetic data", "biological data" -> "gene expression"

### Abstract

- Funnel:
  - Gene expression data
  - Confounding effects
    - Different conditions
    - Covariates like cancer type that we're not interested in and have a strong effect on the data
    - Combining across datasets

### Intro

- Have at least 5 references on gene expression + neural networks (show there's breadth to the claim)

### Methods

- Add a few words about louizos findings (show DVAEs are effective and cool)
- ReLU - say what it stands for
- Dropout & batch norm - how do they reduce overfitting? at most 1 sentence on the mechanism
- TCGA - batch -> confounding

### Results

- MSE/MMD - put actual numbers instead of "by a factor of..."
- Important signal -> class-related signal

### Discussion

- Usually there aren't subsections
- General flow / outline
  - Talk about motivation for using NNs - confounding effects in any gene expression experiment. We assume these are both linear & nonlinear.
  - High level description of our results
  - Caveats (which scenarios were good?) - limitations of NNs in general
  - Every dataset might need a different

- Observations for people who use batch adjusters
- Observations for people who write batch adjusters

- Dr. Piccolo is OK with using questions:
  - How can I tell how well batch adjustment worked?
  - Which batch adjuster should I use?
  - What limitations does Confounded have?
    - Limitation, then idea for addressing the limitation
  - What else might Confounded be used for?

## What I've done

- Changed the title
- Reworked the abstract
- Reworked the first "Background" paragraph
- Added about 5 references to the claim that DNNs work with expression data
- Added a few words about the Louizos findings (VFAE) showing that it's effective
- Added what ReLU stands for
- Added R & RStudio version numbers
- Added explanations about dropout and batch norm
- Changed TCGA wording "batch effect"->"confounding effect"
- Changed "important signal"->"class-related signal"
- Updated the MNIST digits image and the caption
- Put actual numbers instead of improvement ratios for MSE / MMD

---

"Blurry" section - images / other expression data
"Confounded may be a viable replacement method" -> is an effective alternative
Code & instructions for running it can be found at URL

## What I've done

Results

- Added a few sentences at the beginning describing the study
- Removed the "Various previous studies" section
- Changed the tables to only have 3 significant digits
- Added tables for MSE and MMD scores

---

## Notes from Gentri

Title Page

- ~~Your name should match what is on university records: Jonathan Bryan Dayton. Change this in both places it appears on the Title Page.~~
- ~~See if you can get “All Rights Reserved” to be exactly 1 inch from the bottom of the page (it looks like it’s 1 line too high). You might need to change the line spacing – it might help to make sure that it’s set to “single-spacing.”~~ - use `\centering` instead of `\begin{center}`.

Abstract

- ~~Change your name as described above.~~
- ~~Indent the paragraph.~~
- ~~Keywords: Delete the extra space before “batch effects” (it looks like there’s 2 spaces instead of 1).~~ adding a `\@` after the colon fixed this
- ~~URL text may be included but should not be included as a link (changing this will hopefully remove the blue box around it as well).~~ added the `hidelinks` option to `hyperref` and changed `\url`s to `\nolinkurl`s

Table of Contents

- ~~There should be a line of periods between all the headings and their corresponding page number (so add this for the Title Page through Background and for Results to the end.)~~

List of Tables

- ~~Instead of just listing the number, it should be “Table 1,” Table 2,” etc.~~
- ~~Typically the table title is the first sentence (or only sentence) of the table heading. Not sure if it was intentional to leave out the rest of the sentence, but unless you want to keep it the way you have it, include the full title on the List of Tables (and then bold the full title in the actual text as well).~~ - I prefer it the way it is, is that OK?

List of Figures

- ~~Same for the figures: Figure 1, Figure 2, etc.~~
- ~~The figure title is typically the first sentence of the figure caption. So similar to the tables, consider making the full sentence the figure title (and bolding the actual text below the figure).~~

Body Text

- ~~There shouldn’t be any colored boxes around any of the text (green, red, etc.).~~
- ~~Hyperlinks: Just like in the abstract, the URL text can be included but make sure that it is not actually a link (and make sure that the blue box is removed as well).~~

Headings

- ~~Between 2.2.1 MNIST and before 2.2.2 Bladderbatch there is some bolded font: Synthetic Batch Effect. Should this be a heading? If so, number it like you have the other ones, include it in the Table of Contents, include a bookmark for it, and have the paragraph text start on the next line.~~

Tables

- ~~Move the tables so they are at the top of the page as opposed to at the bottom (Table 1) or in the middle (Table 2 and Table 3).~~

Figures

- ~~“Figures” should be on the same page as Figure 1 (instead of it appearing on a page all by itself).~~
- ~~Figure 2: Bold “of Confounded,” so that the full title is bolded (as listed on the List of Figures).~~

Bookmarks

- ~~The bookmark to “Tables” is too low (i.e. “Tables” is not visible).~~
- ~~The bookmarks to the tables should include the Table number and title.~~
- ~~Remove the duplicate bookmarks for Table 2 and Table 3.~~
- ~~The bookmark to “Figures” is too low (i.e. “Figures” is not visible).~~
- ~~Figure 8 and Figure 9 link incorrectly (they go to Table 2).~~

Embed Font

- This isn’t important yet, but when you submit your ETD, make sure that all fonts are embedded.

---

- Email the group re: fun lab activity
- 30-40 minutes
- Put xor problem in slides

- Timing OK (24 min), could slow down
- Simplify stuff - too much to digest - Give a better overview at the beginning - answer the WHYs
- Don't need to present ALL of the results - start with MNIST - Start with the why for each dataset & maybe just use GSE or bladderbatch - then use TCGA - sanity check -> batch effects -> other confounders
- Network diagram was "off the deep end too soon" - start with what a neural network is & why & what is an autoencoder
- Why predict batch, true class
- Publicly available & tools we used - maybe move to end
- Add acknowledgments slide
- Graphs aren't colorblind safe (OK for presentation, bad for submission)
- More focus on the why, the story, a view into the results but not everything
- Presentation is with general public, then discussion time with the committee - make the presentation more general
- Don't waste brain cycles on whether you'll pass
- Not pictured slide - bold a few bullet points, or break down into what made a diff, what didn't
- Add (higher = better) / (lower = better)
- Think in teaching mode instead of in technical overview mode
- Batch, true accuracy results - maybe add baseline dashed line

---

Story of my thesis

- What is a batch effect? - caterpillar example
  - These can be a special problem in gene expression data (why? what is gene expression data?)
  - What is a confounding effect?
  - How do you remove batch / confounding effects?
- Problems with previous approaches
  - Problem with our last study - we can find confounding effects even more after adjustment!
  - Why might this be? ^ Linear vs. Nonlinear, ComBat uses a linear approach
- So how do we deal with nonlinear effects?
  - Same problem occurred a while back in machine learning
  - Talk about perceptron and XOR problem
  - Mention problems with traditional pictures / metrics
  - After some research, it looks like most of the classic approaches use linear methods
  - We need some method that can model arbitrary nonlinear functions
  - Adding nonlinear functions between layers of perceptrons solve that problem and makes "universal function approximators" - deep neural networks, deep learning, this is how Google converts speech to text, recognizes images, and translates from one language to another (among other things)
- Stepping back to batch effects, how can we apply these neural networks to remove batch effects?
  - If we input data into this DNN, we want 2 things: a. the data to change as little as possible, and b. the batch to be removed
  - For constraint a, we can use an autoencoder
  - For constraint b, we can try to tell whether the batch is still there, and if it is, penalize the autoencoder
  - Show the overall schematic of Confounded, let them know it's called confounded & why
- Sometimes neural networks don't work... how can we tell whether it is working?
  - Dataset: MNIST + added batch
  - How can we validate our results (traditional plots and metrics, then use batch -- lower = better, and true class -- higher = better, classification with a variety of methods - why?)
  - Show MNIST results (looks pretty good!)
  - Process of setting defaults (what we tried, what worked, what didn't)
- Does it work with real-world data?
  - One issue with deep learning is that when it only sees a few instances, it memorizes instead of learning (this is called overfitting), and real datasets have traditionally been pretty small (but are getting bigger)
  - Next dataset: the one used in ComBat's documentation - pretty typical real-world dataset (talk about balance, small size) (talk about where the data came from)
  - Results for bladderbatch
- Does it work with other confounding effects?
  - At this point, we wanted to see how well we could do with the dataset we started with, and see how well we can remove real confounding effects
  - Did really well with TCGA (according to our new metrics, and did OK according to old metrics)
- How can other scientists use this method?
  - Now we'd seen that Confounded works well with image, small microarray, and large RNA-Seq datasets and with artificial batch, batch, and confounding effects.
  - We now want other scientists to be able to use our awesome method!
  - Code is publicly available at GitHub, Docker for scientists to download, read instructions, and easily use.
  - Talk about the tools we used
- Acknowledgments - Dr. Piccolo, my family, my wife, the dude in Japan who peer reviewed, the committee, my lab mates and office mates
- Questions?

Dr. Piccolo's comments

- Near beginning - briefly introduce gene expression data (central dogma, illumina sequencer) - needs more biological context
- Put link if I use other people's graphics
- Expand "How to remove batch effects" graphics
- TCGA dataset - introduce the actual data, what we were using it for, pancancer data, looking at patterns across cancer types
- Closing note before impact - maybe make the tcga figure with Confounded? at least put the numbers
- Talking about reviewer - mention Random Forests - mention that lower accuracy is better
- Make sure I don't completely equate NNs with MLP bc CNN/RNN/etc
- Before tuning, state "Neural networks are notoriously difficult to tune because there are so many parameters you can adjust" - make sure it's obvious that the hyperparameter tuning was with MNIST
- Red dashed lines
- Highlight True Class or Batch on boxplot slides + (Lower = Better)
- Add labels on the cut/paste/crop boxplots

---

Questions

- Why do I need to remove confounders?
- Why the word "adversarial"
- Could you add another "true class" discriminator?
- Why RNA data, not protein expression? (historical data)
- Give a coherent response to Dr. Clement

## 2019-05-31

I passed my final defense!!!
I'm done!
Except I still need to submit my thesis, but I need a paper from Dr. Piccolo before I can do that.
Also, I'm trying to submit to Bioinformatics by next Friday, so I need to fix / add a bunch of things that Dr. Piccolo recommended.
I'll collect below the issues that need to be fixed.

- Organize the paper with a similar flow to the defense
- Do experiments on sample size. How does Confounded work on TCGA when there are much fewer samples?
- Add the extra figures & descriptions from the presentation into the supplementary material

1. All code in GitHub
2. All data files in CodeOcean (OSF first, then CodeOcean after submission)?
3. Send to Dr. Piccolo link to GitHub repo with tex file.
