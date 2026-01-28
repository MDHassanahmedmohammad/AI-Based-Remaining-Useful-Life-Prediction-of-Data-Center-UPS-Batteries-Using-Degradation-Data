# AI-Based Remaining Useful Life Prediction of Data Center UPS Batteries

## 📌 Overview
This repository presents a machine learning–based approach for predicting the **Remaining Useful Life (RUL)** of lithium-ion batteries used in **Uninterruptible Power Supply (UPS)** systems for data centers. Accurate RUL prediction enables predictive maintenance, improves system reliability, and reduces unexpected battery failures in mission-critical infrastructure.

The project uses real battery degradation data and develops a baseline, interpretable machine learning model for cycle-level RUL estimation.

---

## 🧠 Abstract
This project presents a machine learning–based approach for predicting the Remaining Useful Life (RUL) of lithium-ion batteries used in data center UPS systems. Using real degradation data, a Random Forest model achieves accurate RUL estimation with low prediction error, supporting data-driven predictive maintenance.

---

## 📂 Dataset
- **Source:** NASA Lithium-Ion Battery Degradation Dataset  
- **Batteries used:** B0005, B0006, B0007, B0018  
- **Observations:** 636 discharge-cycle observations  
- **RUL samples:** 336 (from batteries that reached end-of-life)

Each observation corresponds to a complete discharge cycle.

**End-of-Life (EOL) criterion:**  
Battery capacity ≤ 70% of initial capacity.

---

## ⚙️ Methodology
### Features
- Discharge cycle number  
- Discharge capacity (Ah)  
- State of Health (SOH)

### Model
- Random Forest Regressor (baseline)
- Supervised regression for RUL prediction

### Evaluation Metrics
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## 📊 Results
- **MAE:** 1.86 cycles  
- **RMSE:** 2.99 cycles  

Key findings:
- Predictions closely follow actual RUL values
- Error distribution is centered around zero
- Feature importance analysis shows SOH contributes over 92% of predictive power

---

## 📈 Visualizations
The repository includes:
- Battery capacity degradation curves
- Actual vs predicted RUL plot
- RUL prediction error distribution

All figures are stored in the `outputs/` directory.

---

## 🗂️ Repository Structure
