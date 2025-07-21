from fetch.youtube_fetcher import fetch_youtube_updates
from fetch.linkedin_scraper import fetch_linkedin_posts
from summarize.summarizer import summarize_texts
from notify.slack_notifier import send_to_slack
from notify.email_notifier import send_email
import config
from config import EMAIL
from notify.email_notifier import send_email
import csv

def save_summary_to_csv(summary, file_path='influencer_summary.csv'):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Trend Summary'])  # Header
        for line in summary.split('\n'):
            if line.strip():  # Skip empty lines
                writer.writerow([line.strip()])




print("start")
def run_all():
    print("start")
    influencers = get_top_influencers()
    posts = fetch_recent_posts(influencers)
    summary = analyze_sentiment(posts)

    save_summary_to_csv(summary)  # Save CSV

    send_email(
        subject="Influencer Trend Summary",
        body="Here is the summary CSV report attached.",
        to=EMAIL["receiver"],
        attachment_path="influencer_summary.csv"  # NEW: attach the file
    )

    print("📺 Fetching YouTube updates...")
    for channel_id in config.INFLUENCERS['youtube']:
        updates = fetch_youtube_updates(channel_id, config.YOUTUBE_API_KEY)
        print(f"Found {len(updates)} YouTube updates.")
        all_texts.extend(updates)

    print("💼 Fetching LinkedIn posts...")
    for linkedin_url in config.INFLUENCERS['linkedin']:
        posts = fetch_linkedin_posts(linkedin_url)
        print(f"Found {len(posts)} LinkedIn posts.")
        all_texts.extend(posts)

    if not all_texts:
        print("⚠️ No new updates found.")
        return

    print("🧠 Summarizing content...")
    summary = summarize_texts(all_texts)
    print("📤 Sending summary to Slack and Email...")
    send_to_slack(summary, config.SLACK_WEBHOOK_URL)
    send_email("Influencer Trend Summary", summary, config.RECEIVER_EMAIL)


    print("✅ Done.")

# Run it
def run_all():
    summary = "Here is the weekly influencer report..."
    send_email("Influencer Trend Summary", summary, EMAIL["receiver"])

if __name__ == "__main__":
    run_all()
