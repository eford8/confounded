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
