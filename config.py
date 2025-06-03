
import os
from dotenv import load_dotenv

load_dotenv()

# API keys
OPENAI_API_KEY = "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"
SERPAPI_API_KEY="83e4745e32031a5a4a423904c5b3b21c1a97f513aca4ac3eec7cf3f29777e25b"

# Model settings
LLM_MODEL = "gpt-3.5-turbo" 

# Job search settings
DEFAULT_JOB_COUNT = 5
JOB_PLATFORMS = ["LinkedIn", "Indeed", "Glassdoor", "ZipRecruiter", "Monster"]


COLORS = {
    # Primary palette
    "primary": "#1C4E80",      # Dark blue for main elements and headers
    "secondary": "#0091D5",    # Medium blue for secondary elements
    "tertiary": "#6BB4C0",     # Teal blue for tertiary elements
    
    # Accent colors
    "accent": "#F17300",       # Orange for highlighting
    "accent1": "#3E7CB1",      # Steel blue for subtler accents
    "accent2": "#44BBA4",      # Seafoam for highlighting information
    "accent3": "#F17300",      # Orange for call-to-action buttons
    
    # Functional colors
    "success": "#26A69A",      # Teal green for success messages
    "warning": "#F9A825",      # Golden yellow for warnings
    "error": "#E53935",        # Bright red for errors
    "info": "#0277BD",         # Information blue
    
    # Background and text - BASIC PROFESSIONAL STYLE
    "background": "#F5F7FA",   # Light blue-gray for backgrounds
    "card_bg": "#FFFFFF",      # White for card backgrounds
    "text": "#FFFFFF",         # White for text on dark backgrounds
    "text_dark": "#000000",    # Black for text on light backgrounds
    "text_light": "#333333",   # Dark gray for secondary text
    "text_red": "#FF5252",     # Red color for high-contrast text
    "panel_bg": "#F0F5FF"      # Light blue background for panels
}
