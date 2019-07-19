# coding: utf-8
import pandas as pd
import numpy as np
exp = pd.read_csv("GEO_GPL570_SCAN_135663samples_2019-07-02.tsv", index_col=0, sep="\t")
exp = exp[sorted(exp.columns)]
exp = exp.reset_index().rename(columns={"index": "Patient"})
studies = pd.read_csv("GSE_GSM.txt", sep="\t", names=["Patient", "Study"])
exploded_studies = pd.DataFrame(studies["Study"].str.rstrip().str.split(" ").tolist(), index=studies.Patient).stack().reset_index([0, 'Patient']).rename(columns={0: "Study"})
merged = pd.merge(exploded_studies, exp, on=["Patient", "Patient"])
vc = merged["Study"].value_counts()
small_groups = vc[vc < 5].index.tolist()
merged['Study'] = merged['Study'].apply(lambda x: "other" if x in small_groups else x)
merged.to_csv("merged.csv", index=False)
