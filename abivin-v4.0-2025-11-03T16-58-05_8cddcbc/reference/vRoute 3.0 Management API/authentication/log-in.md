---
title: Log In
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: noindex
next:
  description: ''
---
# Request Body

```json
{
    "username": "...",
    "password": "..."
}
```

# Response Body

## Successful Authentication

HTTP 200, with JSON response body in which '**token**' is the JWT token to be set in cookie '**jwtToken**' in next API requests:

```json
{
    "_id" : <hash>,
    "displayName" : <full-name>,
    "masterId" : <hash>,
    "__v" : 0,
    "coupled" : [
    ],
    "useType" : ,
    "linkAccounts" : [
    ],
    "subscriptionExpiry" : <iso-date>,
    "subscriptionCode" : <string>,
    "secret" : ,
    "stopTime" : ,
    "startTime" : ,
    "callPass" : ,
    "callId" : ,
    "globalConfig" : {
        "notification" : <string>
    },
    "timeFormat" : <number>,
    "phoneNumber" : <string>,
    "isDeleted" : <bool>,
    "profilePicture" : ,
    "description" : ,
    "occupation" : ,
    "createdAt" : <iso-date>,
    "isActive" : <bool>,
    "additionalSocialData" : ,
    "socialData" : [
    ],
    "socialNetwork" : ,
    "plivo_phone_number" : ,
    "plivo_endpoint_id" : ,
    "plivo_CallUUID" : ,
    "plivo_pwd" : ,
    "plivo_status" : <number>,
    "plivo_updated_username" : ,
    "plivo_username" : ,
    "support_agent" : <bool>,
    "email" : <email-address>,
    "lastName" : <string>,
    "firstName" : <string>,
    "roleIds" : [
        <hashes>
    ],
    "organizationIds" : [
        <hashes>
    ],
    "username" : <string>
}
```

## Failed Authentication

HTTP 4xx, with string message.
