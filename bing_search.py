import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class BingSearchAutomation:
    def __init__(self):
        self.username = os.environ.get('OUTLOOK_USERNAME')
        self.password = os.environ.get('OUTLOOK_PASSWORD')
        self.driver = None
        
        # Search topics - customize these as needed
        self.search_topics = [
            "Python programming tutorials",
            "React development best practices",
            "Chennai weather today",
            "Stock market news India",
            "Electric vehicles 2025",
            "JavaScript frameworks comparison",
            "Cloud computing AWS Azure",
            "Machine learning algorithms",
            "Cryptocurrency news today",
            "Web development trends",
            "Mobile app development",
            "Database optimization techniques",
            "Cybersecurity latest threats",
            "AI artificial intelligence",
            "Data science projects",
            "Software engineering practices",
            "Tech industry news",
            "Programming languages comparison",
            "DevOps automation tools",
            "Digital transformation trends"
        ]
    
    def setup_driver(self):
        """Setup Chrome driver with headless configuration for GitHub Actions"""
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.implicitly_wait(10)
        print("✅ Chrome driver setup completed")
    
    def login_to_microsoft(self):
        """Login to Microsoft account"""
        try:
            print("🔐 Starting Microsoft account login...")
            self.driver.get("https://login.live.com/")
            
            # Enter username
            username_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "loginfmt"))
            )
            username_field.clear()
            username_field.send_keys(self.username)
            print(f"📧 Entered username: {self.username[:3]}***")
            
            # Click Next
            next_button = self.driver.find_element(By.ID, "idSIButton9")
            next_button.click()
            time.sleep(2)
            
            # Enter password
            password_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.NAME, "passwd"))
            )
            password_field.clear()
            password_field.send_keys(self.password)
            print("🔑 Password entered")
            
            # Click Sign In
            signin_button = self.driver.find_element(By.ID, "idSIButton9")
            signin_button.click()
            
            # Handle "Stay signed in?" prompt
            try:
                stay_signed_in = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.ID, "idSIButton9"))
                )
                stay_signed_in.click()
                print("✅ Clicked 'Yes' on stay signed in")
            except TimeoutException:
                print("ℹ️ Stay signed in prompt not found, continuing...")
            
            time.sleep(3)
            print("✅ Microsoft login completed successfully")
            return True
            
        except Exception as e:
            print(f"❌ Login failed: {str(e)}")
            return False
    
    def perform_bing_searches(self, num_searches=30):
        """Perform Bing searches with random topics"""
        try:
            print(f"🔍 Starting {num_searches} Bing searches...")
            
            # Navigate to Bing
            self.driver.get("https://www.bing.com")
            time.sleep(2)
            
            search_count = 0
            selected_topics = random.sample(self.search_topics, min(num_searches, len(self.search_topics)))
            
            for i, topic in enumerate(selected_topics, 1):
                try:
                    print(f"🔎 Search {i}/{num_searches}: {topic}")
                    
                    # Find search box
                    search_box = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "sb_form_q"))
                    )
                    
                    # Clear and enter search term
                    search_box.clear()
                    search_box.send_keys(topic)
                    
                    # Submit search
                    search_button = self.driver.find_element(By.ID, "sb_form_go")
                    search_button.click()
                    
                    # Wait for results to load
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.ID, "b_results"))
                    )
                    
                    search_count += 1
                    
                    # Random delay between searches (3-8 seconds)
                    delay = random.uniform(3, 8)
                    print(f"⏳ Waiting {delay:.1f} seconds...")
                    time.sleep(delay)
                    
                except Exception as e:
                    print(f"⚠️ Error in search {i}: {str(e)}")
                    continue
            
            print(f"✅ Completed {search_count} searches successfully")
            return search_count
            
        except Exception as e:
            print(f"❌ Search automation failed: {str(e)}")
            return 0
    
    def check_rewards_points(self):
        """Check current Microsoft Rewards points"""
        try:
            print("📊 Checking Microsoft Rewards points...")
            self.driver.get("https://rewards.bing.com/")
            time.sleep(3)
            
            # Try to find points display
            try:
                points_element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "[data-bi-name='rewardsUserBalance']"))
                )
                points = points_element.text
                print(f"🎯 Current points: {points}")
                return points
            except TimeoutException:
                print("ℹ️ Points information not found")
                return "Unknown"
                
        except Exception as e:
            print(f"⚠️ Could not check points: {str(e)}")
            return "Error"
    
    def run(self):
        """Main execution function"""
        if not self.username or not self.password:
            print("❌ Error: OUTLOOK_USERNAME or OUTLOOK_PASSWORD not found in environment variables")
            return
        
        try:
            print("🚀 Starting Bing Search Automation")
            print(f"📅 Running for user: {self.username[:3]}***@{self.username.split('@')[1]}")
            
            # Setup browser
            self.setup_driver()
            
            # Login to Microsoft
            if not self.login_to_microsoft():
                print("❌ Failed to login, stopping automation")
                return
            
            # Perform searches
            searches_completed = self.perform_bing_searches(30)
            
            # Check rewards points
            points = self.check_rewards_points()
            
            print("=" * 50)
            print("📈 AUTOMATION SUMMARY")
            print(f"✅ Searches completed: {searches_completed}")
            print(f"🎯 Current points: {points}")
            print("🎉 Daily Bing search automation completed successfully!")
            print("=" * 50)
            
        except Exception as e:
            print(f"💥 Critical error: {str(e)}")
        
        finally:
            if self.driver:
                self.driver.quit()
                print("🔚 Browser session closed")

if __name__ == "__main__":
    automation = BingSearchAutomation()
    automation.run()
