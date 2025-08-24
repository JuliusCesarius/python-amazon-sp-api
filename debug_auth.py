#!/usr/bin/env python3

import os
from sp_api.auth import AccessTokenClient
from sp_api.base.credential_provider import CredentialProvider

def debug_authentication():
    """Debug authentication step by step"""
    
    print("🔍 Debugging Amazon SP API Authentication...")
    print("=" * 50)
    
    # Set sandbox environment
    os.environ['AWS_ENV'] = 'SANDBOX'
    
    # Check environment variables
    print("📋 Environment Variables:")
    print(f"   LWA_APP_ID: {os.environ.get('LWA_APP_ID', 'Not set')}")
    print(f"   LWA_CLIENT_SECRET: {os.environ.get('LWA_CLIENT_SECRET', 'Not set')[:20]}..." if os.environ.get('LWA_CLIENT_SECRET') else 'Not set')
    print(f"   SP_API_REFRESH_TOKEN: {os.environ.get('SP_API_REFRESH_TOKEN', 'Not set')[:20]}..." if os.environ.get('SP_API_REFRESH_TOKEN') else 'Not set')
    print(f"   AWS_ENV: {os.environ.get('AWS_ENV', 'Not set')}")
    
    try:
        print("\n🔑 Testing Credential Provider...")
        credentials = CredentialProvider().credentials
        print(f"   ✅ Credentials loaded successfully")
        print(f"   📊 LWA App ID: {credentials.lwa_app_id}")
        print(f"   📊 LWA Client Secret: {credentials.lwa_client_secret[:20]}...")
        print(f"   📊 Refresh Token: {credentials.refresh_token[:20]}...")
        
        print("\n🔄 Testing Access Token Client...")
        auth_client = AccessTokenClient(
            refresh_token=credentials.refresh_token,
            credentials=credentials
        )
        
        print("   🔄 Attempting to get access token...")
        access_token_response = auth_client.get_auth()
        print(f"   ✅ Access token obtained successfully!")
        print(f"   📊 Token type: {access_token_response.token_type}")
        print(f"   📊 Expires in: {access_token_response.expires_in} seconds")
        
        return True
        
    except Exception as e:
        print(f"   ❌ Error: {e}")
        print(f"   🔍 Error type: {type(e).__name__}")
        return False

if __name__ == "__main__":
    success = debug_authentication()
    if success:
        print("\n🎉 Authentication debug completed successfully!")
    else:
        print("\n💥 Authentication debug failed!")
