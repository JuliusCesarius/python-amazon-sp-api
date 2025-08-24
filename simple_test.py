#!/usr/bin/env python3

import os
import requests
import json

def test_sandbox_connection():
    """Test connection to Amazon SP API sandbox environment"""
    
    print("🔍 Testing Amazon SP API Sandbox Connection...")
    print("=" * 50)
    
    # Set sandbox environment
    os.environ['AWS_ENV'] = 'SANDBOX'
    
    # Check environment variables
    print("📋 Environment Variables:")
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
    
    # Test direct LWA token exchange
    print("\n🔄 Testing LWA Token Exchange...")
    
    try:
        # LWA token endpoint
        token_url = "https://api.amazon.com/auth/o2/token"
        
        # Prepare the request data
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': lwa_app_id,
            'client_secret': lwa_client_secret
        }
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        print("   🔄 Sending token request...")
        response = requests.post(token_url, data=data, headers=headers)
        
        print(f"   📊 Response Status: {response.status_code}")
        print(f"   📊 Response Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            token_data = response.json()
            print(f"   ✅ Token exchange successful!")
            print(f"   📊 Token type: {token_data.get('token_type')}")
            print(f"   📊 Expires in: {token_data.get('expires_in')} seconds")
            return True
        else:
            print(f"   ❌ Token exchange failed!")
            print(f"   📊 Error response: {response.text}")
            return False
            
    except Exception as e:
        print(f"   ❌ Error during token exchange: {e}")
        return False

if __name__ == "__main__":
    success = test_sandbox_connection()
    if success:
        print("\n🎉 Sandbox connection test completed successfully!")
    else:
        print("\n💥 Sandbox connection test failed!")
