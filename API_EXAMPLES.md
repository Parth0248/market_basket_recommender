# API Usage Examples

## Python Examples

### Example 1: Get All Products

```python
import requests

response = requests.get("http://localhost:8000/api/products")
products = response.json()

print(f"Total Products: {len(products['products'])}")
for product in products['products'][:5]:
    print(f"- {product['product_name']} (SKU: {product['sku']})")
```

### Example 2: Get Recommendations

```python
import requests

# Cart with two items
cart_data = {
    "cart_items": ["D7050", "PG9914"],
    "top_n": 5
}

response = requests.post(
    "http://localhost:8000/api/recommendations",
    json=cart_data
)

recommendations = response.json()

print(f"Cart Size: {recommendations['cart_size']}")
print(f"Recommendations: {len(recommendations['recommendations'])}")

for rec in recommendations['recommendations']:
    print(f"\n{rec['product_name']}")
    print(f"  Confidence: {rec['confidence']:.1%}")
    print(f"  Lift: {rec['lift']:.2f}")
```

### Example 3: Get Product by SKU

```python
import requests

sku = "D7050"
response = requests.get(f"http://localhost:8000/api/product/{sku}")
product = response.json()

print(f"Product: {product['product_name']}")
print(f"SKU: {product['sku']}")
```

---

## cURL Examples

### Get All Products

```bash
curl http://localhost:8000/api/products
```

### Get Recommendations

```bash
curl -X POST http://localhost:8000/api/recommendations \
  -H "Content-Type: application/json" \
  -d '{
    "cart_items": ["D7050", "PG9914"],
    "top_n": 5
  }'
```

### Get Product by SKU

```bash
curl http://localhost:8000/api/product/D7050
```

### Health Check

```bash
curl http://localhost:8000/health
```

---

## JavaScript/Fetch Examples

### Get Recommendations

```javascript
async function getRecommendations(cartItems) {
    const response = await fetch('http://localhost:8000/api/recommendations', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            cart_items: cartItems,
            top_n: 5
        })
    });
    
    const data = await response.json();
    return data;
}

// Usage
const recommendations = await getRecommendations(['D7050', 'PG9914']);
console.log(recommendations);
```

### Get All Products

```javascript
async function getAllProducts() {
    const response = await fetch('http://localhost:8000/api/products');
    const data = await response.json();
    return data.products;
}

// Usage
const products = await getAllProducts();
console.log(`Total products: ${products.length}`);
```

---

## Advanced Usage: Programmatic Model Training

```python
from recommender import MarketBasketRecommender

# Initialize recommender with custom parameters
recommender = MarketBasketRecommender(
    min_support=0.03,      # Lower threshold for more rules
    min_confidence=0.25,   # Slightly lower confidence
    min_lift=1.2          # Higher lift requirement
)

# Load and train
recommender.load_data("data/transactions.csv")
recommender.train()

# Get recommendations
cart = ["D7050", "PG9914"]
recommendations = recommender.get_recommendations(cart, top_n=5)

for rec in recommendations:
    print(f"{rec['product_name']}: {rec['confidence']:.1%} confidence")

# Save model
recommender.save_model("models/custom_model.pkl")
```

---

## Integration Example: E-commerce Platform

```python
from fastapi import FastAPI
from recommender import MarketBasketRecommender

app = FastAPI()
recommender = MarketBasketRecommender()
recommender.load_model("models/recommender_model.pkl")

@app.post("/checkout/recommendations")
async def checkout_recommendations(user_id: str, cart_items: list):
    """
    Get recommendations for a specific user's cart
    """
    recommendations = recommender.get_recommendations(cart_items, top_n=3)
    
    # Log for analytics
    log_recommendations(user_id, cart_items, recommendations)
    
    return {
        "user_id": user_id,
        "recommendations": recommendations,
        "timestamp": datetime.now()
    }
```

---

## Testing with pytest

```python
import pytest
from recommender import MarketBasketRecommender

def test_recommendations():
    recommender = MarketBasketRecommender()
    recommender.load_model("models/recommender_model.pkl")
    
    cart = ["D7050"]
    recommendations = recommender.get_recommendations(cart, top_n=5)
    
    assert len(recommendations) > 0
    assert all('sku' in rec for rec in recommendations)
    assert all('confidence' in rec for rec in recommendations)

def test_empty_cart():
    recommender = MarketBasketRecommender()
    recommender.load_model("models/recommender_model.pkl")
    
    recommendations = recommender.get_recommendations([], top_n=5)
    assert len(recommendations) == 0
```

---

## Performance Monitoring

```python
import time
from recommender import MarketBasketRecommender

recommender = MarketBasketRecommender()
recommender.load_model("models/recommender_model.pkl")

# Benchmark recommendation speed
test_carts = [
    ["D7050"],
    ["D7050", "PG9914"],
    ["D7050", "PG9914", "HS2016NK"]
]

for cart in test_carts:
    start = time.time()
    recommendations = recommender.get_recommendations(cart, top_n=5)
    duration = time.time() - start
    
    print(f"Cart size {len(cart)}: {duration*1000:.2f}ms")
    print(f"  Recommendations: {len(recommendations)}")
```

---

## Error Handling

```python
import requests
from requests.exceptions import RequestException

def get_recommendations_safe(cart_items):
    try:
        response = requests.post(
            "http://localhost:8000/api/recommendations",
            json={"cart_items": cart_items, "top_n": 5},
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except RequestException as e:
        print(f"Error getting recommendations: {e}")
        return {"recommendations": [], "cart_size": len(cart_items)}

# Usage
recommendations = get_recommendations_safe(["D7050", "PG9914"])
```
