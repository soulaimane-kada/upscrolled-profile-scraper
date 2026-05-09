# UpScrolled Profile Scraper

UpScrolled Profile Scraper is a tool that extracts all profile information. Extract all profile data + metadata

The UpScrolled Profile Scraper allows you to scrape profiles from the UpScrolled app. when a link to an UpScrolled profile is provided.

This unofficial UpScrolled API is designed to let you scrape profiles easily and retrieve metadata with no limits and no login required. Use it to do what ever you want

## Features

- **Profile Data** → Extract all profile data
- **Profile Stats** → Extract profile stats
- **Profile Metadata** → Extract all profile metadata

## How to Use This API

### Input Parameters

The input for this scraper should be a JSON object containing the URL of the target profile you want to scrape. Check the input tab for a detailed list of parameters.

```json
{
  "url": "https://share.upscrolled.com/en/user/c1466cfc-ff89-48c5-88f2-6247b39596c0"
}
```

## UpScrolled Output Format

After a successful request, the API will return the profile data.

### Scraped UpScrolled Profile
```json
{
  "success": true,
  "results": {
    "name": "Issam Hijazi",
    "username": "@Issam",
    "profileImage": "https://d2sscsmkqn4j9v.cloudfront.net/c1466cfc-ff89-48c5-88f2-6247b39596c0/ProfileImage_1e1d56c7-0d33-41dc-9681-a4428e50f706.jpg",
    "stats": {
      "following": "180",
      "followers": "300046"
    },
    "description": "@Issam",
    "isVerified": true,
    "userId": "c1466cfc-ff89-48c5-88f2-6247b39596c0"
  }
}
```

### Your feedback
We’re always working on improving the performance of our Actors. So if you’ve got any technical feedback for upscrolled profile scraper or simply found a bug, please create an issue on the Actor’s Issues tab in Apify Console.

