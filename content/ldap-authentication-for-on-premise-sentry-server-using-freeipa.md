---
Title: LDAP Authentication for On-premise Sentry Server using freeIPA
Date: 2017-12-11 23:27
Author: Huahai
Category: notebook
Tags: SysAdmin, Sentry, LDAP, FreeIPA 
Slug: ldap-authentication-for-on-premise-sentry-server-using-freeipa
Alias: /blog/2017/12/ldap-authentication-premise-sentry-server-using-freeipa
Lang: en
---

Sentry is a fairly popular service for tracking exceptions and errors in production softwares. They also provides a [docker recipe](https://github.com/getsentry/onpremise) for people who want to self host their own sentry server. This post shows how to enable LDAP authentication for such a self hosted sentry server, using freeIPA as the LDAP provider.

In addition to follow their instructions to install sentry, the following changes need to be made to add the capability to authenticate to sentry using freeIPA as the account source:

1\. Change the Dockerfile to install some dependencies:

    FROM sentry:8.22-onbuild

    RUN apt-get update && apt-get install -y libsasl2-dev python-dev libldap2-dev libssl-dev
    RUN pip install sentry-ldap-auth

2\. Add the following code at the end of <span style="color:#e74c3c;">sentry.conf.py</span>

    #############
    # LDAP auth #
    #############

    import ldap
    from django_auth_ldap.config import LDAPSearch, GroupOfUniqueNamesType

    AUTH_LDAP_SERVER_URI = 'ldap://ipa.example.com'
    AUTH_LDAP_BIND_DN = 'uid=jenkins,cn=sysaccounts,cn=etc,dc=example,dc=com'
    AUTH_LDAP_BIND_PASSWORD = 'secret'

    AUTH_LDAP_USER_SEARCH = LDAPSearch(
        'cn=users,cn=accounts,dc=example,dc=com',
        ldap.SCOPE_SUBTREE,
        '(uid=%(user)s)',
    )

    AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
        '',
        ldap.SCOPE_SUBTREE,
        '(objectClass=groupOfUniqueNames)'
    )

    AUTH_LDAP_GROUP_TYPE = GroupOfUniqueNamesType()
    AUTH_LDAP_REQUIRE_GROUP = None
    AUTH_LDAP_DENY_GROUP = None

    AUTH_LDAP_USER_ATTR_MAP = {
        'name': 'cn',
        'email': 'mail'
    }

    AUTH_LDAP_FIND_GROUP_PERMS = False
    AUTH_LDAP_CACHE_GROUPS = True
    AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600

    AUTH_LDAP_DEFAULT_SENTRY_ORGANIZATION = u'Sentry'
    AUTH_LDAP_SENTRY_ORGANIZATION_ROLE_TYPE = 'member'
    AUTH_LDAP_SENTRY_ORGANIZATION_GLOBAL_ACCESS = True
    AUTH_LDAP_SENTRY_SUBSCRIBE_BY_DEFAULT = False

    SENTRY_MANAGED_USER_FIELDS = ('email', 'first_name', 'last_name', 'password', )

    AUTHENTICATION_BACKENDS = AUTHENTICATION_BACKENDS + (
        'sentry_ldap_auth.backend.SentryLdapBackend',
    )

    # optional, for debugging
    import logging
    logger = logging.getLogger('django_auth_ldap')
    logger.addHandler(logging.StreamHandler())
    logger.addHandler(logging.FileHandler('/tmp/ldap2.log'))
    logger.setLevel('DEBUG')

    LOGGING['overridable'] = ['sentry', 'django_auth_ldap']
    LOGGING['loggers']['django_auth_ldap'] = {
        'handlers': ['console'],
        'level': 'DEBUG'
    }

                                                                                                                                                      

Some notes:

-   We are re-using a freeIPA system account that was created for read-only access ([originally for Jenkins](https://yyhh.org/blog/2017/12/configure-jenkins-use-freeipa-ldap-security-realm)).
-   freeIPA use a flat structure for users:  '<span style="color:#e74c3c;">cn=users,cn=accounts,dc=example,dc=com</span>'
-   <span style="color:#e74c3c;">AUTH\_LDAP\_DEFAULT\_SENTRY\_ORGANIZATION</span> must be an exact (case sensitive) match with the organization full name, otherwise the logged in user will not have access to anything. The default organization name is "Sentry", but it can be changed in the UI.
-   Those logging statements are useful for testing and debugging 
