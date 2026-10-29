# Uber Eats Operational & Customer Intelligence System

## Day 01: Project Setup, Synthetic Data Generation & Prompt Engineering

**Project:** Uber Eats Operational & Customer Intelligence System\
**Day:** 01\
**Status:** Project setup and synthetic-data generation tasks were part
of the initial workflow. Update checkboxes to reflect the final state of
your repository.

------------------------------------------------------------------------

## 1. Day 01 Objectives

-   Set up the project repository and development workflow.
-   Create a dedicated Git feature branch.
-   Prepare the initial project structure and Python dependencies.
-   Generate synthetic datasets representing the Uber Eats business
    workflow.
-   Practice structured prompting using the P.T.C.F. framework and
    few-shot examples.

## 2. Project Overview

The project aims to build an operational and customer intelligence
workflow for a food-delivery platform. The planned analytics areas
include:

-   Customer and restaurant segmentation
-   Customer-review sentiment analysis
-   Delivery-time prediction
-   Hourly order-demand forecasting
-   Recommendation opportunities

The project uses synthetic data for development and experimentation.
Results from synthetic data should not be presented as evidence of
actual Uber Eats business performance.

## 3. Development Setup

The project was developed in VS Code with Git/GitHub version control.

-   Repository: `uber_eats_intelligence`
-   Feature branch: `feature/uber-eats-pipeline`
-   Remote repository: `SharathKumar-2004/uber_eats_intelligence`

Initial setup items:

-   [ ] Confirm project folder and Git repository.
-   [ ] Confirm feature branch.
-   [ ] Add `.gitignore`.
-   [ ] Add `requirements.txt`.
-   [ ] Add a README with project scope and progress.
-   [ ] Commit and push the initial project files.

## 4. Synthetic Dataset Plan

The project dataset files include:

  -----------------------------------------------------------------------
  Dataset                             Intended role
  ----------------------------------- -----------------------------------
  `customers.csv`                     Customer attributes for
                                      customer-level analysis and
                                      segmentation

  `restaurants.csv`                   Restaurant attributes for
                                      restaurant analysis and
                                      segmentation

  `orders.csv`                        Order details and order-level
                                      features

  `deliveries.csv`                    Delivery distance, conditions,
                                      preparation time, and delivery-time
                                      target

  `drivers.csv`                       Driver-related attributes for
                                      operational analysis

  `reviews.csv`                       Review text and sentiment analysis

  `payments.csv`                      Payment-related fields for order
                                      and payment analysis
  -----------------------------------------------------------------------

The exact fields and relationships should be verified against the CSV
files in the project repository.

## 5. Prompt Engineering

The initial learning tasks included structured prompting with
**P.T.C.F.** and few-shot examples.

### P.T.C.F. framework

Use the framework to structure prompts around:

-   **P --- Persona:** define the role the AI should take.
-   **T --- Task:** specify the requested work.
-   **C --- Context:** provide the relevant project details,
    constraints, and data.
-   **F --- Format:** define the expected structure of the output.

### Few-shot prompting

Few-shot prompting supplies a small number of examples showing the
desired input-output pattern. It can help the model follow a consistent
structure, but outputs still need validation.

## 6. Day 01 Deliverables

-   [ ] Project repository and branch checked.
-   [ ] Initial project files prepared.
-   [ ] Synthetic CSV datasets generated and inspected.
-   [ ] Prompt-engineering examples documented.
-   [ ] Initial changes committed and pushed.

## 7. Key Learnings

-   Git branches allow development work to be isolated before merging.
-   A clear project structure makes analysis easier to maintain.
-   Synthetic data can support pipeline development and testing, but
    does not establish real-world performance.
-   Structured prompts improve clarity by specifying role, task,
    context, and output format.

## 8. Next Steps

1.  Inspect the generated CSV files and verify columns, data types,
    missing values, and relationships.
2.  Prepare a repeatable preprocessing and exploratory data analysis
    workflow.
3.  Build customer and restaurant segmentation models.
4.  Record assumptions and validate all findings against actual outputs.

