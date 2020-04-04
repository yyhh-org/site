---
Title: How to enable SAML SSO with self-hosted gotrue and git-gateway
Date: 2020-04-03T06:18:46.579Z
Author: Huahai
Category: notebook
Tags: 'SAML, keycloak, netlify cms, sysadmin'
Lang: en
Status: draft
---

Keycloak 3.4.3Final

> {"code":400,"msg":"Unsupported provider: Fetching metadata failed: expected element type \u003cEntityDescriptor\u003e but have \u003cEntitiesDescriptor\u003e"}

Here RedHat did not follow the spec.

https://issues.redhat.com/browse/KEYCLOAK-4399

`{root}/auth/realms/{realm}/protocol/saml/descriptor`

They decided not to fix the problem. So you have to manually copy out the correct metadata, save in a XML file and put it on some public server temporily for gotrue to fetch. The corret metadata can be obtained in the UI: "Installation" tab, then select "SAML Metadata IDPSSODescriptor"

> {"code":400,"msg":"Unsupported provider: No valid SSO service found in IDP metadata"}

Turned out gotrue implemention does not support HTTP-POST binding, like everyone else. They only supports HTTP-Redirect binding. So make sure to uncheck "Force POST binding" in KeyCloak, and re-do steps above to get a new XML file.

Also, set "Assertion Consumer Service Redirect Binding URL" to be "https://example.com/.netlify/identity/saml/acs"

On line 130 in `api/provider/saml.go`, and add `NameIdFormat`, otherwise, gotrue will send `""`, which cause keycloak to error out "We are sorry... Unsupported NameIdFormat".

```go
        sp := &saml2.SAMLServiceProvider{
                IdentityProviderSSOURL:      ssoService.Location,
                IdentityProviderIssuer:      meta.EntityID,
                AssertionConsumerServiceURL: baseURI.String() + "/saml/acs",
                ServiceProviderIssuer:       baseURI.String() + "/saml",
                SignAuthnRequests:           true,
                AudienceURI:                 baseURI.String() + "/saml",
                IDPCertificateStore:         &certStore,
                SPKeyStore:                  keyStore,
                NameIdFormat:                "urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified",
                AllowMissingAttributes:      true,
        }
```
