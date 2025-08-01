"""
Example usage of the Instagram Profile Scraper
"""

from instagram_scraper import InstagramScraper
import os

def example_basic_usage():
    """
    Basic example of how to use the Instagram scraper programmatically.
    """
    print("=== Basic Usage Example ===")
    
    # Create scraper instance with user's Firefox profile path
    profile_path = input("Enter your Firefox profile path: ")
    scraper = InstagramScraper(profile_path=profile_path)
    
    # Example profile name (replace with actual profile)
    profile_name = "example_profile"
    
    try:
        # Process the profile with default settings
        result_file = scraper.process_instagram_profile(
            profile_name=profile_name,
            max_posts=50,  # Start with a small number for testing (requests over 500 post make take longer and some may not process correctly)
            output_dir="example_output"
        )
        
        if result_file:
            print(f"✅ Success! Data saved to: {result_file}")
            
            # You can now process the CSV file
            import pandas as pd
            df = pd.read_csv(result_file)
            print(f"📊 Summary: {len(df)} posts scraped")
            print(f"📅 Date range: {df['date'].min()} to {df['date'].max()}")
            print(f"❤️ Total likes: {df['likes'].sum()}")
            print(f"💬 Total comments: {df['comments_count'].sum()}")
            
        else:
            print("❌ Failed to scrape data")
            
    except Exception as e:
        print(f"Error: {e}")

def example_custom_settings():
    """
    Example with custom settings and error handling.
    """
    print("\n=== Custom Settings Example ===")
    
    # Custom Firefox profile path (adjust for your system)
    custom_profile_path = r"C:\Users\YourUser\AppData\Roaming\Mozilla\Firefox\Profiles\your.profile"
    
    # Create scraper with custom profile
    scraper = InstagramScraper(profile_path=custom_profile_path)
    
    profile_name = "example_profile"
    
    try:
        result_file = scraper.process_instagram_profile(
            profile_name=profile_name,
            max_posts=200,
            output_dir="custom_output"
        )
        
        if result_file and os.path.exists(result_file):
            print(f"✅ Custom scraping completed: {result_file}")
            
            # Basic analysis
            import pandas as pd
            df = pd.read_csv(result_file)
            
            print(f"\n📈 Analytics:")
            print(f"   • Posts: {len(df)}")
            print(f"   • Videos: {df['is_video'].sum()}")
            print(f"   • Images: {len(df) - df['is_video'].sum()}")
            print(f"   • Avg likes: {df['likes'].mean():.1f}")
            print(f"   • Avg comments: {df['comments_count'].mean():.1f}")
            
        else:
            print("❌ Custom scraping failed")
            
    except Exception as e:
        print(f"Error in custom settings example: {e}")

def example_batch_processing():
    """
    Example of processing multiple profiles.
    """
    print("\n=== Batch Processing Example ===")
    
    # List of profiles to process
    profiles = ["profile1", "profile2", "profile3"]  # Replace with actual profiles
    
    profile_path = input("Enter your Firefox profile path: ")
    scraper = InstagramScraper(profile_path=profile_path)
    results = {}
    
    for profile in profiles:
        print(f"\n🔄 Processing {profile}...")
        
        try:
            result_file = scraper.process_instagram_profile(
                profile_name=profile,
                max_posts=100,
                output_dir="batch_output"
            )
            
            results[profile] = result_file
            
            if result_file:
                print(f"   ✅ {profile}: Success")
            else:
                print(f"   ❌ {profile}: Failed")
                
        except Exception as e:
            print(f"   ❌ {profile}: Error - {e}")
            results[profile] = None
    
    # Summary
    successful = sum(1 for r in results.values() if r is not None)
    print(f"\n📊 Batch Summary: {successful}/{len(profiles)} profiles processed successfully")
    
    return results

def example_data_analysis():
    """
    Example of analyzing scraped data.
    """
    print("\n=== Data Analysis Example ===")
    
    # This assumes you have some CSV files from previous scraping
    import pandas as pd
    import glob
    
    csv_files = glob.glob("output/*.csv")
    
    if not csv_files:
        print("No CSV files found. Run scraping first.")
        return
    
    print(f"Found {len(csv_files)} CSV files")
    
    for csv_file in csv_files[:3]:  # Analyze first 3 files
        try:
            df = pd.read_csv(csv_file)
            profile_name = os.path.basename(csv_file).split('_')[0]
            
            print(f"\n📊 Analysis for {profile_name}:")
            print(f"   • Total posts: {len(df)}")
            print(f"   • Date range: {df['date'].min()} to {df['date'].max()}")
            print(f"   • Total engagement: {df['likes'].sum() + df['comments_count'].sum()}")
            print(f"   • Top post likes: {df['likes'].max()}")
            print(f"   • Video ratio: {df['is_video'].mean()*100:.1f}%")
            
            # Find most engaging posts
            df['engagement'] = df['likes'] + df['comments_count']
            top_post = df.loc[df['engagement'].idxmax()]
            print(f"   • Most engaging post: {top_post['engagement']} interactions")
            
        except Exception as e:
            print(f"Error analyzing {csv_file}: {e}")

if __name__ == "__main__":
    print("🚀 Instagram Profile Scraper - Usage Examples")
    print("=" * 50)
    
    # Run examples (comment out the ones you don't want to run)
    
    # Basic usage
    # example_basic_usage()
    
    # Custom settings
    # example_custom_settings()
    
    # Batch processing
    # example_batch_processing()
    
    # Data analysis
    example_data_analysis()
    
    print("\n✨ Examples completed!")
    print("\nNote: Replace 'example_profile' with actual Instagram profile names")
    print("Make sure you're logged into Instagram in your Firefox profile before running.")