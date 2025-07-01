import logging
from telegram import Bot, InputMediaPhoto, InputMediaVideo
from telegram.error import TelegramError
import os
from typing import List, Optional, Union
from datetime import datetime
import random

class TelegramPostAgent:
    """
    An AI agent that automates the creation and posting of content to Telegram channels/groups.
    
    Features:
    - Post text messages
    - Post single or multiple media files (photos/videos)
    - Schedule posts (basic implementation)
    - Generate simple AI content
    - Handle errors and logging
    """
    
    def __init__(self, bot_token: str, channel_id: str):
        """
        Initialize the Telegram Post Agent.
        
        Args:
            bot_token (str): Your Telegram bot token from @BotFather
            channel_id (str): The channel/group chat ID where posts will be sent
        """
        self.bot_token = bot_token
        self.channel_id = channel_id
        self.bot = Bot(token=bot_token)
        
        # Configure logging
        logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            level=logging.INFO
        )
        self.logger = logging.getLogger(__name__)
        
        self.logger.info("Telegram Post Agent initialized")
    
    def post_text(self, text: str, disable_web_page_preview: bool = False) -> bool:
        """
        Post a text message to the Telegram channel.
        
        Args:
            text (str): The text message to post
            disable_web_page_preview (bool): Disable link previews if True
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            self.bot.send_message(
                chat_id=self.channel_id,
                text=text,
                disable_web_page_preview=disable_web_page_preview
            )
            self.logger.info(f"Text post successful: {text[:50]}...")
            return True
        except TelegramError as e:
            self.logger.error(f"Failed to post text: {e}")
            return False
    
    def post_photo(self, photo_path: str, caption: str = "") -> bool:
        """
        Post a single photo to the Telegram channel.
        
        Args:
            photo_path (str): Path to the photo file
            caption (str): Optional caption for the photo
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(photo_path, 'rb') as photo_file:
                self.bot.send_photo(
                    chat_id=self.channel_id,
                    photo=photo_file,
                    caption=caption
                )
            self.logger.info(f"Photo post successful: {photo_path}")
            return True
        except (TelegramError, FileNotFoundError) as e:
            self.logger.error(f"Failed to post photo: {e}")
            return False
    
    def post_video(self, video_path: str, caption: str = "") -> bool:
        """
        Post a single video to the Telegram channel.
        
        Args:
            video_path (str): Path to the video file
            caption (str): Optional caption for the video
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with open(video_path, 'rb') as video_file:
                self.bot.send_video(
                    chat_id=self.channel_id,
                    video=video_file,
                    caption=caption
                )
            self.logger.info(f"Video post successful: {video_path}")
            return True
        except (TelegramError, FileNotFoundError) as e:
            self.logger.error(f"Failed to post video: {e}")
            return False
    
    def post_media_group(self, media_paths: List[str], captions: Optional[List[str]] = None) -> bool:
        """
        Post a group of media files (photos/videos) as an album.
        
        Args:
            media_paths (List[str]): List of paths to media files
            captions (Optional[List[str]]): Optional list of captions for each media file
            
        Returns:
            bool: True if successful, False otherwise
        """
        if captions is None:
            captions = [""] * len(media_paths)
        
        if len(media_paths) != len(captions):
            self.logger.error("Number of media files and captions don't match")
            return False
        
        media_group = []
        for path, caption in zip(media_paths, captions):
            try:
                with open(path, 'rb') as media_file:
                    # Determine if the file is a photo or video
                    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        media = InputMediaPhoto(media=media_file, caption=caption)
                    elif path.lower().endswith(('.mp4', '.mov', '.avi')):
                        media = InputMediaVideo(media=media_file, caption=caption)
                    else:
                        self.logger.error(f"Unsupported media type: {path}")
                        return False
                    
                    media_group.append(media)
            except FileNotFoundError as e:
                self.logger.error(f"Media file not found: {e}")
                return False
        
        try:
            self.bot.send_media_group(
                chat_id=self.channel_id,
                media=media_group
            )
            self.logger.info(f"Media group post successful with {len(media_paths)} files")
            return True
        except TelegramError as e:
            self.logger.error(f"Failed to post media group: {e}")
            return False
    
    def generate_simple_content(self, topic: str) -> str:
        """
        Generate simple AI content based on a topic.
        This is a basic implementation that can be enhanced with more sophisticated AI.
        
        Args:
            topic (str): The topic to generate content about
            
        Returns:
            str: Generated content
        """
        # This is a simple placeholder - consider integrating with an LLM API
        # like OpenAI GPT for more sophisticated content generation
        templates = [
            f"Today's topic: {topic}. Did you know about this? Share your thoughts in the comments!",
            f"Exploring {topic} today. What's your experience with it?",
            f"Hot off the press! New insights about {topic}. Stay tuned for more updates.",
            f"{topic.capitalize()} is trending right now. Here's why it matters...",
            f"Let's discuss {topic} today. Drop your questions below!"
        ]
        
        return random.choice(templates)
    
    def schedule_post(self, post_func: callable, *args, post_time: datetime) -> bool:
        """
        Basic scheduling implementation for posts.
        Note: For proper scheduling, you'd want to use a task queue system.
        
        Args:
            post_func (callable): The posting function to call
            *args: Arguments to pass to the post function
            post_time (datetime): When to post the content
            
        Returns:
            bool: True if scheduling was successful (though actual posting happens later)
        """
        now = datetime.now()
        if post_time < now:
            self.logger.error("Scheduled time is in the past")
            return False
        
        # In a real implementation, you'd use a proper scheduler like APScheduler
        # This is just a placeholder to show the concept
        self.logger.info(f"Post scheduled for {post_time}. Actual scheduling would require a task queue.")
        return True
    
    def post_from_template(self, template_type: str, **kwargs) -> bool:
        """
        Post using predefined templates with placeholders.
        
        Args:
            template_type (str): Type of template to use ('announcement', 'question', 'news')
            **kwargs: Variables to fill in the template
            
        Returns:
            bool: True if successful, False otherwise
        """
        templates = {
            'announcement': "🚀 Announcement: {title}\n\n{content}\n\n#announcement",
            'question': "❓ Question of the day: {question}\n\nWhat do you think? Comment below!",
            'news': "📰 News Update: {headline}\n\n{details}\n\nRead more: {link}",
            'event': "📅 Upcoming Event: {event_name}\n\n📌 When: {date}\n📍 Where: {location}\n\n{description}"
        }
        
        if template_type not in templates:
            self.logger.error(f"Unknown template type: {template_type}")
            return False
        
        try:
            post_text = templates[template_type].format(**kwargs)
            return self.post_text(post_text)
        except KeyError as e:
            self.logger.error(f"Missing template variable: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize the agent with your bot token and channel ID
    BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
    CHANNEL_ID = "@your_channel_username"  # or use the numeric channel ID
    
    agent = TelegramPostAgent(BOT_TOKEN, CHANNEL_ID)
    
    # Example 1: Post a text message
    agent.post_text("Hello from the Telegram Post Agent! This is an automated message.")
    
    # Example 2: Generate and post AI content
    ai_content = agent.generate_simple_content("artificial intelligence")
    agent.post_text(ai_content)
    
    # Example 3: Post a photo with caption
    # agent.post_photo("example.jpg", "Check out this example image!")
    
    # Example 4: Post using a template
    agent.post_from_template(
        'news',
        headline="New AI Breakthrough",
        details="Researchers have developed a new AI model that can...",
        link="https://example.com/news"
    )
    
    # Note: For media posting examples to work, you need actual files
    # Uncomment and modify these when you have actual files to post
    # Example 5: Post a video
    # agent.post_video("example.mp4", "Check out our demo video!")
    
    # Example 6: Post a media group
    # agent.post_media_group(
    #     ["photo1.jpg", "photo2.jpg", "video1.mp4"],
    #     ["Caption 1", "Caption 2", "Video caption"]
    # )