from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
import os
from recommender import MarketBasketRecommender

app = FastAPI(
    title="Electronic Retailer Market Basket Recommendation System",
    description="Real-time product recommendations for online checkout",
    version="1.0.0"
)

# Initialize templates
templates = Jinja2Templates(directory="templates")

# Initialize recommender
recommender = MarketBasketRecommender()

# Load the trained model
MODEL_PATH = "models/recommender_model.pkl"
if os.path.exists(MODEL_PATH):
    recommender.load_model(MODEL_PATH)
    print("✓ Model loaded successfully")
else:
    print("⚠ Model not found. Training new model...")
    recommender.load_data("data/transactions.csv")
    recommender.train()
    os.makedirs("models", exist_ok=True)
    recommender.save_model(MODEL_PATH)
    print("✓ Model trained and saved")


# Pydantic models for API
class CartRequest(BaseModel):
    cart_items: List[str]
    top_n: Optional[int] = 5


class RecommendationResponse(BaseModel):
    recommendations: List[dict]
    cart_size: int


class ProductResponse(BaseModel):
    products: List[dict]


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main web interface"""
    products = recommender.get_all_products()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "products": products}
    )


@app.get("/api/products", response_model=ProductResponse)
async def get_products():
    """Get all available products"""
    products = recommender.get_all_products()
    return ProductResponse(products=products)


@app.post("/api/recommendations", response_model=RecommendationResponse)
async def get_recommendations(cart_request: CartRequest):
    """
    Get product recommendations based on current cart
    
    Args:
        cart_request: Contains list of SKUs in cart and number of recommendations
        
    Returns:
        List of recommended products with confidence scores
    """
    try:
        recommendations = recommender.get_recommendations(
            cart_request.cart_items,
            cart_request.top_n
        )
        
        return RecommendationResponse(
            recommendations=recommendations,
            cart_size=len(cart_request.cart_items)
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/product/{sku}")
async def get_product(sku: str):
    """Get product information by SKU"""
    product = recommender.get_product_by_sku(sku)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_loaded": recommender.rules is not None,
        "total_products": len(recommender.get_all_products())
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
