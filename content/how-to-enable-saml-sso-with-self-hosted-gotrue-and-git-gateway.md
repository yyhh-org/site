---
Status: published
Lang: en
Title: How to enable SAML SSO with self-hosted gotrue and git-gateway
Date: 2020-04-03T06:18:46.579Z
Author: Huahai
Category: notebook
Tags: 'SAML, Keycloak, SSG, Netlify CMS, gotrue, SysAdmin'
---
Static Site Generator (SSG) is in vogue for building Web sites. Compared with traditional content management system (CMS), SSG is more performant, flexible and easier to maintain for people comfortable with coding . However, for the non-technical crowd, a WYSIWYG online editor is still the way to go. [Netlify CMS](https://www.netlifycms.org/) fills this need nicely by offering a user interface for SSG. This article details how to enable single sign-on (SSO) for Netlify CMS, so it can be used in a business environment, where marketers, copy writers or other non-coding editors can edit and publish content. 

Netlify's cloud platform offers SSO, and they also makes their software available in open source. Obviously, these open source software are not particularly well documented, so most people should be using their cloud offering. However, for some companies that are paranoid about privacy and business control, it is possible to host their own, for example, in order to utilize an existing corporate security infrastructure.  

In this guide, we are going to utilize three Netlify's open source components to achieve SSO for a SSG powered Web site: [gotrue](https://github.com/netlify/gotrue) is an identity service provider; [git-gateway](https://github.com/netlify/git-gateway) enables people to commit content in git without knowing about git; and [Netlify identity widget](https://github.com/netlify/netlify-identity-widget) provides the Web form for login. 

We will connect gotrue with an existing Identity Provider (IdP) over [SAML 2.0](https://en.wikipedia.org/wiki/SAML_2.0) protocols. In this case, an  installation of [Keycloak](https://www.keycloak.org/) will be our IdP.

#### Keycloak Setup

First, we need to create a new client for the service provider (SP) in Keycloak. In this case, SP is gotrue, which is an identity API server written in go. In the administrative console of Keycloak, create a client with the ID `https://example.com/.netlify/identity/saml`, which points to the API endpoint of gotrue. Replace `example.com` with your domain name.

In the settings, make sure to *uncheck* `Force POST Binding`. Otherwise, gotrue will throw an error:
 
> {"code":400,"msg":"Unsupported provider: No valid SSO service found in IDP metadata"}

Turns out that gotrue only supports HTTP-Redirect binding and does not support POST binding as of this writing. I find gotrue's design choice strange, as POST has much less uncertainty to deal with in a complex environment where a bunch of Web proxying and redirecting are going on. Most SAML SPs I dealt with use POST. Anyway, it is what it is. 

Correspondingly, set `Assertion Consumer Service Redirect Binding URL` instead of the POST one. The value should be `https://example.com/.netlify/identity/saml/acs`. 

On the other hand, Keycloak also has its own quirk. In its metadata API endpoint, namely `{root}/auth/realms/{realm}/protocol/saml/descriptor`, it returns an XML document that is not conforming to the SAML specification. A non-forgiving SP implementation will have a problem consuming the document, which is the case with gotrue. It will dump this error message:

>{"code":400,"msg":"Unsupported provider: Fetching metadata failed: expected element type \u003cEntityDescriptor\u003e but have \u003cEntitiesDescriptor\u003e"}

As you can see, Keycloak's XML has an unnecessary extra layer of tag `EntitiesDescriptor` around `EntityDescriptor`, which trips gotrue. Strangely, RedHat decided not to fix this. See [this issue](https://issues.redhat.com/browse/KEYCLOAK-4399) for a fun conversation.

So you will have to fix it yourself. What I did was to manually copy out the correct metadata, save it in a XML file and put it on some public facing Web server temporally for gotrue to fetch. The correct metadata can be obtained in the Keycloak UI, go to "Installation" tab, then select "SAML Metadata IDPSSODescriptor".

#### Gotrue and git-gateway Setup

There is an excellent guide on how to self-host gotrue and git-gateway at [https://github.com/hfte/netlify-cms-with-selfhosted-gotrue-and-git-gateway](https://github.com/hfte/netlify-cms-with-selfhosted-gotrue-and-git-gateway)

Follow that guide first, and make sure it works. It does email based login, useful for inviting external bloggers or editors to work on the site. For SAML based SSO that is suitable for employees, read on.

There is a bug in the current version of gotrue source code. You will have to patch it first. On line 130 in `api/provider/saml.go`, we will need to add a `NameIdFormat` field. Otherwise, gotrue will send `""` as the NameIdFormat, which cause Keycloak to error out with 

>"We are sorry... Unsupported NameIdFormat".

The fix should look like this:

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
                NameIdFormat:                "urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress",
                AllowMissingAttributes:      true,
        }
```
Here we set name id format to be email address, which apparently is the only format that gotrue works with. If you set the format as 'unspecified', users will be able to login, but they cannot edit anything, all the Netlify CMS UI controls will be greyed out. Obviously gotrue is checking that it gets an email address from the IdP.

After the patch, compile the code.

```
make deps
make build
```

Now the main configuration of gotrue is in a `.env` file in the root of the gotrue source code.

```bash
GOTRUE_JWT_SECRET="your-secret-key-shared-between-git-gateway-and-gotrue"
GOTRUE_JWT_EXP=3600
GOTRUE_JWT_AUD=localhost
GOTRUE_DB_DRIVER=mysql
GOTRUE_JWT_DEFAULT_GROUP_NAME=admin
DATABASE_URL="gotrue:mysqlpassword@tcp(mysqlipaddress:3306)/gotrue?parseTime=true&multiStatements=true"
GOTRUE_API_HOST=localhost
PORT=8081
GOTRUE_SITE_URL="https://example.com/"
GOTRUE_LOG_LEVEL=DEBUG
GOTRUE_OPERATOR_TOKEN=your-super-secret-operator-token
GOTRUE_DISABLE_SIGNUP=false
GOTRUE_MAILER_AUTOCONFIRM=true
GOTRUE_EXTERNAL_SAML_ENABLED=true
GOTRUE_EXTERNAL_SAML_METADATA_URL="https://idp.example.com/auth/realms/example.com/protocol/saml/descriptor"
GOTRUE_EXTERNAL_SAML_API_BASE="https://example.com/.netlify/identity/"
GOTRUE_EXTERNAL_SAML_NAME="Example SSO"
GOTRUE_EXTERNAL_SAML_SIGNING_CERT=''
GOTRUE_EXTERNAL_SAML_SIGNING_KEY=''
GOTRUE_EXTERNAL_LABELS="{SAML: Example SSO}"
```
The `GOTRUE_EXTERNAL_SAML_METADATA_URL` value should point to the corrected XML mentioned above.

Note, I set the default JWT group name to be "admin", because my IdP is backed by a LDAP server that handles user group membership and permisions already, there's no need to duplicate things here. Your case may be different.

Now the rest of gotrue and git-gateway setup is the same as the guide linked above.

#### Setup Netlify CMS

To add Netlify CMS to your site, follow [the instruction](https://www.netlifycms.org/docs/add-to-your-site/)

To get a nice login form with a SSO button for Netlify CMS, use netlify-identity-widget. This is done by adding some code in `/admin/index.html` of your SSG site. Mine looks like this, and it is a bit simpler than the guide linked above.

```html
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Content Manager</title>
  <script type="text/javascript" src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>
</head>
<body>
  <script>
    netlifyIdentity.init({
        APIUrl: "https://example.com/.netlify/identity"
    });
  </script>
  <script src="https://unpkg.com/netlify-cms@^2.0.0/dist/netlify-cms.js"></script>
  <div data-netlify-identity-button>Log in</div>
</body>
</html>
```
You may also want to add this line `<script type="text/javascript" src="https://identity.netlify.com/v1/netlify-identity-widget.js"></script>` into the `index.html` of your main site. As the email confirmation link is pointed there. 

Again, the rest of the setup should follow [https://github.com/hfte/netlify-cms-with-selfhosted-gotrue-and-git-gateway](https://github.com/hfte/netlify-cms-with-selfhosted-gotrue-and-git-gateway).

Now your company personnel can use their company SSO credential to login to your SSG site to edit and publish content. No need to create another set of user name and password just for the Web editing work. 


