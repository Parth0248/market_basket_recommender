# 🚀 Quick Start Guide

## Get Started in 3 Minutes!

### Step 1: Install Dependencies (30 seconds)

```bash
pip install -r requirements.txt
```

### Step 2: Train the Model (10 seconds)

```bash
python recommender.py
```

You should see output like:
```
Loaded 25 transactions with 20 unique products
Generating frequent itemsets...
Found 39 frequent itemsets
Generating association rules...
Generated 45 association rules
Model training completed!
```

### Step 3: Start the Web Application (5 seconds)

```bash
python app.py
```

### Step 4: Open Your Browser

Navigate to: **http://localhost:8000**

---

## 🎮 How to Use

1. **Select a Product** from the list on the left
2. **Click "Add Item"** to add it to your cart
3. **Watch Recommendations** appear automatically on the right
4. **Click on Recommendations** to add them to your cart
5. **See Updates** as recommendations refresh with each addition

---

## 🔥 Example Usage

### Scenario 1: Security System Setup

**Step 1**: Add "Bosch D7050 Detector" to cart
- System recommends: Control Panel, Motion Detector, Wireless Receiver

**Step 2**: Add recommended "DSC PG9914 Motion Detector"
- System updates recommendations: Alarm Kit (66% confidence!)

**Result**: Customer discovers complementary products they might have missed!

---

## 📊 Understanding Recommendations

Each recommendation shows:
- **Product Name**: What is being recommended
- **Confidence Score**: How often this item is bought together (higher is better)
- **Lift Score**: How much more likely this combination is vs random

Example:
```
DSC PowerSeries Neo Alarm Kit
66% confidence | Lift: 4.17
```
This means: 66% of customers who bought your cart items also bought this alarm kit, and they're 4.17x more likely to buy it together than separately!

---

## 🛠️ Troubleshooting

**Problem**: No recommendations showing
- **Solution**: This is normal! The combination of items in your cart may not have historical patterns. Try different product combinations.

**Problem**: Model training fails
- **Solution**: Make sure all dependencies are installed: `pip install -r requirements.txt`

**Problem**: Port 8000 already in use
- **Solution**: Use a different port: `uvicorn app:app --port 8001`

---

## 🎯 Next Steps

- Explore the **API Documentation** at http://localhost:8000/docs
- Read the full **README.md** for algorithm details
- Modify **data/transactions.csv** to add your own transaction data
- Adjust model parameters in **recommender.py** (min_support, min_confidence, min_lift)

---

## ⚡ One-Line Setup (Advanced Users)

```bash
pip install -r requirements.txt && python recommender.py && python app.py
```

---

**Happy Recommending! 🎉**
