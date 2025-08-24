#!/usr/bin/env python3

import os
from datetime import datetime, timedelta
from sp_api.api import Orders, Sellers
from sp_api.base import SellingApiException

def test_sandbox_connection():
    """Test connection to Amazon SP API sandbox environment"""
    
    print("🔍 Testing Amazon SP API Sandbox Connection...")
    print("=" * 50)
    
    # Set sandbox environment
    os.environ['AWS_ENV'] = 'SANDBOX'
    
    # Check if environment variables are set
    print("📋 Checking environment variables:")
    lwa_app_id = os.environ.get('LWA_APP_ID')
    lwa_client_secret = os.environ.get('LWA_CLIENT_SECRET')
    refresh_token = os.environ.get('SP_API_REFRESH_TOKEN')
    aws_env = os.environ.get('AWS_ENV')
    
    print(f"   LWA_APP_ID: {'✅ Set' if lwa_app_id else '❌ Not set'}")
    print(f"   LWA_CLIENT_SECRET: {'✅ Set' if lwa_client_secret else '❌ Not set'}")
    print(f"   SP_API_REFRESH_TOKEN: {'✅ Set' if refresh_token else '❌ Not set'}")
    print(f"   AWS_ENV: {aws_env}")
    
    if not all([lwa_app_id, lwa_client_secret, refresh_token]):
        print("\n❌ Missing required environment variables!")
        return False
    
    print("\n🚀 Testing API connections...")
    
    # Test 1: Sellers API (usually available in sandbox)
    try:
        print("\n1️⃣ Testing Sellers API...")
        sellers = Sellers()
        response = sellers.get_marketplace_participation()
        print(f"   ✅ Sellers API: Success! Response received")
        print(f"   📊 Response: {response.payload}")
        return True
    except SellingApiException as e:
        print(f"   ❌ Sellers API Error: {e}")
    except Exception as e:
        print(f"   ❌ Sellers API Unexpected Error: {e}")
    
    # Test 2: Orders API
    try:
        print("\n2️⃣ Testing Orders API...")
        orders = Orders()
        # Use a date range that should work in sandbox
        test_date = (datetime.utcnow() - timedelta(days=30)).isoformat()
        response = orders.get_orders(CreatedAfter=test_date)
        print(f"   ✅ Orders API: Success! Response received")
        return True
    except SellingApiException as e:
        print(f"   ❌ Orders API Error: {e}")
    except Exception as e:
        print(f"   ❌ Orders API Unexpected Error: {e}")
    
    print("\n❌ All API tests failed. Please check your credentials and sandbox access.")
    return False

if __name__ == "__main__":
    success = test_sandbox_connection()
    if success:
        print("\n🎉 Sandbox connection test completed successfully!")
    else:
        print("\n💥 Sandbox connection test failed!")
