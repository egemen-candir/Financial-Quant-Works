# 🚨 AML_Works: Sanctions-Aware Money Laundering Detection

This repository presents a **sanctions-enriched anti-money laundering (AML) pipeline** combining expert-crafted features, regulatory insights, and machine learning techniques. The project is designed to simulate a realistic AML detection framework using both **Logistic Regression** and **XGBoost**, enriched with external **sanctions data**.

---

## 📁 Repository Structure

```
AML_Works/
├── sanct_enricher.ipynb       # Enriches transaction dataset with sanctioned bank exposures
├── model_log_reg.ipynb        # Baseline Logistic Regression AML classifier
└── model-xgboost.ipynb        # Advanced AML model using XGBoost with threshold and feature analysis
```

---

## 🧠 Key Modules

### 1. `sanct_enricher.ipynb` — **Sanctions Enrichment**

- Merges sanctions lists with transaction data.
- Flags transactions based on whether **sender or receiver banks** are under sanctions.
- Adds a `sanctions_exposure_flag` feature used by downstream models.
- Ready to handle future sanctions lists from regulatory bodies (e.g., OFAC, UN).

### 2. `model_log_reg.ipynb` — **Logistic Regression Baseline**

- Implements AML-specific feature engineering:
  - Currency mismatch
  - Hour of day
  - Rounded transaction flags
  - Bank pair patterns
- Uses `class_weight='balanced'` to handle class imbalance.
- Outputs ROC, confusion matrix, classification report, and feature coefficients.

### 3. `model-xgboost.ipynb` — **XGBoost Classifier**

- Integrates enriched sanctions data (`sanctions_exposure_flag`).
- Handles extreme class imbalance using `scale_pos_weight`.
- Auto-detects non-linear feature interactions (e.g., risk at sanctioned bank + high-risk hours).
- Includes:
  - Feature importance (gain & weight)
  - ROC-AUC and threshold analysis
  - Visual distribution of laundering scores
- Reports operational insights: alert volume, precision/recall tradeoffs.

---

## 📊 Sample Results

- **ROC AUC Score (XGBoost)**: ~0.975  
- **Top Features**:
  - `payment_format_encoded`
  - `amount_difference`
  - `account_encoded`
  - `sanctions_exposure_flag` (ranks in top 10 under some thresholds)

---

## 🔍 Use Cases

This framework simulates core detection logic that could be deployed in:

- 🔒 **Bank transaction monitoring systems**
- 🌐 **Cross-border payment audits**
- 🕵️ **Sanctions compliance risk scoring**