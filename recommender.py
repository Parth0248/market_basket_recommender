import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
import pickle
import os
from typing import List, Dict, Set, Tuple
import numpy as np


class MarketBasketRecommender:
    """
    Market Basket Recommendation System using Association Rule Mining (Apriori Algorithm)
    """
    
    def __init__(self, min_support=0.05, min_confidence=0.3, min_lift=1.0):
        """
        Initialize the recommender system
        
        Args:
            min_support: Minimum support threshold for frequent itemsets
            min_confidence: Minimum confidence threshold for association rules
            min_lift: Minimum lift threshold for association rules
        """
        self.min_support = min_support
        self.min_confidence = min_confidence
        self.min_lift = min_lift
        self.rules = None
        self.products = None
        self.transactions = None
        
    def load_data(self, csv_path: str):
        """
        Load transaction data from CSV file
        
        Args:
            csv_path: Path to the transactions CSV file
        """
        df = pd.read_csv(csv_path)
        
        # Group by TransactionID to create basket format
        self.transactions = df.groupby('TransactionID')['SKU'].apply(list).values.tolist()
        self.products = df[['ProductName', 'SKU']].drop_duplicates()
        
        print(f"Loaded {len(self.transactions)} transactions with {len(self.products)} unique products")
        
    def train(self):
        """
        Train the recommendation model using Apriori algorithm
        """
        if self.transactions is None:
            raise ValueError("Please load data first using load_data()")
        
        # Create transaction encoder
        te = TransactionEncoder()
        te_ary = te.fit(self.transactions).transform(self.transactions)
        df_encoded = pd.DataFrame(te_ary, columns=te.columns_)
        
        # Apply Apriori algorithm
        print("Generating frequent itemsets...")
        frequent_itemsets = apriori(df_encoded, min_support=self.min_support, use_colnames=True)
        
        if len(frequent_itemsets) == 0:
            print(f"Warning: No frequent itemsets found with min_support={self.min_support}")
            print("Trying with lower support threshold...")
            self.min_support = 0.02
            frequent_itemsets = apriori(df_encoded, min_support=self.min_support, use_colnames=True)
        
        print(f"Found {len(frequent_itemsets)} frequent itemsets")
        
        # Generate association rules
        print("Generating association rules...")
        self.rules = association_rules(
            frequent_itemsets, 
            metric="confidence", 
            min_threshold=self.min_confidence
        )
        
        # Filter by lift
        self.rules = self.rules[self.rules['lift'] >= self.min_lift]
        
        # Sort by confidence and lift
        self.rules = self.rules.sort_values(['confidence', 'lift'], ascending=False)
        
        print(f"Generated {len(self.rules)} association rules")
        print(f"Model training completed!")
        
    def get_recommendations(self, cart_items: List[str], top_n: int = 5) -> List[Dict]:
        """
        Get product recommendations based on current cart items
        
        Args:
            cart_items: List of SKUs currently in the cart
            top_n: Number of recommendations to return
            
        Returns:
            List of recommended products with confidence and lift scores
        """
        if self.rules is None or len(self.rules) == 0:
            return []
        
        if not cart_items:
            return []
        
        cart_set = set(cart_items)
        recommendations = {}
        
        # Find rules where antecedents match current cart items
        for idx, rule in self.rules.iterrows():
            antecedents = set(rule['antecedents'])
            consequents = set(rule['consequents'])
            
            # Check if all antecedents are in the cart
            if antecedents.issubset(cart_set):
                # Recommend items not already in cart
                for item in consequents:
                    if item not in cart_set:
                        if item not in recommendations:
                            recommendations[item] = {
                                'sku': item,
                                'confidence': rule['confidence'],
                                'lift': rule['lift'],
                                'support': rule['support']
                            }
                        else:
                            # Keep the rule with higher confidence
                            if rule['confidence'] > recommendations[item]['confidence']:
                                recommendations[item] = {
                                    'sku': item,
                                    'confidence': rule['confidence'],
                                    'lift': rule['lift'],
                                    'support': rule['support']
                                }
        
        # Sort by confidence and lift
        sorted_recommendations = sorted(
            recommendations.values(),
            key=lambda x: (x['confidence'], x['lift']),
            reverse=True
        )
        
        # Add product names
        result = []
        for rec in sorted_recommendations[:top_n]:
            product_info = self.products[self.products['SKU'] == rec['sku']]
            if not product_info.empty:
                result.append({
                    'sku': rec['sku'],
                    'product_name': product_info.iloc[0]['ProductName'],
                    'confidence': float(rec['confidence']),
                    'lift': float(rec['lift']),
                    'support': float(rec['support'])
                })
        
        return result
    
    def save_model(self, filepath: str):
        """Save the trained model to disk"""
        model_data = {
            'rules': self.rules,
            'products': self.products,
            'min_support': self.min_support,
            'min_confidence': self.min_confidence,
            'min_lift': self.min_lift
        }
        with open(filepath, 'wb') as f:
            pickle.dump(model_data, f)
        print(f"Model saved to {filepath}")
    
    def load_model(self, filepath: str):
        """Load a trained model from disk"""
        with open(filepath, 'rb') as f:
            model_data = pickle.load(f)
        
        self.rules = model_data['rules']
        self.products = model_data['products']
        self.min_support = model_data['min_support']
        self.min_confidence = model_data['min_confidence']
        self.min_lift = model_data['min_lift']
        print(f"Model loaded from {filepath}")
        
    def get_all_products(self) -> List[Dict]:
        """Get list of all available products"""
        if self.products is None:
            return []
        
        return [
            {'sku': row['SKU'], 'product_name': row['ProductName']}
            for _, row in self.products.iterrows()
        ]
    
    def get_product_by_sku(self, sku: str) -> Dict:
        """Get product information by SKU"""
        if self.products is None:
            return None
        
        product = self.products[self.products['SKU'] == sku]
        if not product.empty:
            return {
                'sku': product.iloc[0]['SKU'],
                'product_name': product.iloc[0]['ProductName']
            }
        return None


if __name__ == "__main__":
    # Initialize and train the model
    recommender = MarketBasketRecommender(
        min_support=0.05,
        min_confidence=0.3,
        min_lift=1.0
    )
    
    # Load data
    data_path = "data/transactions.csv"
    if os.path.exists(data_path):
        recommender.load_data(data_path)
        
        # Train the model
        recommender.train()
        
        # Save the model
        os.makedirs("models", exist_ok=True)
        recommender.save_model("models/recommender_model.pkl")
        
        # Test recommendations
        print("\n" + "="*50)
        print("Testing Recommendations")
        print("="*50)
        
        test_cart = ["D7050"]
        print(f"\nCart items: {test_cart}")
        recommendations = recommender.get_recommendations(test_cart, top_n=5)
        print("\nRecommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['product_name']} (SKU: {rec['sku']})")
            print(f"   Confidence: {rec['confidence']:.2%}, Lift: {rec['lift']:.2f}")
        
        test_cart = ["D7050", "PG9914"]
        print(f"\n\nCart items: {test_cart}")
        recommendations = recommender.get_recommendations(test_cart, top_n=5)
        print("\nRecommendations:")
        for i, rec in enumerate(recommendations, 1):
            print(f"{i}. {rec['product_name']} (SKU: {rec['sku']})")
            print(f"   Confidence: {rec['confidence']:.2%}, Lift: {rec['lift']:.2f}")
    else:
        print(f"Error: Data file not found at {data_path}")
