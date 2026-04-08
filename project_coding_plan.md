# Flight Risk Coding Plan

## What the current `idea.md` implies

The project goal is to predict flight disruption risk for an MVP where a user enters:

- origin
- destination
- travel date

and receives flight options ranked by likelihood of:

- on time
- short delay (`< 30 min`)
- long delay (`>= 30 min`)
- cancelled

## What data you already have

### Best dataset for MVP

Use `flights_with_weather.parquet` or `flights_with_weather.csv` as the main modeling dataset because it already combines:

- flight history
- route information
- airline information
- delay and cancellation outcomes
- origin weather
- destination weather

### Supporting datasets

- `ALL_FLIGHTS_2021_2023.csv`: larger raw flight dataset
- `flights_sample_2021_2023_10k.csv`: fast prototyping
- `flights_sample_2021_2023_100k.csv`: medium-size experimentation
- `Tornadoes_SPC_1950to2015.csv`: not ideal for MVP unless you build a separate location/date join pipeline

## Important gaps between the idea and the actual data

1. `idea.md` says the dataset is from 2018-2022, but the available files appear to cover 2019-2023.
2. The tornado dataset is much older and would require additional geographic matching logic before it helps predictions.
3. The current files do not appear to include a ready-made future flight schedule feed, so the MVP should begin as a route/date risk estimator rather than a live booking-style ranking engine.

## Coding that needs to be done

## Phase 1: Data pipeline

### 1. Create a project structure

You need code files for:

- `src/data/load_data.py`
- `src/data/clean_data.py`
- `src/features/build_features.py`
- `src/models/train.py`
- `src/models/evaluate.py`
- `src/inference/predict.py`
- `app.py` or `api.py`

### 2. Build dataset loading code

Code needed:

- load `.csv` and `.parquet`
- optionally switch between sample and full datasets
- select only needed columns
- enforce correct dtypes for dates, numeric delay fields, and categorical airline/airport columns

### 3. Build target labels

Code needed to create the 4-class target from each row:

- `cancelled` if `CANCELLED == 1`
- `long_delay` if not cancelled and `ARR_DELAY >= 30`
- `short_delay` if not cancelled and `0 < ARR_DELAY < 30`
- `on_time` if not cancelled and `ARR_DELAY <= 0`

This is the single most important label-engineering step.

### 4. Clean leakage from the dataset

Many columns should not be used at prediction time because they are only known after departure or arrival.

Do not use these as model inputs for the MVP:

- `DEP_TIME`
- `DEP_DELAY`
- `WHEELS_OFF`
- `WHEELS_ON`
- `ARR_TIME`
- `ARR_DELAY`
- `ELAPSED_TIME`
- `AIR_TIME`
- `TAXI_OUT`
- `TAXI_IN`
- `DELAY_DUE_CARRIER`
- `DELAY_DUE_WEATHER`
- `DELAY_DUE_NAS`
- `DELAY_DUE_SECURITY`
- `DELAY_DUE_LATE_AIRCRAFT`

Use only features that would realistically be known before departure.

### 5. Build usable model features

Code needed for feature engineering:

- parse `FL_DATE` into:
  - month
  - day of week
  - weekend flag
  - holiday-season flag
- convert `CRS_DEP_TIME` into:
  - scheduled departure hour
  - time-of-day bucket
- encode:
  - `AIRLINE_CODE`
  - `ORIGIN`
  - `DEST`
- keep numerical features such as:
  - `DISTANCE`
  - `CRS_ELAPSED_TIME`
  - origin weather columns
  - destination weather columns

### 6. Add route history aggregates

This will likely improve the model more than adding tornado data.

Code needed to compute historical aggregates such as:

- average delay by airline
- average delay by route (`ORIGIN` + `DEST`)
- cancellation rate by route
- cancellation rate by airline
- airport-level delay rate at origin
- airport-level delay rate at destination

These aggregates must be computed only from training data to avoid leakage.

## Phase 2: Modeling

### 7. Start with baseline models

Implement:

- multinomial logistic regression baseline
- random forest or gradient boosting baseline

Best practical first choice:

- gradient boosting model on engineered tabular features

If using Python later, good libraries are:

- `pandas`
- `scikit-learn`
- `xgboost` or `lightgbm`

### 8. Train with time-aware splitting

Do not randomly split the data.

Code needed:

- train on earlier dates
- validate on later dates
- test on the most recent dates

Example:

- train: 2019-2021
- validation: 2022
- test: 2023

This better matches real forecasting.

### 9. Evaluate both class and probability quality

Code needed for:

- class distribution summary
- confusion matrix
- macro F1
- per-class precision/recall
- log loss
- calibration plot if possible

For the product, predicted probabilities matter more than just the hard class label.

## Phase 3: Inference and product logic

### 10. Build a prediction function

Code needed for an inference function that accepts:

- origin
- destination
- airline
- flight date
- scheduled departure time
- optional weather inputs

and returns:

- probability of `on_time`
- probability of `short_delay`
- probability of `long_delay`
- probability of `cancelled`
- a combined risk score for ranking

### 11. Define the ranking formula

Code needed for a product score such as:

`risk_score = 1.0 * P(cancelled) + 0.6 * P(long_delay) + 0.2 * P(short_delay)`

Then rank lowest-risk options first.

### 12. Build explanation outputs

The idea mentions user-friendly guidance, so code should return:

- top 3 factors affecting the risk score
- a short explanation string

Example:

- "This route has elevated delay risk because of winter weather at the destination and poor recent on-time performance for this route."

## Phase 4: User interface

### 13. Build a very small MVP app

You only need one simple interface at first:

- input form for origin, destination, date
- optional airline and departure time
- output table of risk probabilities and ranking

Implementation options:

- Streamlit for fastest demo
- Flask/FastAPI + simple HTML

### 14. Handle the missing live flight list problem

Because the current dataset is historical, the first UI should likely do one of these:

1. Let users choose from historically common airlines/routes.
2. Simulate candidate options from historical flights on that route.
3. Show route-level risk instead of exact future flight numbers.

For a 6-week MVP, option 3 is the safest.

## What should be built first

Recommended build order:

1. Create the 4-class target.
2. Remove leakage columns.
3. Train a baseline classifier on sample data.
4. Evaluate on a time-based split.
5. Add route/airline historical aggregates.
6. Wrap inference in a simple app.
7. Add explanations.

## Minimum viable deliverable

If time is short, the MVP can be:

- a model that predicts the 4 disruption classes
- a route/date risk estimator
- a small web app that displays probabilities and a ranked reliability score

This is enough to match the project brief without solving live airline search.

## Stretch goals

Only after the baseline works:

- add tornado or storm matching
- add SHAP explanations
- retrain regularly with new data
- integrate real weather forecasts
- integrate live schedules or booking APIs

## Recommendation

The best next coding move is:

- build the data-cleaning and target-label pipeline on `flights_sample_2021_2023_100k.csv`
- validate the approach there
- then scale to `flights_with_weather.parquet`

That gives you a fast path to a working model and keeps the MVP aligned with `idea.md`.
