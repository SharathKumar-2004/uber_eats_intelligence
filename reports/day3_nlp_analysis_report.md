# Day 3: Customer Feedback Analysis Using NLP

## 1. Executive Summary

This analysis examines the synthetic Uber Eats review dataset using
traditional NLP, machine-learning sentiment classifiers, and VADER.

The best-performing evaluated method by macro F1 was **Naive Bayes**
with a macro F1 score of **1.000**.

## 2. Business Objective

The objective is to understand customer feedback, identify recurring
dissatisfaction themes, and demonstrate how NLP can support operational
improvements.

## 3. Dataset Overview

- Reviews analyzed: 1984
- Review text column: `review_text`
- Rating column: `rating`
- Sentiment labels: derived from star ratings (1–2 negative, 3 neutral, 4–5 positive)
- Dataset type: synthetic project data, not actual Uber Eats customer records

## 4. Sentiment Distribution

| sentiment   |   review_count |
|:------------|---------------:|
| negative    |            274 |
| neutral     |            274 |
| positive    |           1436 |

These labels are rating-derived proxy labels. They should not be treated as
independent human annotations of review sentiment.

## 5. Text Preprocessing

The traditional NLP pipeline applied lowercase conversion, URL and
punctuation removal, tokenization, stop-word removal, and lemmatization.

## 6. TF-IDF

TF-IDF converted review text into numerical features. Unigrams and bigrams
were used to capture individual terms and two-word phrases.

## 7. Model Evaluation

| method      |   accuracy |   precision_macro |   recall_macro |   f1_macro |
|:------------|-----------:|------------------:|---------------:|-----------:|
| Naive Bayes |      1     |             1     |          1     |      1     |
| Linear SVM  |      1     |             1     |          1     |      1     |
| VADER       |      0.725 |             0.499 |          0.477 |      0.484 |

The models were evaluated against rating-derived labels. Macro precision,
macro recall, and macro F1 provide a class-balanced view of performance.

## 8. VADER

VADER analyzed the original review text using a rule-based sentiment
approach. Its scores were compared with the same rating-derived labels
on the held-out reviews.

## 9. Potential Complaint Terms

Top terms extracted from negative rating-derived reviews:

- delivery
- slow
- delivery slow
- food
- could
- much
- better
- could much
- much better
- quality disappointing

These terms require manual review and do not independently establish
the cause of customer dissatisfaction.

## 10. Business Recommendations

1. Review low-rated comments to identify actionable delivery and food-quality issues.
2. Track negative-review share over time when reliable timestamps are available.
3. Validate automated sentiment predictions against manually labelled reviews.
4. Investigate frequent complaint themes with operational data before proposing interventions.
5. Monitor model performance across sentiment classes, not accuracy alone.

## 11. Limitations

- Sentiment labels were derived from star ratings rather than independent human annotations.
- Synthetic reviews may not represent real customer behavior or language.
- TF-IDF keyword rankings are not definitive complaint categories.
- VADER and traditional classifiers can misinterpret sarcasm, context, and mixed sentiment.
- Model scores against proxy labels do not prove real-world sentiment accuracy.

## 12. Conclusion

This project demonstrates a reproducible NLP workflow for review preprocessing,
TF-IDF feature extraction, sentiment classification, model evaluation, and
initial complaint-term analysis. Further validation with human-labelled reviews
is needed before using these results for operational decisions.

---

