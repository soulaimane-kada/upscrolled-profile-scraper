from playwright.async_api import async_playwright
from apify import Actor
import asyncio, re, json


async def upscrolled_profile_scraper(url):
    async def extract_profile(page):
        scripts = await page.locator("script").all()

        target_script = None
        for s in scripts:
            text = await s.text_content()
            if not text:continue
            if ('profile' in text and 'followers' in text and 'isVerified' in text):
                target_script = text
                break

        if not target_script:return None

        match = re.search(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', target_script, re.DOTALL)
        if not match:return None

        raw = match.group(1)
        raw = raw.encode("utf-8").decode("unicode_escape")
        profile_start = raw.find('"profile":')
        if profile_start == -1:return None

        start = raw.find("{", profile_start)
        brace_count = 0
        end = None

        for i in range(start, len(raw)):
            char = raw[i]
            if char == "{":brace_count += 1
            elif char == "}":
                brace_count -= 1
                if brace_count == 0:
                    end = i + 1
                    break

        if not end:return None

        profile_json = raw[start:end]
        try:
            profile = json.loads(profile_json)
            return {"success": True, "profile": profile}
        except Exception as e:
            return {"success": False, "message": str(e), "raw": profile_json}

    if 'upscrolled.com' not in url or '/user/' not in url:
        return {"success": False, "message": "url is not supported"}

    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)

        data = await extract_profile(page)
        await browser.close()
    
    return {"success": True, "results": data} 


async def main():
    async with Actor:
        input_data = await Actor.get_input()
        url = input_data.get('url')
        result = await upscrolled_profile_scraper(url)
        await Actor.push_data(result)

if __name__ == "__main__":
    asyncio.run(main())