---
Status: published
Lang: en
Title: How to Setup SAML2 Authentication on Sentry with Keycloak
Date: 2020-10-19T18:28:25.187Z
Author: Huahai
Category: notebook
Tags: SAML, Sentry, Keycloak
---
With newer versions of on-premise Sentry (I am using Sentry 20.10.1), the [LDAP authentication](https://yyhh.org/blog/2017/12/ldap-authentication-for-on-premise-sentry-server-using-freeipa/) does not seem to work any more. The code still compiles but the LDAP login UI does not show up. Fortunately, newer versions of Sentry provide built-in support for SAML2 authentication, so we can use that instead. We can do this because our LDAP service is connected with an identity provider, in our case, a Keycloak server. 

It took a bit of fiddlings in the UI of these two applications to set things up correctly. Here's how.

# Keycloak Setup

The first step is to register Sentry with IdP, i.e. the Keycloak server. I am using Keycloak 3.4.3.Final community. 

1. Create a client

Click "Clients" > "Create". 

For the required "Client ID" field, just type something like `https://sentry.example.com/saml/metadata/example/`, assuming the sentry server is at `sentry.example.com`, and the organization slug in sentry is `example`.

Choose `saml` for "Client Protocol".

Click "Save".

2. Configure the client

* "Sign Assertions" => `OFF`
* "Encrypt Assertions" => `OFF`
* "Client Signature Required" => `OFF`
* "Force POST Binding" => `ON`
* "Force Name ID Format" => `OFF`
* "Name ID Format" => `email`
* "Valid Redirect URIs" => `*`
* "Assertion Consumer Service POST Binding URL" => `https://sentry.example.com/saml/acs/example/` 
* "Logout Service POST Binding URL" => `https://sentry.example.com/saml/sls/example/`

Leave the rest as they are.

3. Configure Mappers

Click "Delete" on  the default "role list", and confirm, as we will use a builtin mapper.

Click "Add Builtin", check "X500 email", and click "Add selected". 

Click "X500 Email", and change "SAML Attribute Name" to `user_email`, as that's what Sentry expects. Click Save.

We are done with Keycloak setup, now let's setup Sentry side.

# Sentry Setup

The [instruction](https://docs.sentry.io/product/accounts/sso/saml2/) on registering IdP with Sentry is pretty good. 

The first method of "Using Metadata URL" works with Keycloak. 

For "Meta URL", use `https://idp.example.com/auth/realms/example.com/protocol/saml/descriptor`, assuming the keycloak server is on `idp.example.com`, and the realm name in there is `example.com`.

For Attribute Mappings, use `user_email` for both "IdP User ID" and "User Email" required fields. 

If everything setup correctly, after you are directed to your keycloak server to login, you should be directed back to Sentry with two green notifications on top, success!



