# transfer-anomaly-lab

Interactive cross-border transfer anomaly detection with an autoencoder,
Isolation Forest baseline, and SHAP explanations.

Status: Still work in progress.

## What this is

An independent research and engineering project on detecting unusual
cross-border money transfers. It is inspired by the kind of risk patterns
that international payment services face. It is not affiliated with any
company and does not copy any company's product.

## Planned fraud patterns

Phase 1 (current target):
- First-time large transfer to a new country
- Unusual currency pair
- Velocity spikes

Phase 2 (if time allows):
- Structuring (splitting amounts to stay under limits)
- Dormant account reactivation

## Planned components

- Autoencoder anomaly scorer
- Isolation Forest baseline
- SHAP explanations per scored transaction
- FastAPI backend
- Web frontend with a live demo

## Data

To be documented. Data sources and any synthetic additions will be
described here.