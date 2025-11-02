# Electronic Retailer Market Basket Recommendation System

[![SJSU](https://img.shields.io/badge/SJSU-CMPE%20256-blue)](https://www.sjsu.edu)
[![Python](https://img.shields.io/badge/Python-3.8+-green)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104-teal)](https://fastapi.tiangolo.com/)

**CMPE 256 Recommender Systems - Data Science Hackathon**  
**San José State University - Fall 2025**  
**Team Members**: Parth Maradia(019104527), Kalhar Patel(019140511), Abhishek Darji(019113471)

---

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Algorithm Details](#algorithm-details)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Testing](#testing)
- [Future Enhancements](#future-enhancements)
- [Contributors](#contributors)
- [License](#license)

---

## 🎯 Project Overview

This project implements an intelligent **Market Basket Recommendation System** designed for an electronic retailer's online checkout process. The system analyzes historical transaction data to identify frequently purchased product combinations and provides real-time recommendations to customers as they build their shopping cart.

### Problem Statement

When customers shop online, they often miss complementary products that others frequently purchase together. This system addresses that gap by:

1. **Analyzing** historical transaction patterns using Association Rule Mining (Apriori Algorithm)
2. **Identifying** products frequently bought together
3. **Recommending** relevant items dynamically as customers add products to their cart
4. **Updating** recommendations in real-time based on cart contents

### Business Value

- **Increased Revenue**: Cross-selling and upselling opportunities
- **Enhanced UX**: Personalized shopping experience
- **Data-Driven Insights**: Understanding customer purchase patterns
- **Scalable Architecture**: FastAPI microservice ready for production deployment

---

## ✨ Features

### Core Functionality

- ✅ **Real-time Recommendations**: Dynamic product suggestions based on current cart
- ✅ **Association Rule Mining**: Apriori algorithm with configurable support, confidence, and lift thresholds
- ✅ **Interactive Web Interface**: User-friendly checkout portal
- ✅ **RESTful API**: FastAPI-based microservice architecture
- ✅ **Confidence Scoring**: Recommendations ranked by statistical confidence and lift
- ✅ **Graceful Handling**: No recommendations for unprecedented item combinations
- ✅ **Iterative Updates**: Recommendations refresh with each cart modification

### Technical Features

- 🔧 **Model Persistence**: Save and load trained models
- 🔧 **Configurable Parameters**: Adjustable min_support, min_confidence, min_lift
- 🔧 **Comprehensive API**: RESTful endpoints for all operations
- 🔧 **Health Monitoring**: System health check endpoint
- 🔧 **Production Ready**: Deployable as FastAPI/microservice

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Frontend (HTML/JS)                       │
│  - Product List Display                                      │
│  - Shopping Cart Management                                  │
│  - Real-time Recommendation Display                          │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │ HTTP/REST API
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                   FastAPI Application                        │
│  - API Endpoints                                             │
│  - Request Validation                                        │
│  - Response Formatting                                       │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │
┌─────────────────────▼───────────────────────────────────────┐
│              Recommendation Engine                           │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  1. Data Preprocessing                                 │ │
│  │     - Transaction Encoding                             │ │
│  │     - Basket Format Conversion                         │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  2. Apriori Algorithm                                  │ │
│  │     - Frequent Itemset Generation                      │ │
│  │     - Support Calculation                              │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  3. Association Rules Mining                           │ │
│  │     - Rule Generation                                  │ │
│  │     - Confidence & Lift Filtering                      │ │
│  └────────────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  4. Recommendation Generation                          │ │
│  │     - Cart Analysis                                    │ │
│  │     - Rule Matching                                    │ │
│  │     - Ranking & Filtering                              │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────┬───────────────────────────────────────┘
                      │
                      │
┌─────────────────────▼───────────────────────────────────────┐
│                   Data Storage                               │
│  - Transaction Dataset (CSV)                                 │
│  - Trained Model (Pickle)                                    │
│  - Association Rules                                         │
└─────────────────────────────────────────────────────────────┘
```

---
<img width="1457" height="927" alt="image" src="https://github.com/user-attachments/assets/e1a5dc78-1957-4abf-95a0-ed8d8824e161" />

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Installation

1. **Clone or Extract the Repository**

```bash
cd market_basket_recommender
```

2. **Create Virtual Environment** (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Verify Installation**

```bash
python recommender.py
```

Expected output:
```
Loaded X transactions with Y unique products
Generating frequent itemsets...
Found X frequent itemsets
Generating association rules...
Generated X association rules
Model training completed!
```

---

## 💻 Usage

### Option 1: Train Model and Run Web Application

```bash
# Train the model
python recommender.py

# Start the FastAPI server
python app.py
```

Then open your browser and navigate to: **http://localhost:8000**

### Option 2: Using Uvicorn (Production)

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### Using the Web Interface

1. **Browse Products**: View all available electronic products in the left panel
2. **Add to Cart**: Click "Add Item" to add products to your cart
3. **View Recommendations**: Recommendations appear automatically in the right panel
4. **Add Recommended Items**: Click on recommendations to add them to cart
5. **Remove Items**: Click "Remove" to remove items from cart
6. **Dynamic Updates**: Recommendations update with each cart change

---

## 📚 API Documentation

### Interactive API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### 1. Get All Products

```http
GET /api/products
```

**Response:**
```json
{
  "products": [
    {
      "sku": "0806-001",
      "product_name": "Axis M3046-V Network Camera"
    },
    ...
  ]
}
```

#### 2. Get Recommendations

```http
POST /api/recommendations
Content-Type: application/json

{
  "cart_items": ["D7050", "PG9914"],
  "top_n": 5
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "sku": "HS2016NK",
      "product_name": "DSC PowerSeries Neo Alarm Kit",
      "confidence": 0.75,
      "lift": 2.5,
      "support": 0.12
    },
    ...
  ],
  "cart_size": 2
}
```

#### 3. Get Product by SKU

```http
GET /api/product/{sku}
```

**Example:**
```http
GET /api/product/D7050
```

**Response:**
```json
{
  "sku": "D7050",
  "product_name": "Bosch D7050 Detector"
}
```

#### 4. Health Check

```http
GET /health
```

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true,
  "total_products": 21
}
```

---

## 🧮 Algorithm Details

### Apriori Algorithm

The system uses the **Apriori Algorithm** for mining frequent itemsets and generating association rules.

#### Key Metrics

1. **Support**: Frequency of itemset occurrence
   ```
   Support(A) = (Transactions containing A) / (Total Transactions)
   ```

2. **Confidence**: Conditional probability
   ```
   Confidence(A → B) = Support(A ∪ B) / Support(A)
   ```

3. **Lift**: Measure of rule strength
   ```
   Lift(A → B) = Confidence(A → B) / Support(B)
   ```

#### Default Thresholds

- **Minimum Support**: 0.05 (5% of transactions)
- **Minimum Confidence**: 0.30 (30% probability)
- **Minimum Lift**: 1.0 (positive correlation)

#### Algorithm Steps

1. **Data Preprocessing**
   - Load transaction data from CSV
   - Group items by transaction ID
   - Create transaction encoder

2. **Frequent Itemset Generation**
   - Apply Apriori algorithm with min_support
   - Generate frequent itemsets of all sizes

3. **Association Rule Mining**
   - Generate rules from frequent itemsets
   - Filter by confidence threshold
   - Filter by lift threshold

4. **Recommendation Generation**
   - Match cart items to rule antecedents
   - Extract consequents not in cart
   - Rank by confidence and lift
   - Return top N recommendations

---

## 📁 Project Structure

```
market_basket_recommender/
│
├── app.py                      # FastAPI application
├── recommender.py              # Recommendation engine core
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── data/
│   └── transactions.csv        # Historical transaction data
│
├── models/
│   └── recommender_model.pkl   # Trained model (generated)
│
├── templates/
│   └── index.html             # Web interface
│
└── tests/
    └── test_recommender.py    # Unit tests (optional)
```

### File Descriptions

- **app.py**: FastAPI web application with API endpoints
- **recommender.py**: Core recommendation engine using Apriori algorithm
- **transactions.csv**: Sample transaction dataset with SKUs and product names
- **index.html**: Interactive web interface for the checkout system
- **requirements.txt**: All Python package dependencies
- **recommender_model.pkl**: Serialized trained model for quick loading

---

## 🖼️ Screenshots

### Main Interface
- Clean, professional design with SJSU branding
- Product list on left, cart and recommendations on right
- Real-time cart count indicator

### Recommendation Display
- Recommendations shown with confidence scores
- Clickable recommendations for easy addition
- Visual indicators for high-confidence suggestions

---

## 🧪 Testing

### Manual Testing Scenarios

#### Test Case 1: Single Item in Cart
```
Cart: [Bosch D7050 Detector]
Expected: Recommendations based on items frequently bought with D7050
```

#### Test Case 2: Multiple Items in Cart
```
Cart: [Bosch D7050 Detector, DSC PG9914 Motion Detector]
Expected: Refined recommendations based on both items
```

#### Test Case 3: Unprecedented Combination
```
Cart: [Items that never appear together in training data]
Expected: No recommendations displayed (graceful handling)
```

#### Test Case 4: Remove Items
```
Action: Remove item from cart
Expected: Recommendations update to reflect new cart state
```

### API Testing with cURL

```bash
# Test health endpoint
curl http://localhost:8000/health

# Test get products
curl http://localhost:8000/api/products

# Test recommendations
curl -X POST http://localhost:8000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{"cart_items": ["D7050"], "top_n": 5}'
```

---

## 🔮 Future Enhancements

### Short-term Improvements
- [ ] User authentication and personalized recommendations
- [ ] Product images and detailed descriptions
- [ ] Shopping cart persistence (database)
- [ ] Product search and filtering
- [ ] Mobile-responsive design improvements

### Medium-term Enhancements
- [ ] Collaborative filtering integration
- [ ] A/B testing framework
- [ ] Analytics dashboard
- [ ] Inventory integration
- [ ] Price optimization

### Long-term Vision
- [ ] Deep learning recommendation models
- [ ] Multi-channel recommendation (web, mobile app, email)
- [ ] Real-time model retraining pipeline
- [ ] Explainable AI for recommendations
- [ ] Integration with CRM systems

---

## 🎓 Academic Context

### Course Information
- **Course**: CMPE 256 - Recommender Systems
- **University**: San José State University
- **Semester**: Fall 2025
- **Instructor**: Professor Chandrasekar Vuppalapati

### Learning Outcomes Demonstrated

1. ✅ **Association Rule Mining**: Practical implementation of Apriori algorithm
2. ✅ **Recommendation Systems**: End-to-end system design and deployment
3. ✅ **Data Science Pipeline**: From raw data to production-ready application
4. ✅ **API Development**: RESTful microservice architecture
5. ✅ **Web Development**: Interactive user interface design

---

## 📊 Dataset Information

The transaction dataset, electronic product names, SKU identifiers, and business names represent **synthetic data** derived using advanced language-model-based data generation techniques.

Any resemblance to real transaction data, consumers, or Business-to-Business activities is purely coincidental and bears no predictive or analytical relevance to real-world entities or events.

This dataset was prepared exclusively for academic use in the San José State University Fall 2025 CMPE 256 – Recommender Systems course.

**All rights and restrictions apply.**

---

## 🤝 Contributors

This project was developed as part of the CMPE 256 Data Science Hackathon (November 01-02, 2025).

---

## 📄 License

This project is developed for academic purposes as part of CMPE 256 coursework at San José State University. All rights reserved.

---

## 📞 Support

For questions or issues related to this project, please contact:
- **Professor**: Chandrasekar Vuppalapati
- **Team Members**: Parth Maradia(019104527), Kalhar Patel(019140511), Abhishek Darji(019113471)

---

## 🙏 Acknowledgments

- Professor Chandrasekar Vuppalapati for project guidance
- San José State University CMPE Department
- mlxtend library for Apriori implementation
- FastAPI framework for excellent API development tools

---

**Made with ❤️ for SJSU CMPE 256**
